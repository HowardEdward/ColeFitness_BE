from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.EmpContactSchema import EmpContactSchema
from services.EmpContactServices import EmpContactServices

router = APIRouter(prefix="/emp_contact", tags=["emp_contact"])

@router.get("/getAllContact")
def getAllContact(db: Session = Depends(connectDB.connectDB)):
    response = EmpContactServices(db).getAllContact()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

