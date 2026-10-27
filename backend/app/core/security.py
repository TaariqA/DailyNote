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
from app.core.config import settings

#hashes user pw when account is made
def password_hash(password: str):
    passwordInBytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(passwordInBytes, salt)

    return hash

def password_authenticate(enteredPw: str, userPwHash: bytes):
    enteredPwBytes = enteredPw.encode('utf-8')
    result = bcrypt.checkpw(enteredPwBytes, userPwHash)

    return result

def create_access_token(data: dict, expires_minutes: int = settings.access_token_expire_minutes) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm= settings.jwt_algorithm)

def authenticate_user(username: str, password: str):
    pass
    #finish soon, 