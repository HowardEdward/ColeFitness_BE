from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Boolean
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class MemAccount(Base):
    __tablename__ = "MEM_ACCOUNT"

    # Define Columns
    AccountID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    UserName = Column(String)
    Password = Column(String)
    AccountType = Column(VARCHAR(10))
    Status = Column(Boolean, default=False)
    MemberID = mapped_column(Integer, ForeignKey("MEMBER.MemberID"))

    # Initialize Relationships
    MemberRelationship = relationship("MEMBER", back_populates="MEM_ACCOUNT")