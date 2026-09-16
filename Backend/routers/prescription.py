from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.prescription import Prescription

router = APIRouter()

def serialize_prescription(pres) -> dict:
    d = pres.model_dump(mode='json')
    d['_id'] = str(pres.id)
    if 'id' in d: del d['id']
    return d

@router.get('/PrescriptionData')
async def prescription_data():
    try:
        prescriptions = await Prescription.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllPrescriptionData': [serialize_prescription(p) for p in prescriptions]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/SendPrescription')
async def send_prescription(body: Dict[str, Any] = Body(...)):
    try:
        pres_data = Prescription(**body)
        await pres_data.insert()
        return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'PrescriptionDataa': serialize_prescription(pres_data)}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})
