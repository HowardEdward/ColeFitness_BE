from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, DATE
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Membership(Base):
    __tablename__ = "MEMBERSHIP"

    # Define Columns
    MembershipID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    MembershipType = Column(VARCHAR(10))
    MembershipDuration = Column(String)
    MembershipDescription = Column(String)
    MembershipPrice = Column(Integer)
    StartingDate = Column(DATE)
    ExpireDate = Column(DATE)

    # Initialize Relationships