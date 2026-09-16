from beanie import Document
from datetime import datetime
from typing import Optional

class AddPatient(Document):
    fname: str
    mname: str
    lname: str
    email: str
    age: int
    mobile: str
    gender: str
    bloodgroup: str
    marriedstatus: str
    address: str
    height: float
    weight: float
    status: int = 1
    birthdate: Optional[datetime] = None

    class Settings:
        name = "AddPatientData"
