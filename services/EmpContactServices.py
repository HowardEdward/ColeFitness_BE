from sqlalchemy.orm import Session
from sqlalchemy import func
from db.connectDB import logger
from db.models.EmpContact import EmpContact
from schemas.EmpContactSchema import EmpContactSchema, EmpContactUpdateSchema

class EmpContactServices:
    def __init__(self, db: Session):
        self.db = db
    
    def getAllEmpContact(self):
        try:
            allContacts = self.db.query(EmpContact).all()
            if not allContacts:
                logger.error("getAllContact: No Contact Found !")
                return
            logger.info("getAllContact: Successfully Get All Contact !")
            return allContacts
        except Exception as e:
            logger.error(f"getAllContact: {e} !")
            return
    
    def getEmpContactByID(self, id: int):
        try:
            contactByID = self.db.query(EmpContact).filter(EmpContact.EmpContactID == id).first()
            if not contactByID:
                logger.error("getContactByID: No Contact Found !")
                return
            logger.info("getContactByID: Successfully Get Contact By ID !")
            return contactByID
        except Exception as ex:
            logger.error(f"getContactByID: {ex} !")
            return
    
    def createEmpContact(self, contact: EmpContactSchema):
        try:
            newContact = EmpContact(**dict(contact))
            if not newContact:
                logger.error("createContact: Error During Creating New Contact !")
                return
            self.db.add(newContact)
            self.db.commit()
            logger.info("createContact: Successfully Creat New Contact !")
            return newContact
        except Exception as ex:
            logger.error(f"createContact: {ex} !")
            return

    def updateEmpContactByID(self, id: int, contact: EmpContactUpdateSchema):
        try:
            contactByID = self.db.query(EmpContact).filter(EmpContact.EmpContactID == id).first()
            if not contactByID:
                logger.error("updateContactByID: No Contact Found !")
                return
            contactByID = contactByID.__dict__
            updateContact = {}
            for attribute in contact:
                columnName = attribute[0]
                if attribute[1] == None:
                    updateContact[columnName] = contactByID[columnName]
                else:
                    updateContact[columnName] = attribute[1]
            self.db.query(EmpContact).filter(EmpContact.EmpContactID == id).update(updateContact)
            self.db.commit()
            logger.info("updateContactByID: Successfully Update Contact !")
            return contactByID
        except Exception as ex:
            logger.error(f"updateContactByID: {ex} !")
            return

    def deleteEmpContactByID(self, id: int):
        try:
            contactByID = self.db.query(EmpContact).filter(EmpContact.EmpContactID == id).first()
            if not contactByID:
                logger.error("deleteContactByID: No Contact Found !")
                return
            self.db.delete(contactByID)
            self.db.commit()
            logger.info("deleteContactByID: Successfully Delete Contact !")
            return contactByID
        except Exception as ex:
            logger.error(f"deleteContactByID: {ex} !")
            return