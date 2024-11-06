from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.ClassSchema import ClassSchema
from services.ClassServices import ClassServices

router = APIRouter(prefix="/class", tags=["class"])


@router.get("/getAllClass")
def getAllClass(db: Session = Depends(connectDB.connectDB)):
    response = ClassServices(db).getAllClass()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response