from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.EmpAccountSchema import AccountSchema, PasswordSchema
from db import connectDB
from services.EmpAccountServices import AccountServices

router = APIRouter(prefix="/account", tags=["account"])

@router.get("/getAllAccount")
async def getAllAccount(db: Session = Depends(connectDB.connectDB)):
    response = AccountServices(db).getAllAccounts()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.get("/getAccountByID/{id}")
async def getAccountByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = AccountServices(db).getAccountByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.post("/createAccount")
async def createAccount(account: AccountSchema, db: Session = Depends(connectDB.connectDB)):
    response = AccountServices(db).createAccount(account)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

# @router.put("/updateAccountByID/{id}")
# async def updateUser(id: int, account: AccountSchema, db: Session = Depends(connectDB.connectDB)):
#     response = AccountServices(db).updateAccountByID(id, account)
#     if response["status"] == 404:
#         raise HTTPException(status_code=404, detail=response["message"])
#     return response

@router.delete("/deleteAccountByID/{id}")
async def deleteUserByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = AccountServices(db).deleteAccountByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.put("/updatePasswordByID/{id}")
async def updatePasswordByID(id: int, password: PasswordSchema, db: Session = Depends(connectDB.connectDB)):
    response = AccountServices(db).updatePasswordByID(id, password)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response
