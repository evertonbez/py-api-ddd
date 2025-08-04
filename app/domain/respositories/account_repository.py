from abc import ABC, abstractmethod

from app.domain.entities.account import Account


class AccountRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: str) -> Account | None:
        raise NotImplementedError
