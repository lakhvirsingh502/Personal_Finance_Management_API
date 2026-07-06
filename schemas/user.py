from pydantic import BaseModel

class CreateUser(BaseModel):
    name : str
    password : str
    role : str

class UserResponse(BaseModel):
    id : int
    name:str
    role:str

    class config:
        from_attributes = True

class Login(BaseModel):
    name : str
    password : str

