from typing import List, Dict

from src.model.invoice import Invoice

def convert_invoices_to_dicts(invoices: List[Invoice]) -> List[Dict]:
    return list(map(lambda invoice: invoice.to_dict(), invoices))
