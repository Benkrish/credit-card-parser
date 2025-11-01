import re  
from .base_parser import BaseParser

class ChaseParser(BaseParser):
    def get_issuer(self):
        return 'Chase'

    def get_last_4_digits(self):
        flags = re.IGNORECASE
        match = re.search(r'(ending in|Account Number|Card Number)[\s:.-]*(\d{4})', self.text, flags)
        if match:
            return match.group(2)
        match = re.search(r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?(\d{4})', self.text)
        if match:
            return match.group(1)
        return None 

    def get_due_date(self):
        flags = re.DOTALL | re.IGNORECASE
        
        # Regex to find:
        # 1. MM/DD/YYYY (e.g., 11/25/2025)
        # 2. Month Day, Year (e.g., Nov 25, 2025)
        date_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}|\S+\s+\d+,\s+\d{4})'
        
        match = re.search(r'(Payment Due Date|Due Date).*?' + date_pattern, self.text, flags)
        
        if match:
            return match.group(2).strip()
        
        # --- FALLBACK ---
        # If the first one fails, let's try another common format like DD-MMM-YYYY
        date_pattern_2 = r'(\d{1,2}-\S{3}-\d{2,4})'
        match = re.search(r'(Payment Due Date|Due Date).*?' + date_pattern_2, self.text, flags)
        if match:
            return match.group(2).strip()
        return None
    def get_total_balance(self):
        match = re.search(r'New Balance.*?\s+([$\d,]+\.\d{2})', self.text)
        if match:
            balance_str = match.group(1).replace('$', '').replace(',', '')
            return balance_str
        return None 

    def get_card_variant(self):
    
        flags = re.IGNORECASE

        if re.search(r'Sapphire Preferred', self.text, flags):
            return 'Sapphire Preferred'
        if re.search(r'Sapphire Reserve', self.text, flags):
            return 'Sapphire Reserve'
        if re.search(r'Freedom Unlimited', self.text, flags):
            return 'Freedom Unlimited'
        if re.search(r'Freedom Flex', self.text, flags):
            return 'Freedom Flex'
        return 'Chase Card'