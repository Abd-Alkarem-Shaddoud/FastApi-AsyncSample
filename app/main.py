from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.dashboard import router as dashboard_router
from app.db import engine , Base, init_db


@asynccontextmanager
async def lifespan(app : FastAPI) :
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(dashboard_router)



@app.get("/")
async def root():
    return {"status": "ok"}

