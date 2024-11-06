from pydantic import BaseModel, EmailStr

class BranchSchema(BaseModel):
    BranchName: str
    BranchAddress: str
    BranchPhoneNumber: str
    BranchEmailAddress: EmailStr