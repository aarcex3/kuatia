from typing import Annotated, Any

from litestar import Response, delete, get, post, put, status_codes
from litestar.controller import Controller
from litestar.enums import MediaType, RequestEncodingType
from litestar.exceptions import HTTPException, NotFoundException
from litestar.params import Body

from src.invoice.dto import InvoiceDTO
from src.invoice.models import Invoice
from src.invoice.schemas import InvoiceSchema
from src.invoice.services import InvoiceDetailService, InvoiceService


class InvoiceController(Controller):
    path = "/invoices"
    tags = ["invoices", "invoice"]

    @get(
        description="Get all the invoices",
        return_dto=InvoiceDTO,
        media_type=MediaType.JSON,
    )
    async def get_all(self, invoice_service: InvoiceService) -> list[Invoice]:
        return await invoice_service.list()

    @get(
        path="/{invoice_id:int}",
        description="Get one invoice",
        media_type=MediaType.JSON,
        return_dto=InvoiceDTO,
    )
    async def get_one(
        self, invoice_id: int, invoice_service: InvoiceService
    ) -> Response[Any]:
        invoice: Invoice | None = await invoice_service.get_one_or_none(
            Invoice.id == invoice_id
        )
        if invoice:
            return invoice
        raise NotFoundException(
            detail=f"Invoice with id {invoice_id} not found",
            status_code=status_codes.HTTP_404_NOT_FOUND,
        )

    @post(description="Create one invoice", media_type=MediaType.JSON)
    async def create_one(
        self,
        data: Annotated[
            InvoiceSchema, Body(media_type=RequestEncodingType.URL_ENCODED)
        ],
        invoice_service: InvoiceService,
        invoice_detail_service: InvoiceDetailService,
        # issuer_service:IssuerService
    ) -> None:
        try:
            await invoice_detail_service.create(data=data.detail)
            # await issuer_service.create(data=data.issuer)
        except Exception as ex:
            raise HTTPException(
                detail=str(ex), status_code=status_codes.HTTP_500_INTERNAL_SERVER_ERROR
            ) from ex

    @put(
        path="/{invoice_id:int}",
        description="Update one invoice",
        media_type=MediaType.JSON,
    )
    async def update_one(self, invoice_service: InvoiceService) -> None:
        pass

    @delete(
        path="/{invoice_id:int}",
        description="Delete one invoice",
        media_type=MediaType.JSON,
    )
    async def delete_one(self, invoice_service: InvoiceService) -> None:
        pass
