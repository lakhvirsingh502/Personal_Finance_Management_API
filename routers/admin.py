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
@router.get("/admin/list/users", response_model=list[UserResponse])
def show(skip:int = Query(0,ge=0),limit:int=Query(10,ge=1),user = Depends(get_role),db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail = "User not found."
        )
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/admin/list/allexpenses")
def show(skip = Query(0,ge=0),limit=Query(10,le=1),user = Depends(get_role),  db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    return db.query(Expense).offset(skip).limit(limit).all()

@router.delete("/admin/delete/users/{id}")
def admin_delete_user(id:int, user = Depends(get_role), db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"

        )
    db.delete(user)
    return{
        "message":"Deleted successfully."
    }

@router.delete("/admin/delete/expenses/{id}")
def admin_delete_expense(id:int, user=Depends(get_role),db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    expense = db.query(Expense).filter(Expense.id == id).first()
    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense  not found."
        )
    db.delete(expense)
    return{
        "message" : "Deleted Successfully."
    }
