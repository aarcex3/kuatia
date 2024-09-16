import falcon
import falcon.asgi
from falcon.asgi import App

from src.database.manager import db
from src.media import SERIALIZERS
from src.resources.invoice import InvoiceResource

app: App = falcon.asgi.App()


invoice_resource: InvoiceResource = InvoiceResource(db)

app.add_route("/invoices", invoice_resource)
app.add_route("/invoices/{invoice_id}", invoice_resource, suffix="invoice")

app.req_options.media_handlers.update(SERIALIZERS)
app.resp_options.media_handlers.update(SERIALIZERS)
