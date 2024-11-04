from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Account(Base):
    __tablename__ = "ACCOUNT"

    # Define Columns
    AccountID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EmployeeID = mapped_column(Integer, ForeignKey("EMPLOYEE.EmployeeID"))
    UserName = Column(String)
    Password = Column(String)
    AccountType = Column(VARCHAR(10))
    Status = Column(Boolean, default=False)

    # Initialize Relationships
    EmployeeRelationship = relationship("EMPLOYEE", back_populates="ACCOUNT")
    

