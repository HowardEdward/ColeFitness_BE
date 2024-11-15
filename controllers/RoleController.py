from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.RoleSchema import RoleSchema
from services.RoleServices import RoleServices

router = APIRouter(prefix="/role", tags=["role"])


@router.get("/getAllRole")
def getAllRole(db: Session = Depends(connectDB.connectDB)):
    data = RoleServices(db).getAllRole()
    if not data:
        raise HTTPException(status_code=404, detail="No Role Found !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Role !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response