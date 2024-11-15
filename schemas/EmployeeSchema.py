from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeSchema(BaseModel):
    FirstName: str
    MiddleName: str = None
    LastName: str
    DOB: date
    Gender: str

class EmployeeUpdateSchema(BaseModel):
    FirstName: str = None
    MiddleName: str = None
    LastName: str = None
    DOB: date = None
    Gender: str = None

    # = None means optional, allows null values