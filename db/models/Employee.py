from sqlalchemy import Column, Integer, VARCHAR, DATE, BLOB, ForeignKey
from db.connectDB import Base
from sqlalchemy.orm import mapped_column, relationship
class Employee(Base):
    __tablename__ = "EMPLOYEE"
    EmployeeID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    FirstName = Column(VARCHAR(30))
    MiddleName = Column(VARCHAR(30), nullable=True)
    LastName = Column(VARCHAR(30))
    DOB = Column(DATE)
    # Picture = Column(BLOB)
    RoleKey = mapped_column(VARCHAR(10),nullable=True)
    ContactID = mapped_column(Integer, nullable=True)

    RoleRelationship = relationship("ROLE", back_populates="EMPLOYEE")
    ContactRelationship = relationship("CONTACT", back_populates="EMPLOYEE")
    