from abc import ABC, abstractmethod

from app.domain.entities.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        raise NotImplementedError
