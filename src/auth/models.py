from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Numeric, UniqueConstraint
from sqlalchemy.orm import relationship

from src.database import Base


users_plats = Table(
    "user_plant",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user.id")),
    Column("plant_id", ForeignKey("plant.id")),
    Column("amount", Integer),
    UniqueConstraint('user_id', 'plant_id'),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    wallet = Column(Numeric(precision=10, scale=2))

    plants = relationship("Plant", secondary=users_plats, backref="users")
