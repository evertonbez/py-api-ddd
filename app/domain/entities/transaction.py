from dataclasses import dataclass

from app.domain.entities._base import BaseEntity


@dataclass
class Transaction(BaseEntity):
    account_id: str
    amount: float
    mcc: str
    merchant: str
    used_category: str
