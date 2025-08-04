from dataclasses import dataclass

from app.domain.entities._base import BaseEntity


@dataclass
class Balance(BaseEntity):
    account_id: str
    category: str
    amount: float

    def debit_amount(self, amount: float):
        if amount > self.amount:
            raise ValueError("Insufficient funds")
        self.amount -= amount
