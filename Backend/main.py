from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from beanie import init_beanie
import uvicorn
import os
from contextlib import asynccontextmanager

# Import all models for Beanie init
from models.admin import AdminCredential
from models.appointment import Appointment
from models.doctor import AddDoctor, DoctorLogin
from models.employee import AddEmployee
from models.leave import ApplyLeave
from models.medicine import AddMedicine
from models.patient import AddPatient
from models.patient_credential import CheckPatientCredential
from models.prescription import Prescription

# Import all routers
from routers.auth import router as auth_router
from routers.patient import router as patient_router
from routers.employee import router as employee_router
from routers.medicine import router as medicine_router
from routers.doctor import router as doctor_router
from routers.leave import router as leave_router
from routers.prescription import router as prescription_router
from routers.appointment import router as appointment_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB connection on startup
    db = await init_db()
    
    # Initialize Beanie
    await init_beanie(database=db, document_models=[
        AdminCredential,
        Appointment,
        AddDoctor,
        DoctorLogin,
        AddEmployee,
        ApplyLeave,
        AddMedicine,
        AddPatient,
        CheckPatientCredential,
        Prescription
    ])
    
    yield

app = FastAPI(lifespan=lifespan)

# Add CORS middleware exactly like `app.use(cors())`
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth_router)
app.include_router(patient_router)
app.include_router(employee_router)
app.include_router(medicine_router)
app.include_router(doctor_router)
app.include_router(leave_router)
app.include_router(prescription_router)
app.include_router(appointment_router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1337))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
