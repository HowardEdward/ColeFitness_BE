from sqlalchemy.orm import Session
from db.models.Branch import Branch
from schemas.BranchSchema import BranchSchema

class BranchServices:
    def __init__(self, db: Session):
        self.db = db

    def createBranch(self, branch: BranchSchema):
        response = {}
        newBranch = Branch(**dict(branch))
        self.db.add(newBranch)
        if not newBranch:
            response["message"] = "Error creating branch"
            response["status"] = 404
            return response
        self.db.commit()
        response["data"] = newBranch
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def getAllBranch(self):
        response = {}
        data = self.db.query(Branch).all()
        if not data:
            response["message"] = "No branch found !"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response

    def getBranchByID(self, id: int):
        response = {}
        data = self.db.query(Branch).filter(Branch.BranchID == id).first()
        if not data:
            response["message"] = "Branch not found !"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def updateBranchByID(self, id: int, branch: BranchSchema):
        response = {}
        data = self.db.query(Branch).filter(Branch.BranchID == id).first()
        if not data:
            response["message"] = "Branch not found !"
            response["status"] = 404
            return response
        data.BranchName = branch.BranchName
        data.BranchPhoneNumber = branch.BranchPhoneNumber
        data.BranchEmailAddress = branch.BranchEmailAddress
        data.BranchAddress = branch.BranchAddress
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def deleteBranchByID(self, id: int):
        response = {}
        data = self.db.query(Branch).filter(Branch.BranchID == id).first()
        if not data:
            response["message"] = "Branch not found !"
            response["status"] = 404
            return response
        self.db.delete(data)
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response