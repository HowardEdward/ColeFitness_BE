from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from schemas.MembershipSchema import MembershipSchema, MembershipUpdateSchema
from services.MembershipServices import MembershipServices

router = APIRouter(prefix="/membership", tags=["membership"])

@router.get("/getAllMembership")
def getAllMembership(db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MembershipServices(db).getAllMembership()
    if not data:
        raise HTTPException(status_code=404, detail="No Membership Found !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Membership !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.get("/getMembershipByID/{id}")
def getMembershipByID(id: int, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MembershipServices(db).getMembershipByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Not Found Membership With Provided ID !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Membership By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.post("/createMembership")
def createMembership(membership: MembershipSchema, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    response = MembershipServices(db).createMembership(membership)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.put("/updateMembershipByID/{id}")
def updateMembershipByID(id: int, membership: MembershipUpdateSchema, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MembershipServices(db).updateMembershipByID(id, membership)
    if not data:
        raise HTTPException(status_code=404, detail="Not Found Membership With Given ID To Update !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Update Membership By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response

@router.delete("/deleteMembershipByID/{id}")
def deleteMembershipByID(id: int, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MembershipServices(db).deleteMembershipByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Not Found Membership With Given ID To Delete !")
    responseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Deleted Membership By ID !"
    }
    response = JSONResponse(content=jsonable_encoder(responseConfig), status_code=status.HTTP_200_OK)
    return response