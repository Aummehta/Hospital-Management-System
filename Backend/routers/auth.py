from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
import jwt
from models.doctor import DoctorLogin
from models.admin import AdminCredential
from models.patient_credential import CheckPatientCredential

router = APIRouter()

def serialize_user(user):
    d = user.model_dump(mode='json')
    d['_id'] = str(user.id)
    if 'id' in d: del d['id']
    return d

@router.post('/api/register')
async def register_doctor(body: Dict[str, Any] = Body(...)):
    try:
        user = DoctorLogin(**body)
        await user.insert()
        return JSONResponse(content={'status': 'ok'})
    except Exception as e:
        return JSONResponse(content={'status': 'error', 'error': 'Duplicate Email'})

@router.post('/api/login')
async def login_doctor(body: Dict[str, Any] = Body(...)):
    user = await DoctorLogin.find_one(DoctorLogin.email == body.get('email'), DoctorLogin.password == body.get('password'))
    if user:
        token = jwt.encode({'name': user.name, 'email': user.email}, 'secret123', algorithm='HS256')
        return JSONResponse(content={'status': 'ok', 'user': token, 'email': user.email, 'name': user.name, '_id': str(user.id)})
    return JSONResponse(content={'status': 'error', 'user': False})

@router.post('/api/Adminlogin')
async def login_admin(body: Dict[str, Any] = Body(...)):
    user = await AdminCredential.find_one(AdminCredential.email == body.get('email'), AdminCredential.password == body.get('password'))
    if user:
        token = jwt.encode({'name': user.name, 'email': user.email}, 'secret123', algorithm='HS256')
        return JSONResponse(content={'status': 'ok', 'user': token})
    return JSONResponse(content={'status': 'error', 'user': False})

@router.post('/api/Patientregister')
async def register_patient_cred(body: Dict[str, Any] = Body(...)):
    try:
        user = CheckPatientCredential(**body)
        await user.insert()
        return JSONResponse(content={'status': 'ok'})
    except Exception:
        return JSONResponse(content={'status': 'error', 'error': 'Email Already Exists'})

@router.post('/CheckCredlogin')
async def login_patient_cred(body: Dict[str, Any] = Body(...)):
    user = await CheckPatientCredential.find_one(CheckPatientCredential.email == body.get('email'), CheckPatientCredential.password == body.get('password'))
    if user:
        token = jwt.encode({'name': user.name, 'email': user.email}, 'secret123', algorithm='HS256')
        return JSONResponse(content={'status': 'ok', 'email': user.email, '_id': str(user.id), 'name': user.name})
    return JSONResponse(content={'status': 'error', 'user': False})
