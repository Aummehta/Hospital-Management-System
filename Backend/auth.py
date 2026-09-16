import jwt
from typing import Optional, Dict

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

def create_access_token(data: dict) -> str:
    """
    Replicates the exact JWT signing logic from Express.
    Mongoose app used: jwt.sign({ name: user.name, email: user.email }, 'secret123')
    No expiration was set in the original code.
    """
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Optional[Dict]:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.PyJWTError:
        return None
