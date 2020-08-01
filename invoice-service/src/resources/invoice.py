import json

import falcon

class InvoiceResource:

    def on_get(self, req, resp):
        invoices = [{
            'employee': '1',
            'description': 'Lunch',
            'amount': 30.00
        }]
        resp.body = json.dumps(invoices, ensure_ascii=False)
        resp.status = falcon.HTTP_200
