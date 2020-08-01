import json

import falcon

from src.model.invoice import Invoice
from src.model.invoices_db import invoices

class InvoiceResource:

    def on_get(self, req, resp):
        resp.body = json.dumps(
            list(map(lambda invoice: invoice.to_dict(), invoices)),
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_200
