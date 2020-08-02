import unittest

import msgpack

import falcon
from falcon import testing

from test.invoice_data import invoices

from src.main import api

class RoutesTest(unittest.TestCase):

    def test_getInvoices(self):
        exptected_invoices = list(map(lambda invoice: invoice.to_dict(), invoices))
        client = testing.TestClient(api)
        response = client.simulate_get("/invoices")
        result_invoices = response.json
        self.assertEqual(result_invoices, exptected_invoices)
        self.assertEqual(response.status, falcon.HTTP_OK)
