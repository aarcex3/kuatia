from datetime import date
from typing import Annotated

from msgspec import Meta, Struct

from src.constraints import PRICE, RUC, VAT
from src.issuer.schemas import IssuerSchema


class InvoiceDetail(Struct):
    product_name: str
    unit_price: PRICE
    sale_price_five: VAT
    sale_price_ten: VAT
    quantity: int = Annotated[int, Meta(ge=0)]


class InvoiceSchema(Struct):
    issuer: IssuerSchema
    detail: list[InvoiceDetail]
    ruc: RUC
    date_issue: date
    date_expiration: date
    stamping: int
    is_expired: bool
    name: str
    vat_five: VAT
    vat_ten: VAT
    subtotal: PRICE
    total: PRICE
