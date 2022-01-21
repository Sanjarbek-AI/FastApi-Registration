from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


async def get_hashed_password(password):
    return pwd_context.hash(password)
