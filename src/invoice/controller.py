from litestar import delete, get, post, put
from litestar.controller import Controller

from src.invoice.service import InvoiceService


class InvoiceController(Controller):
    path = "/invoices"

    @get(description="Get all the invoices")
    async def get_all(self, invoice_service: InvoiceService) -> None:
        pass

    @get(path="/{invoice_id:int}", description="Get one invoice")
    async def get_one(self, invoice_service: InvoiceService) -> None:
        pass

    @post(description="Create one invoice")
    async def create_one(self, invoice_service: InvoiceService) -> None:
        pass

    @put(path="/{invoice_id:int}", description="Update one invoice")
    async def update_one(self, invoice_service: InvoiceService) -> None:
        pass

    @delete(path="/{invoice_id:int}", description="Delete one invoice")
    async def delete_one(self, invoice_service: InvoiceService) -> None:
        pass
