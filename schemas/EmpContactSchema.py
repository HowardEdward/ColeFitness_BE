from pydantic import BaseModel, EmailStr

class EmpContactSchema(BaseModel):
    PhoneNumber: str
    EmailAddress: EmailStr
    Address: str
    ContactType: str