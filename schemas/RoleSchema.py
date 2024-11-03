from pydantic import BaseModel

class RoleSchema(BaseModel):
    RoleName: str
    RoleKey: str