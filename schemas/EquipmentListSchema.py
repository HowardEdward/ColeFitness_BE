from pydantic import BaseModel

class EquipmentListSchema(BaseModel):
    EquipmentName: str
    Quantity: int