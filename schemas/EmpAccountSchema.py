from pydantic import BaseModel

class AccountSchema(BaseModel):
    UserName: str
    Password: str

class PasswordSchema(BaseModel):
    Password: str