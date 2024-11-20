from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EquipmentSchema import EquipmentSchema, EquipmentUpdateSchema
from services.EquipmentServices import EquipmentServices

router = APIRouter(prefix="/equipment", tags=["equipment"])

@router.get("/getAllEquipment")
def getAllEquipment(db: Session = Depends(connectDB.connectDB)):
    data = EquipmentServices(db).getAllEquipment()
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get All Equipment !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Equipment !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

def getEquipmentByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EquipmentServices(db).getEquipmentByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get Equipment With This ID !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Equipment By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

def createEquipment(Equipment: EquipmentSchema, db: Session = Depends(connectDB.connectDB)):
    data = EquipmentServices(db).createEquipment(Equipment)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Create Equipment !")
    responseConfig = {
        "data": data,
        "status": 201,
        "message": "Successfully Created Equipment !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_201_CREATED)
    return response

def updateEquipmentByID(id: int, Equipment: EquipmentUpdateSchema, db: Session = Depends(connectDB.connectDB)):
    data = EquipmentServices(db).updateEquipmentByID(id, Equipment)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Update Equipment !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Updated Equipment By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_202_ACCEPTED)
    return response

def deleteEquipmentByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EquipmentServices(db).deleteEquipmentByID(id)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Delete Equipment !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Deleted Equipment By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_202_ACCEPTED)
    return response