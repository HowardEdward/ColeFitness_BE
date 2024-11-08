from sqlalchemy.orm import Session
from db.models.Role import Role
from schemas.RoleSchema import RoleSchema

class RoleServices:
    def __init__(self, db: Session):
        self.db = db

    def getAllRole(self):
        response = {}
        data = self.db.query(Role).all()
        if not data:
            response["message"] = "No role found !"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
        