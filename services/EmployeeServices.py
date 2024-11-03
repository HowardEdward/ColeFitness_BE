from sqlalchemy.orm import Session
from db.models.Employee import Employee
from schemas.EmployeeSchema import EmployeeSchema

class EmployeeServices:
    def __init__(self, db: Session):
        self.db = db
    
    def createEmployee(self, Employee: EmployeeSchema) -> dict:
        response = {}
        newEmployee = Employee(**dict(Employee))
        self.db.add(newEmployee)
        if not newEmployee:
            response["message"] = "Error creating Employee"
            response["status"] = 404
            return response
        self.db.commit()
        response["data"] = newEmployee
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def getAllEmployees(self) -> dict:
        response = {}
        data = self.db.query(Employee).all()
        if not data:
            response["message"] = "No Employees found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def getEmployeeByID(self, id: int) -> dict:
        response = {}
        data = self.db.query(Employee).filter(Employee.EmployeeID == id).first()
        if not data:
            response["message"] = "Employee not found"
            response["status"] = 404
            return response
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def updateEmployeeByID(self, id: int, Employee: EmployeeSchema) -> dict:
        response = {}
        data = self.db.query(Employee).filter(Employee.EmployeeID == id).first()
        if not data:
            response["message"] = "Employee not found"
            response["status"] = 404
            return response
        data.FirstName = Employee.FirstName
        data.MiddleName = Employee.MiddleName
        data.LastName = Employee.LastName
        data.DOB = Employee.DOB
        data.RoleKey = Employee.RoleKey
        data.ContactID = Employee.ContactID
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    
    def deleteEmployeeByID(self, id: int) -> dict:
        response = {}
        data = self.db.query(Employee).filter(Employee.EmployeeID == id).first()
        if not data:
            response["message"] = "Employee not found"
            response["status"] = 404
            return response
        self.db.delete(data)
        self.db.commit()
        response["data"] = data
        response["status"] = 200
        response["message"] = "Success"
        return response
    