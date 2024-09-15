import falcon
import falcon.asgi

from src.media import SERIALIZERS


class InvoiceResource:
    async def on_get(self, req: falcon.Request, resp: falcon.Response):
        """Get all invoices"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Get all invoices"

    async def on_get_invoice(self, req: falcon.Request, resp: falcon.Response):
        """Get a specific invoice"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Get an invoice"

    async def on_post(self, req: falcon.Request, resp: falcon.Response):
        """Add a new invoice"""
        resp.status = falcon.HTTP_201
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Add a new invoice"

    async def on_put_invoice(self, req: falcon.Request, resp: falcon.Response):
        """Update an existing invoice"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Update an invoice"

    async def on_delete_invoice(self, req: falcon.Request, resp: falcon.Response):
        """Delete an invoice"""
        resp.status = falcon.HTTP_204
        resp.content_type = falcon.MEDIA_JSON
        resp.text = "Delete an invoice"


app = falcon.asgi.App()

invoice_resource = InvoiceResource()

app.add_route("/invoices", invoice_resource)
app.add_route("/invoices/{invoice_id}", invoice_resource, suffix="invoice")

app.req_options.media_handlers.update(SERIALIZERS)
app.resp_options.media_handlers.update(SERIALIZERS)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)
