from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import connectDB
from services.MemberServices import MemberServices
from schemas.MemberSchema import MemberSchema, MemberUpdateSchema

router = APIRouter(prefix="/member", tags=["member"])

@router.get("/getAllMember")
def getAllMember(db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MemberServices(db).getAllMember()
    if not data:
        raise HTTPException(status_code=404, detail="No Member Found !")
    reponseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get All Member !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_200_OK)
    return response

@router.get("/getMemberByID/{id}")
def getMemberByID(id: int, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MemberServices(db).getMemberByID(id)
    if not data:
        raise HTTPException(status_code=404, detail="Member Not Found With This ID!")
    reponseConfig = {
        "data": data,
        "status": 200,
        "message": "Successfully Get Member !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_200_OK)
    return response

@router.post("/createMember")
def createMember(member: MemberSchema, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MemberServices(db).createMember(member)
    if not data:
        raise HTTPException(status_code=405, detail="Unable To Creat New Member !")
    reponseConfig = {
        "data": data,
        "status": 201,
        "message": "Successfully Creat New Member !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_201_CREATED)
    return response

@router.put("/updateMemberByID/{id}")
def updateMemberByID(id: int, member: MemberUpdateSchema, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MemberServices(db).updateMemberByID(id, member)
    if not data:
        raise HTTPException(status_code=405, detail="Not Found Member To Update !")
    reponseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Update Member !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_202_ACCEPTED)
    return response

@router.delete("/deleteMemberByID/{id}")
def deleteMemberByID(id: int, db: Session = Depends(connectDB.connectDB)) -> JSONResponse:
    data = MemberServices(db).deleteMemberByID(id)
    if not data:
        raise HTTPException(status_code=405, detail="Not Found Member To Delete !")
    reponseConfig = {
        "data": data,
        "status": 202,
        "message": "Successfully Delete Member !"
    }
    response = JSONResponse(content=jsonable_encoder(reponseConfig), status_code= status.HTTP_200_OK)
    return response