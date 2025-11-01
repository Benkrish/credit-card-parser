import re
from .base_parser import BaseParser

class CitiParser(BaseParser):
    """Parses Citi statements."""

    def get_issuer(self):
        return 'Citi'

    def get_last_4_digits(self):
        flags = re.IGNORECASE
        match = re.search(r'Account Number ending (\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_due_date(self):
        flags = re.IGNORECASE | re.DOTALL
        match = re.search(r'Payment Due Date[:\s]*(\d{1,2}-\S{3}-\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_total_balance(self):
        flags = re.IGNORECASE
        match = re.search(r'New Balance[:\s]*([\d,]+\.\d{2})', self.text, flags)
        if match:
            return match.group(1).replace(',', '')
        return None

    def get_card_variant(self):
        flags = re.IGNORECASE
        match = re.search(r'Card[:\s]*(Citi.+)', self.text, flags)
        if match:
            return match.group(1).strip().replace('®', '')
        
        match = re.search(r'(Citi.+Card)', self.text, flags)
        if match:
            return match.group(1).strip().replace('®', '')
            
        return 'Citi Card' 