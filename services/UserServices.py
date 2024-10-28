from sqlalchemy.orm import Session
from db.models.user import User
from schemas.UserSchema import UserSchema

class UserServices:
    def __init__(self, db: Session):
        self.db = db
    
    def getAllUsers(self):
        response = {}
        data = self.db.query(User).all()
        if not data:
            response["message"] = "No users found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def createUser(self, user: UserSchema):
        response = {}
        newUser = User(name=user.name, email=user.email, password=user.password)
        self.db.add(newUser)
        if not newUser:
            response["message"] = "Error creating user"
            response["status"] = 404
            return response
        self.db.commit()
        response["data"] = newUser
        response["status"] = 200
        response["message"] = "Success"
        return response

