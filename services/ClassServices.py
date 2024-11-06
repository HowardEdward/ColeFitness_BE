from sqlalchemy.orm import Session
from db.models.Class import Class
from schemas.ClassSchema import ClassSchemas

class ClassServices:
    def __init__(self, db: Session):
        self.db = db

    def getAllClass(self):
        response = {}
        data = self.db.query(Class).all()
        if not data:
            response["message"] = "No class found !"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response