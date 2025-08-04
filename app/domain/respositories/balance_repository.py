from abc import ABC, abstractmethod
from ast import List

from app.domain.entities.balance import Balance


class BalanceRepository(ABC):

    @abstractmethod
    def get_all_by_account_id(self, account_id: str) -> List[Balance] | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_account_id_and_category(
        self, account_id: str, category: str
    ) -> Balance | None:
        raise NotImplementedError

    @abstractmethod
    def update_balance(self, balance: Balance) -> None:
        raise NotImplementedError
