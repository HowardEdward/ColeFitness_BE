from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class EmpContact(Base):
    __tablename__ = "EMP_CONTACT"
    ContactID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EmployeeID = mapped_column(Integer, nullable=True)
    PhoneNumber = Column(String)
    EmailAddress = Column(String)
    Address = Column(String)
    ContactType = Column(VARCHAR(5))

    EmployeeRelationship = relationship("Employee", back_populates="RoleRelationship")