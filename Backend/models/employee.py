from beanie import Document
from datetime import datetime
from typing import Optional

class AddEmployee(Document):
    name: str
    age: int
    address: str
    contact: int
    email: str
    salary: int
    classification: Optional[str] = None
    gender: str
    birthdate: datetime

    class Settings:
        name = "AddEmployeeData"
