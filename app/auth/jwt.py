from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

from config import *

SECRET_KEY = config.get("SECRET_KEY")
ALGORITHM = config.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(config.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials",
                            headers={"WWW-Authentication": "Bearer"})
    expire = payload.get("exp")
    if expire < int(datetime.now().strftime("%s")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credentials are expired",
                            headers={"WWW-Authentication": "Bearer"})
    return payload.get("sub")