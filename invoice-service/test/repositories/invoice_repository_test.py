from typing import List, Dict

import unittest

import mongomock

from src.model.invoice import Invoice, InvoiceBuilder
from src.util import utils
from test.invoice_data import invoices, invoices_for_one_user

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
            utils.convert_invoices_to_dicts(found_invoices),
            utils.convert_invoices_to_dicts(invoices)
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

    def test_findInvoicesByKnownUserId(self):
        self.invoice_repository.save_all(invoices_for_one_user)
        user_id = invoices_for_one_user.__getitem__(0).user_id
        found_invoices = self.invoice_repository.find_by_userId(user_id)
        self.assertEqual(
            utils.convert_invoices_to_dicts(found_invoices),
            utils.convert_invoices_to_dicts(invoices_for_one_user)
        )

    def test_findByUnknownUserId(self):
        found_invoices = self.invoice_repository.find_by_userId("unknown-user-id")
        self.assertEqual(
            found_invoices,
            []
        )
