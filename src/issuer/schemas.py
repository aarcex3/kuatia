from msgspec import Struct

from src.constraints import RUC


class IssuerSchema(Struct):
    name: str
    ruc: RUC
