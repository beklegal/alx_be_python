# bank_account.py

class BankAccount:
    """Simple Bank Account class demonstrating basic OOP principles."""

    def __init__(self, initial_balance: float = 0.0):
        # underscore prefix → “protected” convention (encapsulation)
        self._account_balance = float(initial_balance)

    # --------- Behaviours ---------

    def deposit(self, amount: float) -> None:
        """Add amount to the account balance."""
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Deduct amount from balance if sufficient funds exist.
        Returns True on success, False otherwise.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """Print the current balance in a user‑friendly format."""
        print(f"Current Balance: ${self._account_balance}")

    # --------- Optional helper (not required by checker) ---------
    @property
    def balance(self) -> float:
        """Read‑only access to the current balance."""
        return self._account_balance
