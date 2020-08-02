import json

import falcon

from src.repositories.invoice_repository import InvoiceRepository

class InvoiceResource:

    def __init__(self, invoice_repository: InvoiceRepository):
        self.invoice_repository = invoice_repository

    def on_get(self, req, resp):
        invoices = self.invoice_repository.find_all()
        resp.body = json.dumps(
            list(map(lambda invoice: invoice.to_dict(), invoices)),
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_200
