import unittest

import mongomock

from src.model.invoice import Invoice, InvoiceBuilder
from test.invoice_data import invoices

from src.repositories.invoice_repository import InvoiceRepository

class InvoiceRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.db = mongomock.MongoClient().db
        self.invoice_repository = InvoiceRepository(self.db.invoices)

    def test_saveInovice(self):
        invoice = invoices.__getitem__(0)
        inserted_id = self.invoice_repository.save(invoice)
        collections = self.db.list_collection_names()
        self.assertEqual(collections, ['invoices'])
        self.assertEqual(inserted_id, str(invoice.id))
