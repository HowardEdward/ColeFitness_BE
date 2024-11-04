from sqlalchemy.orm import Session
from db.models.EmpAccount import Account
from schemas.EmpAccountSchema import AccountSchema
from werkzeug.security import generate_password_hash, check_password_hash

class AccountServices:
    def __init__(self, db: Session):
        self.db = db

    def createAccount(self, account: AccountSchema):
        response = {}
        if account.Password:
            password_hash = self.hashPassword(account.Password)
        check_password = self.checkPassword(account.Password, password_hash)
        if not check_password:
            response["message"] = "Create account failed, Hash password error"
            response["status"] = 404
            return response
        account.Password = password_hash
        newAccount = Account(**dict(account))
        self.db.add(newAccount)
        if not newAccount:
            response["message"] = "Error creating account"
            response["status"] = 404
            return response
        self.db.commit()
        response["data"] = newAccount
        response["status"] = 200
        response["message"] = "Success"
        return response

    def getAllAccounts(self):
        response = {}
        data = self.db.query(Account).all()
        if not data:
            response["message"] = "No accounts found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response

    def getAccountByID(self, id: int):
        response = {}
        data = self.db.query(Account).filter(Account.AccountID == id).first()
        if not data:
            response["message"] = "Account not found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response

    def deleteAccountByID(self, id: int):
        response = {}
        data = self.db.query(Account).filter(Account.AccountID == id).first()
        if not data:
            response["message"] = "Account not found"
            response["status"] = 404
            return response
        self.db.delete(data)
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response

    # def updateAccountByID(self, id: int, account: AccountSchema):
    #     response = {}
    #     data = self.db.query(Account).filter(Account.AccountID == id).first()
    #     if not data:
    #         response["message"] = "Account not found"
    #         response["status"] = 404
    #         return response
    #     data.UserName = account.UserName
    #     data.Password = account.Password
    #     data.RoleKey = account.RoleKey
    #     data.Status = account.Status
    #     self.db.commit()
    #     response["data"] = data
    #     response["status"] = 200
    #     response["message"] = "Success"
    #     return response

    def updatePasswordByID(self, id: int, password: str):
        response = {}
        data = self.db.query(Account).filter(Account.AccountID == id).first()
        if not data:
            response["message"] = "Account not found"
            response["status"] = 404
            return response
        if not password:
            response["message"] = "Password not found"
            response["status"] = 404
            return response
        new_password = self.hashPassword(password)
        check_password = self.checkPassword(new_password, data.Password)
        if not check_password:
            response["message"] = "Update password failed, Hash password error"
            response["status"] = 404
            return response
        data.Password = new_password
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    @staticmethod
    def hashPassword(password: str) -> str:
        return generate_password_hash(password)
    
    @staticmethod
    def checkPassword(password: str, hashedPassword: str) -> bool:
        return check_password_hash(hashedPassword, password)