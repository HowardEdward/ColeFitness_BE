from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.RoleSchema import RoleSchema
from services.RoleServices import RoleServices

router = APIRouter(prefix="/role", tags=["role"])


@router.get("/getAllRole")
def getAllRole(db: Session = Depends(connectDB.connectDB)):
    response = RoleServices(db).getAllRole()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response