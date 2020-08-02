import json
import unittest
import mongomock

import falcon
from falcon import testing

from src.util import utils
from test.invoice_data import invoices, invoices_for_one_user
from src.model.constants import errors

from src.main import create_context

class RoutesTest(unittest.TestCase):

    def setUp(self):
        mock_client = mongomock.MongoClient().db
        self.context = create_context(mock_client)
        self.context \
            .get('repositories') \
            .get('InvoiceRepository') \
            .save_all(invoices)
        self.client = testing.TestClient(self.context.get('api'))

    def test_getInvoices(self):
        exptected_invoices = utils.convert_invoices_to_dicts(invoices)
        response = self.client.simulate_get("/invoices")
        result_invoices = response.json
        self.assertEqual(result_invoices, exptected_invoices)
        self.assertEqual(response.status, falcon.HTTP_OK)

    def test_getKnownInvoiceById(self):
        expected_invoice = invoices.__getitem__(0)
        known_id = expected_invoice.id
        response = self.client.simulate_get(f'/invoices/{known_id}')
        result_invoice = response.json
        self.assertEqual(result_invoice, expected_invoice.to_dict())
        self.assertEqual(response.status, falcon.HTTP_OK)

    def test_getUnknownInvoiceById(self):
        response = self.client.simulate_get('/invoices/unknown-id')
        result_invoice = response.json
        self.assertEqual(result_invoice, {})
        self.assertEqual(response.status, falcon.HTTP_NOT_FOUND)

    def test_getInvoicesByUserId(self):
        self.context \
            .get('repositories') \
            .get('InvoiceRepository') \
            .save_all(invoices_for_one_user)
        expected_invoices = utils.convert_invoices_to_dicts(invoices_for_one_user)
        user_id = invoices_for_one_user.__getitem__(0).user_id
        response = self.client.simulate_get(f'/users/{user_id}/invoices')
        result_invoices = response.json
        self.assertEqual(result_invoices, expected_invoices)

    def test_postNewCorrectInvoice(self):
        new_invoice = {
            "description": "Brand new invoice",
            "amount": 542.43
        }
        json_data = json.dumps(new_invoice)
        user_id = "UserXYZ"
        response = self.client.simulate_post(f'/users/{user_id}/invoices', body=json_data)
        response_data = response.json
        self.assertEqual(response.status, falcon.HTTP_CREATED)
        self.assertIsNotNone(response_data)
        stored_invoice = self.context \
            .get('repositories') \
            .get('InvoiceRepository') \
            .find_by_id(response_data['invoiceId'])
        self.assertEqual(stored_invoice.description, new_invoice['description'])
        self.assertEqual(stored_invoice.amount, new_invoice['amount'])

    def test_postNewIncorrectInvoice(self):
        new_invoice = {
            "amount": 584.43
        }
        json_data = json.dumps(new_invoice)
        user_id = "User"
        response = self.client.simulate_post(f'/users/{user_id}/invoices', body=json.dumps(new_invoice))
        error = response.json
        self.assertEqual(error, { 'errorMsg': errors.get('wrongInvoiceFormat') })
