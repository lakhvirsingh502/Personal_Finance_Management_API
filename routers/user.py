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

@router.get("/list/user/expense", response_model=list[ExpenseResponse])
def show(category:str=None,sort:str = "asc",skip:int=Query(0,ge=0),limit:int=Query(10,ge=1),user = Depends(get_user),db:Session=Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not found."
        )
    
    
    query = db.query(Expense).filter(Expense.user_id==user.id)
   
    
    if category:
        query = query.filter(Expense.category==category)
    if sort =="desc":
        query = query.order_by(Expense.amount.desc())
    else:
        query = query.order_by(Expense.amount.asc())
    return query.offset(skip).limit(limit).all()

@router.delete("/user/expense/delete/{id}")
def user_delete(id:int,user = Depends(get_user), db:Session = Depends(get_db)):
    if user is None:
        raise HTTPException(
            status_code=401,
            detail = "User not found."
        )
    expense = db.query(Expense).filter(Expense.user_id == user.id,Expense.id==id).first()
    if expense is None:
        raise HTTPException(
            status_code=404,
            detail = "Expense not found."
        )
    db.delete(expense)
    return {
        "message" : "Deleted Successfully."
    }
