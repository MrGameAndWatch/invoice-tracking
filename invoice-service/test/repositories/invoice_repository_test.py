import unittest

import mongomock

from src.model.invoice import Invoice, InvoiceBuilder

from src.repositories.invoice_repository import InvoiceRepository

class InvoiceRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.db = mongomock.MongoClient().db
        self.invoice_repository = InvoiceRepository(self.db.invoices)
        self.invoice = InvoiceBuilder() \
            .user_id("abc-def-gh-1") \
            .description("Hotel im Park") \
            .amount(85.50) \
            .build()

    def test_saveInovice(self):
        inserted_id = self.invoice_repository.save(self.invoice)
        collections = self.db.list_collection_names()
        self.assertEqual(collections, ['invoices'])
        self.assertEqual(inserted_id, str(self.invoice.id))
