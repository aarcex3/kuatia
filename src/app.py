import falcon
import falcon.asgi
from falcon.asgi import App

from src.database.manager import DataBase, db
from src.media import SERIALIZERS


class InvoiceResource:
    def __init__(self, db: DataBase) -> None:
        self.db = db

    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        """Get all invoices"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Get all invoices"

    async def on_get_invoice(
        self, req: falcon.Request, resp: falcon.Response, invoice_id: int
    ):
        """Get a specific invoice"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {"message": "Get an invoice", "invoice_id": invoice_id}

    async def on_post(self, req: falcon.Request, resp: falcon.Response):
        """Add a new invoice"""
        resp.status = falcon.HTTP_201
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Add a new invoice"

    async def on_put_invoice(
        self, req: falcon.Request, resp: falcon.Response, invoice_id: int
    ):
        """Update an existing invoice"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {"message": "Update an invoice", "invoice_id": invoice_id}

    async def on_delete_invoice(
        self, req: falcon.Request, resp: falcon.Response, invoice_id: int
    ):
        """Delete an invoice"""
        resp.status = falcon.HTTP_204
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {"message": "Delete an invoice", "invoice_id": invoice_id}


app: App = falcon.asgi.App()


invoice_resource: InvoiceResource = InvoiceResource(db)

app.add_route("/invoices", invoice_resource)
app.add_route("/invoices/{invoice_id}", invoice_resource, suffix="invoice")

app.req_options.media_handlers.update(SERIALIZERS)
app.resp_options.media_handlers.update(SERIALIZERS)
