from pydantic import BaseModel
from datetime import datetime

class ScheduleSchema(BaseModel):
    DateTime: datetime