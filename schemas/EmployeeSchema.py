from pydantic import BaseModel, EmailStr
from datetime import date, datetime

class EmployeeSchema(BaseModel):
    FirstName: str
    MiddleName: str = None
    LastName: str
    DOB: date
    RoleKey: str = None
    ContactID: int = None
    # = None means optional, allows null values