from pymongo import MongoClient
import falcon

from src.repositories.invoice_repository import InvoiceRepository
from src.middleware.cors import CORSComponent

from src.resources.invoice import InvoiceResource

def create_context(db_client: MongoClient):
    # Database
    db = db_client.invoice_db

    # Respositories
    invoice_repository = InvoiceRepository(db.invoices)

    # API and middleware
    api = falcon.API(middleware=[CORSComponent()])

    # Resources
    invoices = InvoiceResource(invoice_repository)

    # Routes
    api.add_route('/invoices', invoices)
    api.add_route('/invoices/{invoice_id}', invoices, suffix='single')

    api.add_route('/users/{user_id}/invoices', invoices, suffix='by_user')

    context = {
        'databaseClient': db,
        'repositories': {
            'InvoiceRepository': invoice_repository
        },
        'resources': {
            'InvoiceResource': invoices
        },
        'api': api
    }
    return context

context = create_context(MongoClient('mongo', 27017))
api = context.get('api')
