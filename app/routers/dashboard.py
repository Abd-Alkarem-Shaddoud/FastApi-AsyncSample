from fastapi import APIRouter
import asyncio
from app.routers.crud import get_external_data, get_orders, get_user
router = APIRouter()

#====================== WAY1 ====================

@router.get("/dashboard/{user_id}")
async def dashboard(user_id: int):

    async with asyncio.TaskGroup() as tg:

        user_task = tg.create_task(get_user(user_id))
        orders_task = tg.create_task(get_orders(user_id))
        external_task = tg.create_task(get_external_data(user_id))

    # بعد انتهاء TaskGroup (هنا النتائج جاهزة)
    return {
        "user_data": user_task.result(),
        "orders_data": orders_task.result(),
        "external_data": external_task.result(),
    }


#====================== WAY2 ====================

# @router.get("/dashboard/{user_id}")
# async def dashboard(user_id: int, db: AsyncSession = Depends(get_db)):

#     user, orders, external = await asyncio.gather(
#         get_user(user_id, db),
#         get_orders(user_id, db),
#         get_external_data(user_id)
#     )

#     return {
#         "user_data": user,
#         "orders_data": orders,
#         "external_data": external,
#     }
