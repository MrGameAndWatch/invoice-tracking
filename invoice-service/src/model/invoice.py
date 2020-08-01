from typing import Dict

import uuid


class Invoice:

    def __init__(self, description: str, amount: float=0.0):
        self._id = uuid.uuid4()
        self._description = description
        self._amount = amount

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @property
    def amount(self) -> float:
        return self._amount

    def to_dict(self) -> Dict:
        return {
            'id': str(self.id),
            'description': self.description,
            'amount': self.amount
        }



class InvoiceBuilder:

    def __init__(self):
        self._description = ''
        self._amount = 0.0

    def description(self, description: str) -> 'InvoiceBuilder':
        self._description = description
        return self

    def amount(self, amount: float) -> 'InvoiceBuilder':
        self._amount = amount
        return self

    def build(self) -> Invoice:
        return Invoice(self._description, amount=self._amount)
