from sqlalchemy import Column, Integer, String, Enum, Numeric, CheckConstraint
from sqlalchemy.orm import relationship

from src.auth.models import users_plats
from src.database import Base
from src.plant.choices import PlantType, PlantClass


class Plant(Base):
    __tablename__ = "plant"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(Enum(PlantType))
    classification = Column(Enum(PlantClass))
    price = Column(Numeric(precision=10, scale=2))
    growth_stage = Column(Integer, default=0)

    users = relationship("User", secondary=users_plats, backref="plant")

    __table_args__ = (CheckConstraint('growth_stage >= 0'),)
