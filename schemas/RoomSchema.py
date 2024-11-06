from pydantic import BaseModel

class RoomSchema(BaseModel):
    RoomName: str
    RoomMaximum: int