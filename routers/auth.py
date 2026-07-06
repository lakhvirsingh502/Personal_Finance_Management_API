from core.database import get_db
from fastapi import FastAPI, Depends,HTTPException,Query,APIRouter

from schemas.expense import CreateExpense, ExpenseResponse
from schemas.user import CreateUser, UserResponse,Login
from core.security import create_hash_password,verify_password
from core.security import create_token, access_token
from dependencies.current_user import get_user
from dependencies.role import get_role
from sqlalchemy.orm import Session
from models.user import User
from models.expense import Expense

router = APIRouter()
@router.post("/Register")
def register(st:CreateUser,db:Session=Depends(get_db)):
    hashed_password = create_hash_password(st.password)
    new_user = User(
        name = st.name,
        password = hashed_password,
        role = st.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "message" : "User created successfully."
    }

@router.post("/Login")
def login(st:Login, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.name==st.name).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User Not Found."
        )
    password = verify_password(st.password,user.password)
    if not password:
        raise HTTPException(
            status_code=403,
            detail = "Invalid Credentials."
        )
    token = create_token(user.id)
    return {
        "Token" : token
    }