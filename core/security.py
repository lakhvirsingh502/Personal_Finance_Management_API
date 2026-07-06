from jose import jwt
import bcrypt
secret_key = "123456"
def create_token(id:int):
    data = {
        "user_id":id
    }
    return jwt.encode(
        data,
        secret_key,
        algorithm="HS256"
    )
def access_token(token):
    return jwt.decode(
        token,
        secret_key,
        algorithms="HS256"
    )


def create_hash_password(password:str):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

def verify_password(password:str,hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),hashed_password.encode("utf-8")
    )
