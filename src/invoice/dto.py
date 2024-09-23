from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig

from src.invoice.models import Invoice


class InvoiceDTO(SQLAlchemyDTO[Invoice]):
    config = SQLAlchemyDTOConfig(exclude={"id"})
