from beanie import Document
from datetime import datetime
from typing import Optional

class AddMedicine(Document):
    name: str
    description: str
    category: str
    expirydate: datetime
    mfgdate: datetime
    quantity: Optional[int] = None
    price: Optional[int] = None
    myFile: Optional[str] = None

    class Settings:
        name = "AddMedicineData"
