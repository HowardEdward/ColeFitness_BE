from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.ScheduleSchema import ScheduleSchema, ScheduleUpdateSchema
from services.ScheduleServices import ScheduleServices

router = APIRouter(prefix="/schedule", tags=["schedule"])

@router.get("/getAllSchedule")
def getAllSchedule(db: Session = Depends(connectDB.connectDB)):
    data = ScheduleServices(db).getAllSchedule()
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get All Schedule !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Schedule !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.get("/getScheduleByID/{id}")
def getScheduleByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = ScheduleServices(db).getScheduleByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get Schedule By Id !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Schedule By Id !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.post("/createSchedule")
def createSchedule(data: ScheduleSchema, db: Session = Depends(connectDB.connectDB)):
    data = ScheduleServices(db).createSchedule(data)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Create Schedule !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Create Schedule !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.put("/updateScheduleByID/{id}")
def updateScheduleByID(id: int, data: ScheduleUpdateSchema, db: Session = Depends(connectDB.connectDB)):
    data = ScheduleServices(db).updateScheduleByID(id, data)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Update Schedule By Id !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Update Schedule By Id !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.delete("/deleteScheduleByID/{id}")
def deleteScheduleByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = ScheduleServices(db).deleteScheduleByID(id)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Delete Schedule By Id !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Delete Schedule By Id !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response