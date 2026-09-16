from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.doctor import AddDoctor

router = APIRouter()

def serialize_doctor(doctor) -> dict:
    d = doctor.model_dump(mode='json')
    d['_id'] = str(doctor.id)
    if 'id' in d: del d['id']
    return d

@router.get('/AllDoctor')
async def get_all_doctor():
    try:
        doctors = await AddDoctor.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllDoctorData': [serialize_doctor(d) for d in doctors]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/AddDoctor')
async def add_doctor(body: Dict[str, Any] = Body(...)):
    email = body.get('email')
    user = await AddDoctor.find_one(AddDoctor.email == email)
    if user:
        return JSONResponse(status_code=205, content={'status': 'err', 'message': 'Doctor Already exists'})
    doctor = AddDoctor(**body)
    await doctor.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'Doctordata': serialize_doctor(doctor)}})

@router.delete('/DeleteDoctor/{id}')
async def delete_doctor(id: str):
    try:
        doctor = await AddDoctor.get(id)
        if doctor: await doctor.delete()
        return JSONResponse(status_code=204, content={'status': 'ok', 'data': 'Doctor Deleted Successfully'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})

@router.put('/UpdateStatus')
async def update_status(body: Dict[str, Any] = Body(...)):
    user_email = body.get('email', '')
    if user_email.startswith('"') and user_email.endswith('"'):
        user_email = user_email[1:-1]
    
    doctor = await AddDoctor.find_one(AddDoctor.email == user_email)
    if doctor:
        await doctor.set({'status': body.get('status')})
        return JSONResponse(content={'status': 'ok'})
    return JSONResponse(status_code=422, content='Not found')

@router.get('/GetInfoDoctor/{id}')
async def get_info_doctor(id: str):
    try:
        user = await AddDoctor.get(id)
        if user: return JSONResponse(status_code=201, content=serialize_doctor(user))
        return JSONResponse(status_code=201, content=None)
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))

@router.patch('/updateDoctor/{id}')
async def update_doctor(id: str, body: Dict[str, Any] = Body(...)):
    try:
        user = await AddDoctor.get(id)
        if user:
            await user.set(body)
            updated_user = await AddDoctor.get(id)
            return JSONResponse(status_code=201, content=serialize_doctor(updated_user))
        return JSONResponse(status_code=422, content='User not found')
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))
