from pydantic import BaseModel, EmailStr

class EmpContactSchema(BaseModel):
    ContactID: int
    EmployeeID: int
    PhoneNumber: str
    EmailAddress: EmailStr
    Address: str
    ContactType: str