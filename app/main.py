from fastapi import FastAPI
from app.routers.dashboard import router as dashboard_router
from app.db import engine , Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title= "Asynce Dashboard API")


app.include_router(dashboard_router)


@app.get("/")
async def root():
    return {"status": "ok"}