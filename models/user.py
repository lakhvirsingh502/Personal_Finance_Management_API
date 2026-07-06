from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    role = Column(String, default="user")
    expenses = relationship("Expense", back_populates="users")
