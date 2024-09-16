from datetime import date
from typing import Annotated

from msgspec import Meta, Struct

RUC = Annotated[int, Meta(gt=1_000_000)]


class IssuerSchema(Struct):
    name: str
    ruc: RUC


class InvoiceDetail(Struct):
    product_name: str
    quantity: int
    unit_price: float
    sale_price_five: float
    sale_price_ten: float


class InvoiceSchema(Struct):
    issuer: IssuerSchema
    detail: list[InvoiceDetail]
    ruc: RUC
    date_issue: date
    date_expiration: date
    stamping: int
    is_expired: bool
    name: str
    vat_five: float
    vat_ten: float
    subtotal: float
    total: float
