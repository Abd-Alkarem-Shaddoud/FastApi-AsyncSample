
# python -m tests.seeder

import asyncio
from sqlalchemy import delete

from app.db import AsyncSessionLocal, engine, Base
from app.models.user import User
from app.models.order import Order


USERS_DATA = [
    {"name": "Abd-Alkrem", "email": "abd@test.com"},
    {"name": "user2", "email": "bob@test.com"},
    {"name": "Charlie", "email": "charlie@test.com"},
]


async def seed_db():
    async with AsyncSessionLocal() as session:

        
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

      
        await session.execute(delete(Order))
        await session.execute(delete(User))
        await session.commit()

       
        users = []
        for data in USERS_DATA:
            user = User(**data)
            session.add(user)
            users.append(user)

        await session.commit()

        
        await session.refresh(users[0])
        await session.refresh(users[1])
        await session.refresh(users[2])

        
        orders = [
            Order(user_id=users[0].id, product="Laptop"),
            Order(user_id=users[0].id, product="Mouse"),
            Order(user_id=users[1].id, product="Keyboard"),
            Order(user_id=users[2].id, product="Monitor"),
        ]

        session.add_all(orders)
        await session.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed_db())