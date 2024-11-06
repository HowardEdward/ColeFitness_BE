from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, DATE
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import connectDB

connectDB = connectDB()
class Membership(connectDB.Base):
    __tablename__ = "MEMBERSHIP"

    # Define Columns
    MembershipID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    MembershipType = Column(VARCHAR(10))
    MembershipPrice = Column(Integer)
    MembershipDescription = Column(String)
    MembershipDuration = Column(String)
    StartingDate = Column(DATE)
    ExpireDate = Column(DATE)

    # Initialize Relationships