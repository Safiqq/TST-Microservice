from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

import databases.users as db
from auth.jwt import create_access_token, verify_token
from models.users import User, Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_router = APIRouter(tags=["Users"])


@user_router.post("/token", response_model=Token)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get_user_by_username(form_data.username)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print(0)
    if not user:
        raise credentials_exception
    print(1)
    if not pwd_context.verify(form_data.password, user.get("password")):
        raise credentials_exception
    print(2)
    access_token = create_access_token({"sub": user.get("username")})
    print(3)
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post("/register")
async def register(user_data: User):
    user = db.get_user_by_username(user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    user_data.password = pwd_context.hash(user_data.password)
    _id = db.create_user(user_data.to_db())
    return {"message": f"User created successfully with ID {_id}"}
