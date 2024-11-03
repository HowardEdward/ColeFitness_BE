from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Role(Base):
    __tablename__ = "ROLE"
    RoleID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    RoleKey = Column(VARCHAR(10))
    RoleName = Column(VARCHAR(30))

    EmployeeRelationship = relationship("EMPLOYEE", back_populates="ROLE")