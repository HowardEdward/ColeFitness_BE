from sqlalchemy import Column, Integer, String, VARCHAR, DATE, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Member(Base):
    __tablename__ = "MEMBER"

    # Defile Columns
    MemberID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    FirstName = Column(VARCHAR(30))
    MiddleName = Column(VARCHAR(30), nullable=True)
    LastName = Column(VARCHAR(30))
    DOB = Column(DATE)
    PhoneNumber = Column(Integer)
    EmailAddress = Column(String)
    Address = Column(String)
    MembershipType = mapped_column(Integer, ForeignKey("MEMBERSHIP.MembershipType"), nullable=True)

    # Initialize Relationships
    MembershipRelationship = relationship("MEMBERSHIP", back_populates="MEMBER")