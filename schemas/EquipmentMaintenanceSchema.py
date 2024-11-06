from pydantic import BaseModel
from datetime import date

class EquipmentMaintenanceSchema(BaseModel):
    EquipmentName: str
    MaintenanceDate: date
    Cost: int
    Duration: str
    Description: str