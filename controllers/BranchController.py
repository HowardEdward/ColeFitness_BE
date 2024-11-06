from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import connectDB
from schemas.BranchSchema import BranchSchema
from services.BranchServices import BranchServices

router = APIRouter(prefix="/branch", tags=["branch"])


@router.post("/createBranch")
def createBranch(branch: BranchSchema, db: Session = Depends(connectDB.connectDB)):
    response = BranchServices(db).createBranch(branch)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.get("/getAllBranch")
def getAllBranch(db: Session = Depends(connectDB.connectDB)):
    response = BranchServices(db).getAllBranch()
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.get("/getBranchByID/{id}")
def getBranchByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = BranchServices(db).getBranchByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.put("/updateBranchByID/{id}")
def updateBranch(id: int, branch: BranchSchema, db: Session = Depends(connectDB.connectDB)):
    response = BranchServices(db).updateBranchByID(id, branch)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response

@router.delete("/deleteBranchByID/{id}")
def deleteBranchByID(id: int, db: Session = Depends(connectDB.connectDB)):
    response = BranchServices(db).deleteBranchByID(id)
    if response["status"] == 404:
        raise HTTPException(status_code=404, detail=response["message"])
    return response