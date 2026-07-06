from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="expenses")