'''password hashing
password verification
token creation
token validation
extracting the current user from a request
checking if the user is authenticated
optional role/permission checks'''
import bcrypt

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