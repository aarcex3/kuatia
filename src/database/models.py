from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.database.utils import hash_password

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @property
    def as_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)

    __table_args__ = (
        Index("idx_username", "username"),
        Index("idx_email", "email"),
    )

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = hash_password(password)
        self.email = email


class Invoice(BaseModel):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
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

    user = relationship("User")
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


class InvoiceDetail(BaseModel):
    __tablename__ = "invoice_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float)
    sale_price_five = Column(Float)
    sale_price_ten = Column(Float)

    __table_args__ = (Index("idx_product_name", "product_name"),)


class Issuer(BaseModel):
    __tablename__ = "issuer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruc = Column(Integer, unique=True)
    name = Column(String, unique=True)

    __table_args__ = (Index("idx_issuer_name", "name"), Index("idx_issuer_ruc", "ruc"))
