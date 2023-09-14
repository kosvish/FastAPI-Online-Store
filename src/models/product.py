from sqlalchemy import MetaData, Table, Column, Integer, String, Float

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("category", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("brand", String, nullable=False)
)
