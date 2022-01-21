from fastapi import APIRouter, status

from core import schemes
from db_commands.users import insert_user, get_user
from routers.functions import authentication

user_router = APIRouter()


@user_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(user: schemes.UserIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = await authentication.get_hashed_password(user_info["password"])
    user_id = await insert_user(user_info)
    user_data = await get_user(user_id)

    return {
        "status": status.HTTP_201_CREATED,
        "data": f"Hello {user_data['username']}, please check your email, and verify it."
    }

