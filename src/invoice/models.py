from datetime import date

from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.issuer.models import Issuer


class InvoiceDetail(Base):
    __tablename__ = "invoice_details"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str]
    quantity: Mapped[int]
    unit_price: Mapped[float]
    sale_price_five: Mapped[float]
    sale_price_ten: Mapped[float]

    invoices: Mapped["Invoice"] = relationship("Invoice", back_populates="detail")
    __table_args__ = (Index("idx_product_name", "product_name"),)


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    stamping: Mapped[int]
    date_issue: Mapped[date]
    date_expiration: Mapped[date]
    is_expired: Mapped[bool]
    ruc: Mapped[int]
    name: Mapped[str]
    vat_five: Mapped[float]
    vat_ten: Mapped[float]
    subtotal: Mapped[float]
    total: Mapped[float]

    issuer: Mapped[Issuer] = relationship("Issuer", back_populates="invoices")
    detail: Mapped[InvoiceDetail] = relationship(
        "InvoiceDetail", back_populates="invoices"
    )

    __table_args__ = (
        Index("idx_invoice_stamping", "stamping"),
        Index("idx_invoice_date_issue", "date_issue"),
        Index("idx_invoice_ruc", "ruc"),
    )
