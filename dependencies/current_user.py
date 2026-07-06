from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import access_token
from models.user import User
security = HTTPBearer()

def get_user(credentials = Depends(security), db:Session = Depends(get_db)):
    token = credentials.credentials
    data = access_token(token)
    user = db.query(User).filter(User.id == data["user_id"]).first()
    return user