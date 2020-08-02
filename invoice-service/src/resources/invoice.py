import json

import falcon

from src.util import utils
from src.repositories.invoice_repository import InvoiceRepository

class InvoiceResource:

    def __init__(self, invoice_repository: InvoiceRepository):
        self.invoice_repository = invoice_repository

    def on_get(self, req, resp):
        invoices = self.invoice_repository.find_all()
        resp.body = json.dumps(
            utils.convert_invoices_to_dicts(invoices),
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_OK

    def on_get_single(self, req, resp, invoice_id: str):
        invoice = self.invoice_repository.find_by_id(invoice_id)
        if invoice is None:
            resp.body = json.dumps(
                {},
                ensure_ascii=False
            )
            resp.status = falcon.HTTP_NOT_FOUND
        else:
            resp.body = json.dumps(
                invoice.to_dict(),
                ensure_ascii=False
            )
            resp.status = falcon.HTTP_OK

    def on_get_user_id(self, req, resp, user_id: str):
        invoices = self.invoice_repository.find_by_userId(user_id)
        resp.body = json.dumps(
            utils.convert_invoices_to_dicts(invoices),
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_OK
