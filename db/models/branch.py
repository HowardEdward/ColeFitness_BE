from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from db.connectDB import Base

class Branch(Base):
    __tablename__ = "BRANCH"

    # Define Columns
    BranchID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    BranchPhoneNumber = Column(Integer)
    BranchEmailAddress = Column(String)
    BranchAddress = Column(String)
    ManagerID = mapped_column(Integer, ForeignKey("EMPLOYEE.EmployeeID"), nullable=True)
    
    # Initialize Relationships
    ManagerRelationship = relationship("EMPLOYEE", back_populates="BRANCH")