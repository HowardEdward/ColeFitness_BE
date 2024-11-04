from sqlalchemy import Column, Integer, VARCHAR, DATE, BLOB, ForeignKey
from db.connectDB import Base
from sqlalchemy.orm import mapped_column, relationship
class Employee(Base):
    __tablename__ = "EMPLOYEE"

    # Define Columns
    EmployeeID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    FirstName = Column(VARCHAR(30))
    MiddleName = Column(VARCHAR(30), nullable=True)
    LastName = Column(VARCHAR(30))
    DOB = Column(DATE)
    Picture = Column(BLOB, nullable=True)
    RoleKey = mapped_column(VARCHAR(10), ForeignKey("ROLE.RoleKey"),nullable=True)
    ContactID = mapped_column(Integer, ForeignKey("EMP_CONTACT.ContactID"),nullable=True)
    AccountID = mapped_column(Integer, ForeignKey("EMP_ACCOUNT.AccountID"),nullable=True)

    # Initialize Relationships
    RoleRelationship = relationship("ROLE", back_populates="EMPLOYEE")
    ContactRelationship = relationship("EMP_CONTACT", back_populates="EMPLOYEE")
    AccountRelationship = relationship("EMP_ACCOUNT", back_populates="EMPLOYEE")
    