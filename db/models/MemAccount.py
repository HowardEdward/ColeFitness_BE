from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Boolean
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class MemAccount(Base):
    __tablename__ = "mem_account"

    # Define Columns
    AccountID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    UserName = Column(String)
    Password = Column(String)
    AccountType = Column(VARCHAR(10))
    Status = Column(Boolean, default=False)
    MemberID = mapped_column(Integer, ForeignKey("member.MemberID"))

    # Initialize Relationships
    MemberRelationship = relationship("member", back_populates="mem_account")