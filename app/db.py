from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/postgres"

engine = create_async_engine(DATABASE_URL, pool_pre_ping = True ,echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine ,
    class_= AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn :
       await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session