'''password hashing
password verification
token creation
token validation
extracting the current user from a request
checking if the user is authenticated
optional role/permission checks'''
import bcrypt

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