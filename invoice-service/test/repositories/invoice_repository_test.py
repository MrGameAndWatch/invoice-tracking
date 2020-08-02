from typing import List

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

    def test_saveAllInvoices(self):
        inserted_ids: List[str] = self.invoice_repository.save_all(invoices)
        expected_ids: List[str] = list(map(lambda invoice: str(invoice.id), invoices))
        self.assertEqual(inserted_ids, expected_ids)

    def test_findAll(self):
        self.invoice_repository.save_all(invoices)
        found_invoices: List[Invoice] = self.invoice_repository.find_all()
        for invoice in found_invoices:
            self.assertIs(type(invoice), Invoice)
        self.assertEqual(
            list(map(lambda invoice: invoice.to_dict(), found_invoices)),
            list(map(lambda invoice: invoice.to_dict(), invoices))
        )

    def test_findKnownInvoiceById(self):
        self.invoice_repository.save_all(invoices)
        exptected_invoice: Invoice = invoices.__getitem__(0)
        search_id = str(exptected_invoice.id)
        found_invoice: Invoice = self.invoice_repository.find_by_id(search_id)
        self.assertIs(type(found_invoice), Invoice)
        self.assertEqual(found_invoice.to_dict(), exptected_invoice.to_dict())

    def test_findUnknownInvoiceById(self):
        self.invoice_repository.save_all(invoices)
        found_invoice: Invoice = self.invoice_repository.find_by_id("unknown-id")
        self.assertEqual(found_invoice, None)
