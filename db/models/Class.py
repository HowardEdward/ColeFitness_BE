from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Class(Base):
    __tablename__ = "CLASS"

    # Define Columns
    ClassID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    ClassTitle = Column(String)
    RegisteredStudentNum = Column(Integer)
    ScheduleID = mapped_column(Integer, ForeignKey("SCHEDULE.ScheduleID"), nullable=True)
    InstructorID = mapped_column(Integer, ForeignKey("EMPLOYEE.EmployeeID"), nullable=True)

    # Initialize Relationships
    ScheduleRelationship = relationship("SCHEDULE", back_populates="CLASS")
    InstructorRelationship = relationship("EMPLOYEE", back_populates="CLASS")