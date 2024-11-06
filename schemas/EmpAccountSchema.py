from pydantic import BaseModel

class EmpAccountSchema(BaseModel):
    UserName: str
    Password: str

class EmpAccountPasswordSchema(BaseModel):
    Password: str