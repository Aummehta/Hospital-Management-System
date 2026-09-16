from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from typing import Dict, Any
from models.leave import ApplyLeave

router = APIRouter()

def serialize_leave(leave) -> dict:
    d = leave.model_dump(mode='json')
    d['_id'] = str(leave.id)
    if 'id' in d: del d['id']
    return d

@router.post('/AddLeave')
async def add_leave(body: Dict[str, Any] = Body(...)):
    leave = ApplyLeave(**body)
    await leave.insert()
    return JSONResponse(status_code=201, content={'status': 'Success', 'data': {'leave': serialize_leave(leave)}})

@router.get('/LeaveApp')
async def leave_app():
    try:
        leaves = await ApplyLeave.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'LeaveApplication': [serialize_leave(l) for l in leaves]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.get('/GetLeave')
async def get_leave():
    try:
        leaves = await ApplyLeave.find_all().to_list()
        return JSONResponse(status_code=200, content={'status': 'ok', 'data': {'GetLeave': [serialize_leave(l) for l in leaves]}})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'err', 'message': str(e)})

@router.post('/UpdateLeave')
async def update_leave(body: Dict[str, Any] = Body(...)):
    leave = await ApplyLeave.find_one(ApplyLeave.email == body.get('email'))
    if leave:
        await leave.set({'approve': body.get('status')})
        return JSONResponse(content={'status': 'ok'})
    return JSONResponse(content={'status': 'error'})
