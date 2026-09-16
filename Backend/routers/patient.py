from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.patient import AddPatient

router = APIRouter()

def serialize_patient(patient) -> dict:
    d = patient.model_dump(mode='json')
    d['_id'] = str(patient.id)
    if 'id' in d: del d['id']
    return d

@router.get('/AllPatient')
async def get_all_patients():
    try:
        patients = await AddPatient.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllPatientData': [serialize_patient(p) for p in patients]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/addPatient')
async def add_patient(body: Dict[str, Any] = Body(...)):
    email = body.get('email')
    user = await AddPatient.find_one(AddPatient.email == email)
    if user:
        return JSONResponse(status_code=205, content={'status': 'err', 'message': 'Email Already exists'})
    patientdata = AddPatient(**body)
    await patientdata.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'patientdata': serialize_patient(patientdata)}})

@router.delete('/DeletePatient/{id}')
async def delete_patient(id: str):
    try:
        patient = await AddPatient.get(id)
        if patient: await patient.delete()
        return JSONResponse(status_code=204, content={'status': 'ok', 'data': 'Patient Deleted Successfully'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})

@router.get('/AllPatientNameEmail')
async def all_patient_name_email():
    try:
        patients = await AddPatient.find_all().to_list()
        patients_list = [{'fname': p.fname, 'email': p.email} for p in patients]
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllPatientNameEmail': patients_list}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.get('/GetInfo/{id}')
async def get_info(id: str):
    try:
        user = await AddPatient.get(id)
        if user: return JSONResponse(status_code=201, content=serialize_patient(user))
        return JSONResponse(status_code=201, content=None)
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))

@router.patch('/updateuser/{id}')
async def update_user(id: str, body: Dict[str, Any] = Body(...)):
    try:
        user = await AddPatient.get(id)
        if user:
            await user.set(body)
            updated_user = await AddPatient.get(id)
            return JSONResponse(status_code=201, content=serialize_patient(updated_user))
        return JSONResponse(status_code=422, content='User not found')
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))
