import uvicorn
from fastapi import FastAPI

from core.database import database
from routers.products import product_router
from core.config import API_V1

app = FastAPI()

app.include_router(product_router, prefix=f"{API_V1}", tags=["Product Routes"])


@app.get('/')
async def main_page():
    return {"detail": "Welcome to main page."}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
