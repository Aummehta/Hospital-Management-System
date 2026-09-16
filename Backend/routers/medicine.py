from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.medicine import AddMedicine

router = APIRouter()

def serialize_medicine(medicine) -> dict:
    d = medicine.model_dump(mode='json')
    d['_id'] = str(medicine.id)
    if 'id' in d: del d['id']
    return d

@router.get('/AllMedicine')
async def get_all_medicine():
    try:
        medicines = await AddMedicine.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllMedicine': [serialize_medicine(m) for m in medicines]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/AddMedicineData')
async def add_medicine_data(body: Dict[str, Any] = Body(...)):
    name = body.get('name')
    user = await AddMedicine.find_one(AddMedicine.name == name)
    if user:
        return JSONResponse(status_code=205, content={'status': 'err', 'message': 'Medicine Already exists'})
    medicine = AddMedicine(**body)
    await medicine.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'MedicineData': serialize_medicine(medicine)}})

@router.delete('/DeleteMedicine/{id}')
async def delete_medicine(id: str):
    try:
        medicine = await AddMedicine.get(id)
        if medicine: await medicine.delete()
        return JSONResponse(status_code=204, content={'status': 'ok', 'data': 'Medicine Deleted Successfully'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})

@router.get('/AllMedicineData')
async def all_medicine_data():
    try:
        medicines = await AddMedicine.find_all().to_list()
        medicines_list = [{'name': m.name, 'category': m.category} for m in medicines]
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllMedicineData': medicines_list}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})
