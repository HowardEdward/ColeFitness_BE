from sqlalchemy import Column, Integer, String, VARCHAR, DATE, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Member(Base):
    __tablename__ = "member"

    # Defile Columns
    MemberID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    FirstName = Column(VARCHAR(30))
    MiddleName = Column(VARCHAR(30), nullable=True)
    LastName = Column(VARCHAR(30))
    DOB = Column(DATE)
    PhoneNumber = Column(String)
    EmailAddress = Column(String)
    Address = Column(String)
    MembershipType = mapped_column(VARCHAR(10), ForeignKey("membership.MembershipType"), nullable=True)

    # Initialize Relationships
    MembershipRelationship = relationship("membership", back_populates="member")