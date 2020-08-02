import unittest
import mongomock

import falcon
from falcon import testing

from test.invoice_data import invoices

from src.main import create_context

class RoutesTest(unittest.TestCase):

    def setUp(self):
        mock_client = mongomock.MongoClient().db
        self.context = create_context(mock_client)
        self.context \
            .get('repositories') \
            .get('InvoiceRepository') \
            .save_all(invoices)

    def test_getInvoices(self):
        exptected_invoices = list(map(lambda invoice: invoice.to_dict(), invoices))
        client = testing.TestClient(self.context.get('api'))
        response = client.simulate_get("/invoices")
        result_invoices = response.json
        self.assertEqual(result_invoices, exptected_invoices)
        self.assertEqual(response.status, falcon.HTTP_OK)
