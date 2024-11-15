from sqlalchemy.orm import Session
from sqlalchemy import func
from db.connectDB import logger
from db.models.Role import Role
from schemas.RoleSchema import RoleSchema

class RoleServices:
    def __init__(self, db: Session):
        self.db = db

    def getAllRole(self):
        allRoles = self.db.query(Role).all()
        if not allRoles:
            logger.error("getAllRole: No Role Found !")
            return
        logger.info("getAllRole: Successfully Get All Role !")
        self.db.close()
        return allRoles
        