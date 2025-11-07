import csv
from typing import List

from .models import Transaction


def load_transactions(csv_path: str) -> List[Transaction]:
    """Load transactions from a CSV file and return a list of Transaction objects."""
    transactions: List[Transaction] = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(
                Transaction(
                    date=row['date'],
                    description=row['description'],
                    amount=float(row['amount']),
                    category=row['category'],
                )
            )
    return transactions
