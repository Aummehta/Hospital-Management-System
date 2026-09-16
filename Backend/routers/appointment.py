from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.appointment import Appointment

router = APIRouter()

def serialize_appointment(app) -> dict:
    d = app.model_dump(mode='json')
    d['_id'] = str(app.id)
    if 'id' in d: del d['id']
    return d

@router.post('/SendAppointment')
async def send_appointment(body: Dict[str, Any] = Body(...)):
    app_data = Appointment(**body)
    await app_data.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'AppointmentData': serialize_appointment(app_data)}})

@router.get('/AppointmentData')
async def appointment_data():
    try:
        appointments = await Appointment.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllAppointmetnData': [serialize_appointment(a) for a in appointments]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/UpdateAppoin')
async def update_appoin(body: Dict[str, Any] = Body(...)):
    user = await Appointment.get(body.get('id'))
    if user:
        await user.set({'status': body.get('status')})
        return JSONResponse(content={'status': 'ok'})
    return JSONResponse(content='No U')
