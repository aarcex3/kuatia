from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Index, Integer, String
from sqlalchemy.orm import relationship

from src.database import BaseDBModel


class Invoice(BaseDBModel):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    issuer_id = Column(Integer, ForeignKey("issuer.id"))
    stamping = Column(Integer)
    date_issue = Column(Date)
    date_expiration = Column(Date)
    is_expired = Column(Boolean)
    detail_id = Column(Integer, ForeignKey("invoice_detail.id"))
    ruc = Column(Integer)
    name = Column(String)
    vat_five = Column(Float)
    vat_ten = Column(Float)
    subtotal = Column(Float)
    total = Column(Float)

    issuer = relationship("Issuer")
    detail = relationship("InvoiceDetail")

    __table_args__ = (
        Index("idx_invoice_stamping", "stamping"),
        Index("idx_user_id", "user_id"),
        Index("idx_issuer_id", "issuer_id"),
        Index("idx_detail_id", "detail_id"),
        Index("idx_invoice_date_issue", "date_issue"),
        Index("idx_invoice_ruc", "ruc"),
    )


class InvoiceDetail(BaseDBModel):
    __tablename__ = "invoice_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float)
    sale_price_five = Column(Float)
    sale_price_ten = Column(Float)

    __table_args__ = (Index("idx_product_name", "product_name"),)
