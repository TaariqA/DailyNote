'''password hashing (CHECK)
password verification (CHECK)
token creation
token validation
extracting the current user from a request
checking if the user is authenticated
optional role/permission checks'''
import bcrypt
from backend.app.core.config import settings
from datetime import datetime,  timedelta, timezone
from jose import jwt, JWTError

#hashes user pw when account is made
def hash_user_password(password: str):
    password_in_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(password_in_bytes, salt)

    return hash

def password_authenticate(entered_pw: str, user_pw_hash: bytes):
    entered_pw_bytes = entered_pw.encode('utf-8')
    result = bcrypt.checkpw(entered_pw_bytes, user_pw_hash)

    return result

def create_token(expires_minutes: int = settings.access_token_expire_minutes):
    expiry = datetime.now(timezone.utc) + timedelta(minutes = expires_minutes)
    to_encode = ({"exp" : expiry})
    return jwt.encode(to_encode, settings.secret_key, algorithm = settings.jwt_algorithm)

def login_authenticate(entered_user, entered_pw):
    pass

