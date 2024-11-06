from pydantic import BaseModel
from datetime import date

class EquipmentSchema(BaseModel):
    EquipmentName: str
    PurchasedDate: date

