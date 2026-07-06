from fastapi import Depends,HTTPException
from dependencies.current_user import get_user
from core.database import get_db
from sqlalchemy.orm import Session

def get_role(user = Depends(get_user), db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found."
        )
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to do these actions."
        )
    return user