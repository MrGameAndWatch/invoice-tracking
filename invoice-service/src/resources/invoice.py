import json
import jsonschema
from jsonschema import validate

import falcon

from src.util import utils
from src.model.invoice import Invoice, InvoiceBuilder
from src.model.constants import errors
from src.repositories.invoice_repository import InvoiceRepository

invoiceSchema = {
    "type": "object",
    "properties": {
        "description": { "type": "string" },
        "amount": { "type": "number" }
    },
    "required": ["description", "amount"]
}

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

    def on_get_by_user(self, req, resp, user_id: str):
        invoices = self.invoice_repository.find_by_userId(user_id)
        resp.body = json.dumps(
            utils.convert_invoices_to_dicts(invoices),
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_OK

    def on_post_by_user(self, req, resp, user_id: str):
        data = json.loads(req.bounded_stream.read())
        try:
            validate(instance=data, schema=invoiceSchema)
        except jsonschema.exceptions.ValidationError as err:
            resp.body = json.dumps(
                { 'errorMsg': errors.get('wrongInvoiceFormat') },
                ensure_ascii=False
            )
            resp.status = falcon.HTTP_UNPROCESSABLE_ENTITY
            return

        invoice = InvoiceBuilder() \
            .user_id(user_id) \
            .description(data['description']) \
            .amount(data['amount']) \
            .build()
        invoice_id = self.invoice_repository.save(invoice)
        resp.body = json.dumps(
            { 'invoiceId': invoice_id },
            ensure_ascii=False
        )
        resp.status = falcon.HTTP_CREATED
