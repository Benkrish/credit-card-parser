import re
from .base_parser import BaseParser

class BofAParser(BaseParser):
    """Parses Bank of America statements."""

    def get_issuer(self):
        return 'Bank of America'

    def get_last_4_digits(self):
        flags = re.IGNORECASE
        match = re.search(r'Account #[:\s]*\d{4}-\d{4}-\d{4}-(\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_due_date(self):
        flags = re.IGNORECASE | re.DOTALL
        match = re.search(r'Payment Due[:\s]*(\d{1,2}/\d{1,2}/\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_total_balance(self):
        flags = re.IGNORECASE
        match = re.search(r'Total Balance Due[:\s]*\$([\d,]+\.\d{2})', self.text, flags)
        if match:
            return match.group(1).replace(',', '')
        return None

    def get_card_variant(self):
        flags = re.IGNORECASE
        match = re.search(r'Card[:\s]*(Bank of America.+)', self.text, flags)
        if match:
            return match.group(1).strip().replace('®', '')
        return 'BofA Card' # Default