from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class EquipmentList(Base):
    __tablename__ = "equipment_list"

    # Define Columns
    EquipmentListID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    Quantity = Column(Integer)
    EquipmentName = mapped_column(Integer, ForeignKey("equipment.EquipmentName"), nullable=True)

    # Initialize Relationship
    EquipmentRelationship = relationship("equipment", back_populates="equipment_list")