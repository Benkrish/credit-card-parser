from abc import ABC, abstractmethod

class BaseParser(ABC):

    
    def __init__(self, pdf_text):
        self.text = pdf_text
        self.data = {}


    @abstractmethod
    def get_issuer(self):
        """Extracts the card issuer (e.g., 'Chase')."""
        pass

    @abstractmethod
    def get_last_4_digits(self):
        """Extracts the last 4 digits of the card number."""
        pass

    @abstractmethod
    def get_due_date(self):
        """Extracts the payment due date."""
        pass

    @abstractmethod
    def get_total_balance(self):
        """Extracts the total balance due."""
        pass

    @abstractmethod
    def get_card_variant(self):
        """Extracts the card variant (e.g., 'Sapphire Preferred')."""
        pass

    # --- This "parse" method runs the whole process ---

    def parse(self):
        """
        Public method to run all extraction methods and return
        the consolidated data.
        """
        try:
            self.data['issuer'] = self.get_issuer()
            self.data['last_4_digits'] = self.get_last_4_digits()
            self.data['due_date'] = self.get_due_date()
            self.data['total_balance'] = self.get_total_balance()
            self.data['card_variant'] = self.get_card_variant()
        except Exception as e:
            print(f"Error during parsing: {e}")
            return None
        
        return self.data