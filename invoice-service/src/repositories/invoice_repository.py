from typing import List

from pymongo.collection import Collection

from src.model.invoice import Invoice, InvoiceBuilder
from src.repositories.converters import invoice_converter

class InvoiceRepository:

    def __init__(self, collection: Collection):
        self.collection = collection

    def save(self, invoice: Invoice) -> str:
        res = self.collection.insert_one(invoice.to_dict())
        return res.inserted_id

    def save_all(self, invoices: List[Invoice]) -> List[str]:
        new_invoices = list(map(lambda invoice: invoice.to_dict(), invoices))
        res = self.collection.insert_many(new_invoices)
        return res.inserted_ids

    def find_all(self) -> List[Invoice]:
        found_invoices = self.collection.find()
        return self._get_converted(found_invoices)

    def find_by_id(self, id: str) -> Invoice:
        found_raw_invoice = self.collection.find_one({"_id": id})
        return invoice_converter.convert(found_raw_invoice)

    def find_by_userId(self, userId: str) -> List[Invoice]:
        found_invoices = self.collection.find({"userId": userId})
        return self._get_converted(found_invoices)

    def _get_converted(self, raw_invoices: List) -> List[Invoice]:
        return list(map(lambda raw_invoice: invoice_converter.convert(raw_invoice), raw_invoices))
