from pydantic import BaseModel
class CreateExpense(BaseModel):
    title : str
    amount : int
    category : str

class ExpenseResponse(BaseModel):
    title : str
    amount : int
    category : str

    class config:
        from_attributes : True