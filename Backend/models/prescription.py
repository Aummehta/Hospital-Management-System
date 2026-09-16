from beanie import Document
from datetime import datetime, timedelta
from typing import List, Optional
from pydantic import Field

def get_default_date():
    return datetime.utcnow() + timedelta(days=7)

class Prescription(Document):
    date: datetime = Field(default_factory=get_default_date)
    patientname: str
    patientemail: str
    category: str
    medicine: List[str]  # Originally Array
    description: str
    doctorname: str
    doctoremail: str

    class Settings:
        name = "PrescriptionSchema"
