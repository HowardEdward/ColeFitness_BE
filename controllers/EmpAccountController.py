from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EmpAccountSchema import EmpAccountSchema, EmpAccountPasswordUpdateSchema
from services.EmpAccountServices import EmpAccountServices

router = APIRouter(prefix="/employee", tags=["employee_account"])

@router.get("/getAllEmpAccount")
def getAllEmpAccount(db: Session = Depends(connectDB.connectDB)):
    data = EmpAccountServices(db).getAllEmpAccount()
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get All Employee Account !")
    reponseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Employees !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_200_OK)
    return response

@router.get("/getAccountByEmpID/{id}")
def getAccountByEmpID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EmpAccountServices(db).getAccountByEmpID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Unable To Get Account With This Employee ID !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Employee's Account !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_201_CREATED)
    return response

@router.post("/createEmpAccount")
def createEmpAccount(account: EmpAccountSchema, db: Session = Depends(connectDB.connectDB)):
    data = EmpAccountServices(db).createEmpAccount(account)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Create Employee Account !")
    responseConfig = {
        "data": data,
        "status": 201,
        "message": "Successfully Created Employee Account !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_201_CREATED)
    return response

@router.put("/updateEmpAccountPasswordByID/{id}")
def updateEmpAccountPasswordByID(id: int, password: EmpAccountPasswordUpdateSchema, db: Session = Depends(connectDB.connectDB)):
    data = EmpAccountServices(db).updateEmpAccountPasswordByID(id, password)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Update Employee Account !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Updated Employee Account !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.delete("/deleteEmpAccountByID/{id}")
def deleteEmpAccountByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EmpAccountServices(db).deleteEmpAccountByID(id)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Delete Employee Account !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Deleted Employee Account !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

