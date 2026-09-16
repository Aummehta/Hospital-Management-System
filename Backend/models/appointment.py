from beanie import Document
from typing import List, Optional
from datetime import datetime

class Appointment(Document):
    date: Optional[datetime] = None
    time: Optional[datetime] = None
    name: str
    age: str
    gender: List[str]
    appreason: str
    doctorname: str
    doctoremail: str
    status: int = 0
    email: Optional[str] = None

    class Settings:
        name = "Appointmentschema"
