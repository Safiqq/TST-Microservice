"""
This API provides functionalities for user management, including generating JWT tokens and user
registration.
"""
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

import app.databases.user as db
from app.auth.jwt import create_access_token
from app.schemas.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_router = APIRouter(tags=["Users"])


@user_router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Generates a JSON Web Token (JWT) for an existing user.

    Args:
        form_data: An OAuth2PasswordRequestForm object containing username and password.

    Returns:
        A dictionary containing the access token and token type.

    Raises:
        HTTPException 401: If the username or password is incorrect.
    """
    user = db.get_user_by_username(form_data.username)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not user:
        raise credentials_exception
    if not pwd_context.verify(form_data.password, user.get("password")):
        raise credentials_exception
    access_token = create_access_token(
        {"sub": user.get("username"), "admin": user.get("admin")}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post("/register")
async def register(form_data: User):
    """
    Registers a new user.

    Args:
        form_data: A User object containing user information.

    Returns:
        A dictionary containing a success message.

    Raises:
        HTTPException 400: If a user with the same username already exists.
    """
    user = db.get_user_by_username(form_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    form_data.password = pwd_context.hash(form_data.password)
    _id = db.create_user(form_data.to_db())
    # print(form_data)
    return {"message": f"User created successfully with ID {_id}"}
