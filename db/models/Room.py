from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Room(Base):
    __tablename__ = "room"

    # Define Columns
    RoomID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    RoomName = Column(VARCHAR(30))
    RoomMaximum = Column(Integer(2))
    BranchID = mapped_column(Integer, ForeignKey("branch.BranchID"), nullable=True)

    # Initalize Relationships
    BranchRelationship = relationship("branch", back_populates="room")