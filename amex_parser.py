import re
from .base_parser import BaseParser

class AmexParser(BaseParser):
    def get_issuer(self):
        return 'American Express'

    def get_last_4_digits(self):
        flags = re.IGNORECASE
        match = re.search(r'Account Ending In[:\s]*(\d{4})', self.text, flags)
        if match:
            return match.group(1)
        return None

    def get_due_date(self):
       
        flags = re.IGNORECASE
        match = re.search(r'Payment Due Date[:\s]*(\S+\s+\d+,\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})', self.text, flags)
        if match:
            return match.group(1).strip()
        return None

    def get_total_balance(self):
  
        flags = re.IGNORECASE
        match = re.search(r'Total Balance[:\s]*\$([\d,]+\.\d{2})', self.text, flags)
        if match:
            balance_str = match.group(1).replace(',', '')
            return balance_str
        
        return None 

    def get_card_variant(self):
       
        flags = re.IGNORECASE
        match = re.search(r'Card[:\s]*(.*)', self.text, flags)
        if match:
            card_name = match.group(1).strip().replace('®', '')
            return card_name
        return None