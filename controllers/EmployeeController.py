from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EmployeeSchema import EmployeeSchema, EmployeeUpdateSchema
from services.EmployeeServices import EmployeeServices

router = APIRouter(prefix="/employee", tags=["employee"])

@router.get("/getAllEmployee")
def getAllEmployee(db: Session = Depends(connectDB.connectDB)):
    data = EmployeeServices(db).getAllEmployee()
    if not data:
        raise HTTPException(status_code=404, detail="No Employees Found !")
    reponseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Employees !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_200_OK)
    return response

@router.get("/getEmployeeByID/{id}")
def getEmployeeByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EmployeeServices(db).getEmployeeByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Employee Not Found !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Employee By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.post("/createEmployee")
async def createEmployee(Employee: EmployeeSchema, db: Session = Depends(connectDB.connectDB)):
    data = EmployeeServices(db).createEmployee(Employee)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Creat New Employee !")
    responseConfig = {
        "data": data,
        "status": 201,
        "message": "Successfully Created Employee !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_201_CREATED)
    return response

@router.put("/updateEmployeeByID/{id}")
def updateEmployee(id: int, Employee: EmployeeUpdateSchema, db: Session = Depends(connectDB.connectDB)):
    data = EmployeeServices(db).updateEmployeeByID(id, Employee)
    if not data:
        raise HTTPException(status_code=405, detail="Not Found Employee To Update !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Updated Employee !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_202_ACCEPTED)
    return response

@router.delete("/deleteEmployeeByID/{id}")
def deleteEmployeeByID(id: int, db: Session = Depends(connectDB.connectDB)):
    data = EmployeeServices(db).deleteEmployeeByID(id)
    if not data:
        raise HTTPException(status_code=405, detail="Not Found Employee To Delete !")
    responseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Deleted Employee !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_202_ACCEPTED)
    return response