from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Account(Base):
    __tablename__ = "ACCOUNT"
    AccountID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EmployeeID = mapped_column(Integer, ForeignKey("EMPLOYEE.EmployeeID"),nullable=True)
    UserName = Column(String)
    Password = Column(String)
    RoleKey = mapped_column(VARCHAR(10), nullable=True)
    Status = Column(Boolean, default=False)

    EmployeeRelationship = relationship("EMPLOYEE", back_populates="ACCOUNT")
    
