'''password hashing
password verification
token creation
token validation
extracting the current user from a request
checking if the user is authenticated
optional role/permission checks'''
import bcrypt
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from backend.app.core.config import settings
from backend.app.services.user_logic import get_user_by_email
from sqlalchemy.orm import Session

#hashes user pw when account is made
def password_hash(password: str):
    password_in_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(password_in_bytes, salt)

    return hash

def password_authenticate(enteredPw: str, userPwHash: bytes):
    entered_pw_bytes = enteredPw.encode('utf-8')
    result = bcrypt.checkpw(entered_pw_bytes, userPwHash)

    return result

def create_access_token(data: dict, expires_minutes: int = settings.access_token_expire_minutes) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm= settings.jwt_algorithm)

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_email(username, db)
    #check if user account exists and authenticate password