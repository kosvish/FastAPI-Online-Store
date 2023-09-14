from sqlalchemy import MetaData, Table, Column, Integer, String, Float, TIMESTAMP, ForeignKey
from datetime import datetime
from user import user

metadata = MetaData()

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("status", String, nullable=False, default="в обработке"),
    Column("total_price", Float, nullable=False)
)
