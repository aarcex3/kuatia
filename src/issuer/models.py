from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Issuer(Base):
    __tablename__ = "issuers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ruc: Mapped[int] = mapped_column(unique=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)

    invoices: Mapped[list["Invoice"]] = relationship("Invoice", back_populates="issuer")  # type: ignore

    __table_args__ = (Index("idx_issuer_name", "name"), Index("idx_issuer_ruc", "ruc"))
