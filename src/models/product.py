from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from src.database import Base
from src.models.user import user

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("category", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("brand", String, nullable=False),
    Column("username", ForeignKey(user.c.username), nullable=False)
)


class Product(Base):
    __tablename__ = "product"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=True)
    description = Column("description", String, nullable=True)
    category = Column("category", String, nullable=True)
    price = Column("price", Float, nullable=True)
    brand = Column("brand", String, nullable=True)
    username = Column("username", ForeignKey(user.c.username), nullable=False)
