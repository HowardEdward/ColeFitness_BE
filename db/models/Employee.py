from sqlalchemy import Column, Integer, VARCHAR, DATE, LargeBinary as BLOB, ForeignKey, FLOAT, event, DDL
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Employee(Base):
    __tablename__ = "employee"

    # Define Columns
    EmployeeID = Column(Integer, primary_key=True, nullable=False, autoincrement=True, default=1, unique=True)
    FirstName = Column(VARCHAR(30))
    MiddleName = Column(VARCHAR(30), nullable=True)
    LastName = Column(VARCHAR(30))
    Gender = Column(VARCHAR(10))
    DOB = Column(DATE)
    Picture = Column(BLOB, nullable=True)
    # Weight = Column(FLOAT, nullable=True)
    # Height = Column(FLOAT, nullable=True)
    RoleKey = mapped_column(VARCHAR(10), ForeignKey("role.RoleKey"),nullable=True)
    EmpContactID = mapped_column(Integer, ForeignKey("emp_contact.EmpContactID"),nullable=True)
    EmpAccountID = mapped_column(Integer, ForeignKey("emp_account.EmpAccountID"),nullable=True)

    # Initialize Relationships
    # RoleRelationship = relationship("role", back_populates="employee")
    # ContactRelationship = relationship("emp_contact", back_populates="employee")
    # AccountRelationship = relationship("emp_account", back_populates="employee")

    def __repr__(self):
        return f"EmployeeID: {self.EmployeeID} FirstName: {self.FirstName} MiddleName: {self.MiddleName} LastName: {self.LastName} DOB: {self.DOB}"

# Base.metadata.create_all(engine)