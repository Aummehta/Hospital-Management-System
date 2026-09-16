from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.employee import AddEmployee

router = APIRouter()

def serialize_employee(employee) -> dict:
    d = employee.model_dump(mode='json')
    d['_id'] = str(employee.id)
    if 'id' in d: del d['id']
    return d

@router.delete('/DeleteEmployee/{id}')
async def delete_employee(id: str):
    try:
        employee = await AddEmployee.get(id)
        if employee: await employee.delete()
        return JSONResponse(status_code=204, content={'status': 'ok', 'data': 'Patient Deleted Successfully'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})

@router.post('/AddEmployee')
async def add_employee(body: Dict[str, Any] = Body(...)):
    employee = AddEmployee(**body)
    await employee.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'EmployeeData': serialize_employee(employee)}})

@router.get('/AllEmployee')
async def all_employee():
    try:
        employees = await AddEmployee.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'AllEmployeeData': [serialize_employee(e) for e in employees]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.get('/GetInfoEmployee/{id}')
async def get_info_employee(id: str):
    try:
        user = await AddEmployee.get(id)
        if user: return JSONResponse(status_code=201, content=serialize_employee(user))
        return JSONResponse(status_code=201, content=None)
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))

@router.patch('/updateEmployee/{id}')
async def update_employee(id: str, body: Dict[str, Any] = Body(...)):
    try:
        user = await AddEmployee.get(id)
        if user:
            await user.set(body)
            updated_user = await AddEmployee.get(id)
            return JSONResponse(status_code=201, content=serialize_employee(updated_user))
        return JSONResponse(status_code=422, content='User not found')
    except Exception as e:
        return JSONResponse(status_code=422, content=str(e))
