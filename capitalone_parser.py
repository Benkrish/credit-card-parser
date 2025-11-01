import re
from .base_parser import BaseParser

class CapitalOneParser(BaseParser):

    def get_issuer(self):
        return 'Capital One'

    def get_last_4_digits(self):
        flags = re.IGNORECASE
        match = re.search(r'Number[:\s]*\.\.\.\s*(\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_due_date(self):
        flags = re.IGNORECASE | re.DOTALL
        match = re.search(r'Payment Due Date[:\s]*(\d{1,2}/\d{1,2}/\d{4})', self.text, flags)
        return match.group(1) if match else None

    def get_total_balance(self):
        flags = re.IGNORECASE
        match = re.search(r'New Balance[:\s]*\$([\d,]+\.\d{2})', self.text, flags)
        if match:
            return match.group(1).replace(',', '')
        return None

    def get_card_variant(self):
        flags = re.IGNORECASE
        match = re.search(r'Account[:\s]*(Quicksilver)', self.text, flags)
        if match:
            return match.group(1).strip()
        return 'Capital One Card'