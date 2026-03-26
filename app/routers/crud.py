from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.db import AsyncSessionLocal
from app.db import get_db
from app.models.order import Order
from app.models.user import User
import asyncio
import httpx

router = APIRouter()

@router.get("/get_user/{user_id}")
async def get_user(user_id:int):
    async with AsyncSessionLocal() as db :
        user_result = await db.execute(select(User).where(User.id == user_id))
        return user_result.scalar_one_or_none()

@router.get("/get_orders/{user_id}")
async def get_orders(user_id : int ):
    async with AsyncSessionLocal() as db :
        orders_result = await db.execute(select(Order).where(Order.user_id == user_id))
        return orders_result.scalars().all()


@router.get("/get_external_data")
async def get_external_data(user_id : int ):
    url =  f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    async with httpx.AsyncClient() as client :
        response = await client.get(url)
        response.raise_for_status()

        return response.json()
   