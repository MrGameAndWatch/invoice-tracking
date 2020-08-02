from pymongo.collection import Collection

from src.model.invoice import Invoice, InvoiceBuilder

class InvoiceRepository:

    def __init__(self, collection: Collection):
        self.collection = collection

    def save(self, invoice: Invoice) -> str:
        res = self.collection.insert_one(invoice.to_dict())
        return res.inserted_id
