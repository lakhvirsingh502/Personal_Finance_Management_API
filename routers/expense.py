from core.database import get_db
from fastapi import FastAPI, Depends,HTTPException,Query,APIRouter
from schemas.user import CreateUser,Login,UserResponse
from schemas.expense import CreateExpense, ExpenseResponse
from core.security import create_hash_password,verify_password
from core.security import create_token, access_token
from dependencies.current_user import get_user
from dependencies.role import get_role
from sqlalchemy.orm import Session
from models.expense import  Expense
from models.user import User
router = APIRouter()

@router.post("/user/expense")
def create_expense(st:CreateExpense,user = Depends(get_user),db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    new_expense = Expense(
        title = st.title,
        amount = st.amount,
        category = st.category
    )
    user.expenses.append(new_expense)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return{
        "message" : "Expense created successfully."
    }



