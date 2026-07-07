from fastapi import APIRouter,FastAPI
from routers import auth,admin,expense,user
import models




app = FastAPI(
    title="Personal Finance Manager App",
    version="1.0.0"

)
@app.get("/")
def home():
    return {"message": "Personal Finance Management API is running"}
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(expense.router)