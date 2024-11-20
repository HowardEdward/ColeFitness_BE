from sqlalchemy.orm import Session
from sqlalchemy import func
from db.connectDB import logger
from db.models.EmpAccount import EmpAccount
from db.models.MemAccount import MemAccount
from db.models.Employee import Employee
from db.models.Member import Member
from schemas.ColeFitnessSchema import ColeFitnessLoginSchema
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

class ColeFitnessServices:
    def __init__(self, db: Session):
        self.db = db
    
    def login(self, type, account: ColeFitnessLoginSchema) -> (EmpAccount | MemAccount | None):
        try:
            if type == "Employee":
                data = self.db.query(EmpAccount).filter(EmpAccount.UserName == account.UserName).first()
                if not data:
                    logger.error("login: No Account Found !")
                    return
                check_password = check_password_hash(data.Password, account.Password)
                if not check_password:
                    logger.error("login: Invalid Password !")
                    return
                logger.info("login: Successfully Login !")
                employee = self.db.query(Employee).filter(Employee.EmployeeID == data.EmployeeID).first()
                if not employee:
                    logger.error("login: No Employee Found !")
                    return
                return employee
            elif type == "Member":
                data = self.db.query(MemAccount).filter(MemAccount.UserName == account.UserName).first()
                if not data:
                    logger.error("login: No Account Found !")
                    return
                check_password = check_password_hash(data.Password, account.Password)
                if not check_password:
                    logger.error("login: Invalid Password !")
                    return
                logger.info("login: Successfully Login !")
                member = self.db.query(Member).filter(Member.MemberID == data.MemberID).first()
                if not member:
                    logger.error("login: No Member Found !")
                    return
                return member
            else:
                logger.error("login: Invalid Type !")
                return
        except Exception as ex:
            logger.error(f"login: {ex} !")
            return