import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from src.database import Base


class Garden(Base):
    __tablename__ = "garden"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey("user.id"))
    plant_id = Column(Integer, ForeignKey("plant.id"), unique=True, nullable=True)
    price = Column(Numeric(precision=10, scale=2), default=20)

    user = relationship("User", backref="gardens")
    plant = relationship("Plant", backref="garden")
