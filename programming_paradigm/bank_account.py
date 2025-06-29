class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        self._account_balance += amount

    def withdraw(self, amount):
        """Deduct amount if sufficient funds; return True if successful."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self._account_balance:.2f}")
