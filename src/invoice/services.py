from typing import Any

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from src.invoice.models import Invoice, InvoiceDetail
from src.invoice.repository import InvoiceDetailRepository, InvoiceRepository


class InvoiceService(SQLAlchemyAsyncRepositoryService[Invoice]):
    repository_type = InvoiceRepository

    def __init__(self, session: AsyncSession, **repo_kwargs: Any) -> None:
        self.repository: InvoiceRepository = self.repository_type(
            session=session, **repo_kwargs
        )  # type: ignore
        self.model_type = self.repository.model_type


class InvoiceDetailService(SQLAlchemyAsyncRepositoryService[InvoiceDetail]):
    repository_type = InvoiceDetailRepository

    def __init__(self, session: AsyncSession, **repo_kwargs: Any) -> None:
        self.repository: InvoiceDetailRepository = self.repository_type(
            session=session, **repo_kwargs
        )  # type: ignore
        self.model_type = self.repository.model_type
