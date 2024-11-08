from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, DATE
from sqlalchemy.orm import mapped_column, relationship
from db.connectDB import Base

class Equipment(Base):
    __tablename__ = "equipment"

    # Define Columns
    EquipmentID = Column(Integer, primary_key=True, autoincrement=True, default=1)
    EquipmentName = Column(VARCHAR(30))
    PurchasedDate = Column(DATE)
    BranchID = mapped_column(Integer, ForeignKey("branch.BranchID"), nullable=True)
    EquipmentListID = mapped_column(Integer, ForeignKey("equipment_list.EquipmentListID"), nullable=True)
    EquipmentMaintenanceID = mapped_column(Integer, ForeignKey("equipment_maintenance.EquipmentMaintenanceID"), nullable=True)

    # Initialize Relationships
    # EquipmentListRelationship = relationship("equipment_list", back_populates="equipment")
    # EquipmentMaintenanceRelationship = relationship("equipment_maintenance", back_populates="equipment")
    # BranchRelationship = relationship("branch", back_populates="equipment")