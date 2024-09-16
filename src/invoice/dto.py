from litestar.dto.config import DTOConfig
from litestar.dto.msgspec_dto import MsgspecDTO

from src.invoice.schemas import InvoiceSchema


class InvoiceDTO(MsgspecDTO):
    config = DTOConfig(exclude={"id"})
    model_type = InvoiceSchema
