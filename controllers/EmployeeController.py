from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EmployeeSchema import EmployeeSchema
from services.EmployeeServices import EmployeeServices

router = APIRouter(prefix="/employee", tags=["employee"])

@router.get("/getAllEmployee")
def getAllEmployees(db: Session = Depends(connectDB.connectDB)):
    response = EmployeeServices(db).getAllEmployees()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.get("/getEmployeeByID/{id}")
def getEmployeeByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = EmployeeServices(db).getEmployeeByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.post("/createEmployee")
def createEmployee(Employee: EmployeeSchema, db: Session = Depends(connectDB.connectDB)):
    print(Employee)
    response = EmployeeServices(db).createEmployee(Employee)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.put("/updateEmployeeByID/{id}")
def updateEmployee(id: int, Employee: EmployeeSchema, db: Session = Depends(connectDB.connectDB)):
    response = EmployeeServices(db).updateEmployeeByID(id, Employee)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.delete("/deleteEmployeeByID/{id}")
def deleteEmployeeByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = EmployeeServices(db).deleteEmployeeByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response