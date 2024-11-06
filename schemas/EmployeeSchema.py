from pydantic import BaseModel
from datetime import date

class EmployeeSchema(BaseModel):
    FirstName: str
    MiddleName: str = None
    LastName: str
    DOB: date
    Gender: str
    Height: float
    Weight: float
    
    # = None means optional, allows null values