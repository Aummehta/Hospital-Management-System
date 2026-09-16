from beanie import Document
from pydantic import Field

class AdminCredential(Document):
    name: str
    email: str
    password: str

    class Settings:
        name = "AdminCredential"
