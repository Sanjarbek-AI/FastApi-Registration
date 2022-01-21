import datetime
from fastapi import HTTPException, status
from core.database import database
from core.models import user


async def insert_user(data: dict):
    try:
        query = user.insert().values(**data, is_verified=False, created_at=datetime.datetime.utcnow())
        return await database.execute(query)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Something is wrong, user not saved.")


async def get_user(user_id: int):
    try:
        query = user.select().where(user.c.id == user_id)
        return await database.fetch_one(query)
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found with this id")
