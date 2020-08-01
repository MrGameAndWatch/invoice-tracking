import unittest

import msgpack

import falcon
from falcon import testing

from src.main import api

class RoutesTest(unittest.TestCase):

    def test_getInvoices(self):
        invoices = [{
            'employee': '1',
            'description': 'Lunch',
            'amount': 30.00
        }]
        client = testing.TestClient(api)
        response = client.simulate_get("/invoices")
        result_invoices = response.json
        self.assertEqual(result_invoices, invoices)
        self.assertEqual(response.status, falcon.HTTP_OK)
