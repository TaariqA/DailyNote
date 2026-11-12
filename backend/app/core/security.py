'''password hashing (CHECK)
password verification (CHECK)
token creation
token validation
extracting the current user from a request
checking if the user is authenticated
optional role/permission checks'''
import bcrypt
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from backend.app.core.config import settings
from backend.app.services.user_logic import get_user_by_email,get_user_by_id
from backend.app.schemas.user import UserOut
from sqlalchemy.orm import Session

from typing import Optional

from fastapi import Depends, HTTPException, status

#hashes user pw when account is made
def password_hash(password: str):
    password_in_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(password_in_bytes, salt)

    return hash

def password_authenticate(entered_pw: str, user_pw_hash: bytes):
    entered_pw_bytes = entered_pw.encode('utf-8')
    result = bcrypt.checkpw(entered_pw_bytes, user_pw_hash)

    return result

def create_access_token(data: dict, expires_minutes: int = settings.access_token_expire_minutes) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm= settings.jwt_algorithm)

def authenticate_user(email: str, password: str, db: Session):
    user = get_user_by_email(email, db)

    if not password_authenticate(password, user.password_hash):
        return None
    return user

async def get_current_user(db: Session, token: str = Depends(settings.oauth2_scheme)) -> UserOut:
    cred_exec = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=settings.jwt_algorithm)
        id: Optional[str] = payload.get("sub")
        if id is None:
            raise cred_exec
    except JWTError:
        raise cred_exec

    user = get_user_by_id(int(id), db)
    if not user:
        raise cred_exec
    return UserOut(email=user.email,name=user.name,user_id=user.id)