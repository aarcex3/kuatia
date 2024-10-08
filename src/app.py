from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyPlugin
from litestar.di import Provide

from src.database import db_connection, provide_session, sqlalchemy_config
from src.invoice.controller import InvoiceController
from src.invoice.repository import provide_invoice_detail_repo, provide_invoice_repo
from src.invoice.services import InvoiceDetailService, InvoiceService

app = Litestar(
    debug=True,
    route_handlers=[InvoiceController],
    dependencies={
        "invoice_service": Provide(InvoiceService, sync_to_thread=False),
        "invoice_repo": Provide(provide_invoice_repo),
        "invoice_detail_service": Provide(InvoiceDetailService, sync_to_thread=False),
        "invoice_detail_repo": Provide(provide_invoice_detail_repo),
        "session": Provide(provide_session),
    },
    plugins=[SQLAlchemyPlugin(sqlalchemy_config)],
    lifespan=[db_connection],
)
