from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Class(Base):
    __tablename__ = "class"

    # Define Columns
    ClassID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    ClassTitle = Column(String)
    DateTime = mapped_column(Integer, ForeignKey("schedule.DateTime"), nullable=True)
    InstructorID = mapped_column(Integer, ForeignKey("employee.EmployeeID"), nullable=True)

    # Initialize Relationships
    # DateTimelationship = relationship("schedule", back_populates="class")
    # InstructorRelationship = relationship("employee", back_populates="class")