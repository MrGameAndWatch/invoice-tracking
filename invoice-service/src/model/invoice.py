from typing import Dict

from datetime import datetime
from uuid import uuid4, UUID

from src.model.constants import time_format

class Invoice:

    def __init__(self, user_id: str, description: str, amount: float=0.0, id: UUID=None, timestamp: datetime=None):
        self._id = id if id is not None else uuid4()
        self._user_id = user_id
        self._description = description
        self._amount = amount
        self._timestamp = timestamp if timestamp is not None else datetime.now()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def description(self) -> str:
        return self._description

    @property
    def amount(self) -> float:
        return self._amount

    def to_dict(self) -> Dict:
        return {
            '_id': str(self.id),
            'userId': str(self.user_id),
            'description': self.description,
            'amount': self.amount,
            'timestamp': self._timestamp.strftime(time_format)
        }

class InvoiceBuilder:

    def __init__(self):
        self._id = None
        self._user_id = ''
        self._description = ''
        self._amount = 0.0
        self._timestamp = None

    def id(self, id: UUID) -> 'InvoiceBuilder':
        self._id = id
        return self

    def user_id(self, user_id: str) -> 'InvoiceBuilder':
        self._user_id = user_id
        return self

    def description(self, description: str) -> 'InvoiceBuilder':
        self._description = description
        return self

    def amount(self, amount: float) -> 'InvoiceBuilder':
        self._amount = amount
        return self

    def timestamp(self, timestamp: datetime) -> 'InvoiceBuilder':
        self._timestamp = timestamp
        return self

    def build(self) -> Invoice:
        return Invoice(self._user_id, self._description, amount=self._amount, id=self._id, timestamp=self._timestamp)
