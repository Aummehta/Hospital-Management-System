from beanie import Document

class CheckPatientCredential(Document):
    name: str
    email: str
    password: str

    class Settings:
        name = "PatientCredential"
