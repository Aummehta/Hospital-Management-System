from beanie import Document
from datetime import datetime
from typing import Optional

class AddDoctor(Document):
    name: str
    age: int
    address: str
    contact: int
    email: str
    salary: int
    speciality: str
    gender: str
    birthdate: datetime
    status: int = 0

    class Settings:
        name = "AddDoctorData"

class DoctorLogin(Document):
    name: str
    speciality: str
    contact: int
    email: str
    password: str

    class Settings:
        name = "DoctorLogin"
