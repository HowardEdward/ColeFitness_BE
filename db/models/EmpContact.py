from sqlalchemy import Column, Integer, String, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Contact(Base):
    __tablename__ = "EMP_CONTACT"
    ContactID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EmployeeID = mapped_column(Integer, ForeignKey("EMPLOYEE.EmployeeID"), nullable=True)
    PhoneNumber = Column(String)
    EmailAddress = Column(String)
    Address = Column(String)
    ContactType = Column(VARCHAR(5))

    EmployeeRelationship = relationship("EMPLOYEE", back_populates="EMP_CONTACT")