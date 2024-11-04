from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, DATE
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Equipment(Base):
    __tablename__ = "EQUIPMENT"

    # Define Columns
    EquipmentID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EquipmentName = Column(VARCHAR(30))
    PurchasedDate = Column(DATE)
    BranchID = mapped_column(Integer, ForeignKey("BRANCH.BranchID"), nullable=True)
    EquipmentListID = mapped_column(Integer, ForeignKey("EQUIPMENT_LIST.EquipmentListID"), nullable=True)
    EquipmentMaintenanceID = mapped_column(Integer, ForeignKey("EQUIPMENT_MAINTENANCE.EquipmentMaintenanceID"), nullable=True)

    # Initialize Relationships
    EquipmentListRelationship = relationship("EQUIPMENT_LIST", back_populates="EQUIPMENT")
    EquipmentMaintenanceRelationship = relationship("EQUIPMENT_MAINTENANCE", back_populates="EQUIPMENT")
    BranchRelationship = relationship("BRANCH", back_populates="EQUIPMENT")