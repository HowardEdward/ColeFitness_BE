from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.UserSchema import UserSchema
from db import connectDB
from services.UserServices import UserServices

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/getAllUsers")
async def getAllUsers(db: Session = Depends(connectDB.connectDB)):
    response = UserServices(db).getAllUsers()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.post("/createUser")
async def createUser(user: UserSchema, db: Session = Depends(connectDB.connectDB)):
    response = UserServices(db).createUser(user)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response