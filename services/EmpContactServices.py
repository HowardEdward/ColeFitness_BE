from sqlalchemy.orm import Session
from db.models.EmpContact import EmpContact
from schemas.EmpContactSchema import EmpContactSchema


class EmpContactServices:
    def __init__(self, db: Session):
        self.db = db
    
    def getAllContact(self):
        response = {}
        data = self.db.query(EmpContact).all()
        if not data:
            response["message"] = "No contact found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
        