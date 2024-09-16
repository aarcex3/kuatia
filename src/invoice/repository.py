from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from src.invoice.models import Invoice, InvoiceDetail

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class InvoiceRepository(SQLAlchemyAsyncRepository[Invoice]):  # pylint: disable=duplicate-bases
    model_type = Invoice


async def provide_invoice_repo(session: AsyncSession) -> InvoiceRepository:
    return InvoiceRepository(session=session)


class InvoiceDetailRepository(SQLAlchemyAsyncRepository[InvoiceDetail]):  # pylint: disable=duplicate-bases
    model_type = InvoiceDetail


async def provide_invoice_detail_repo(session: AsyncSession) -> InvoiceDetailRepository:
    return InvoiceDetailRepository(session=session)
