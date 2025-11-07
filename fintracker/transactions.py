from typing import List

from .models import Transaction

class TransactionManager:
    """Manage a list of financial transactions."""

    def __init__(self) -> None:
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the list."""
        self.transactions.append(transaction)

    def list_transactions(self) -> List[Transaction]:
        """Return the list of stored transactions."""
        return self.transactions
