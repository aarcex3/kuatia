from sqlalchemy import Column, Index, Integer, String

from src.database import BaseDBModel


class Issuer(BaseDBModel):
    __tablename__ = "issuer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruc = Column(Integer, unique=True)
    name = Column(String, unique=True)

    __table_args__ = (Index("idx_issuer_name", "name"), Index("idx_issuer_ruc", "ruc"))
