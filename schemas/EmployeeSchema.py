from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeSchema(BaseModel):
    FirstName: str
    MiddleName: str = None
    LastName: str
    DOB: date
    Gender: str
    Height: Optional[float]
    Weight: Optional[float]

class EmployeeUpdateSchema(BaseModel):
    FirstName: str = None
    MiddleName: str = None
    LastName: str = None
    DOB: date = None
    Gender: str = None
    Height: Optional[float] = None
    Weight: Optional[float] = None
    # = None means optional, allows null values