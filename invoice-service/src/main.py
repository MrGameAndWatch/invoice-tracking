import falcon

from src.resources.invoice import InvoiceResource

api = falcon.API()

invoices = InvoiceResource()
api.add_route('/invoices', invoices)
