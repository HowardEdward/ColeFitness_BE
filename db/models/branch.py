from sqlalchemy import String, Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship, mapped_column
from db.connectDB import Base

class Branch(Base):
    __tablename__ = "branch"

    # Define Columns
    BranchID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    BranchName = Column(VARCHAR(30))
    BranchPhoneNumber = Column(Integer)
    BranchEmailAddress = Column(String)
    BranchAddress = Column(String)
    EmployeeID = mapped_column(Integer, ForeignKey("employee.EmployeeID"), nullable=True)
    # Initialize Relationships
    EmployeeRelationship = relationship("employee", back_populates="branch")