from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EmpAccountSchema import EmpAccountSchema, EmpAccountPasswordSchema
from services.EmpAccountServices import EmpAccountServices

router = APIRouter(prefix="/account", tags=["account"])

@router.get("/getAllAccount")
def getAllAccount(db: Session = Depends(connectDB.connectDB)):
    response = EmpAccountServices(db).getAllAccounts()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.get("/getAccountByID/{id}")
def getAccountByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = EmpAccountServices(db).getAccountByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.post("/createAccount")
def createAccount(account: EmpAccountSchema, db: Session = Depends(connectDB.connectDB)):
    response = EmpAccountServices(db).createAccount(account)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

# @router.put("/updateAccountByID/{id}")
# def updateUser(id: int, account: EmpAccountSchema, db: Session = Depends(connectDB.connectDB)):
#     response = EmpAccountServices(db).updateAccountByID(id, account)
#     if response["status"] == 404:
#         raise HTTPException(status_code=404, detail=response["message"])
#     return response

@router.delete("/deleteAccountByID/{id}")
def deleteUserByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = EmpAccountServices(db).deleteAccountByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.put("/updatePasswordByID/{id}")
def updatePasswordByID(id: int, password: EmpAccountPasswordSchema, db: Session = Depends(connectDB.connectDB)):
    response = EmpAccountServices(db).updatePasswordByID(id, password)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response
