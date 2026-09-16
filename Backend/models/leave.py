from beanie import Document
from datetime import datetime
from typing import Optional

class ApplyLeave(Document):
    startdate: datetime
    enddate: datetime
    duration: int
    reason: str
    approve: int = 0
    name: Optional[str] = None
    email: Optional[str] = None

    class Settings:
        name = "AddLeaveSchema"
