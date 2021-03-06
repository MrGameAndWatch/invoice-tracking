from uuid import UUID
from datetime import datetime

from src.model.constants import time_format
from src.model.invoice import Invoice, InvoiceBuilder

def convert(raw) -> Invoice:
    return InvoiceBuilder() \
        .id(UUID(raw['_id'])) \
        .user_id(raw['userId']) \
        .description(raw['description']) \
        .amount(float(raw['amount'])) \
        .timestamp(datetime.strptime(raw['timestamp'], time_format)) \
        .build() if raw is not None else None
