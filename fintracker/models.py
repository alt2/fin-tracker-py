from dataclasses import dataclass

@dataclass
class Transaction:
    """Represents a financial transaction."""
    date: str
    description: str
    amount: float
    category: str
