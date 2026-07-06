from models.user import User
from models.expense import Expense
from core.database import Base,engine

Base.metadata.create_all(bind=engine)