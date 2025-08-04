from abc import ABC, abstractmethod

from app.domain.entities.mcc_category import MccCategory


class MccCategoryRepository(ABC):
    @abstractmethod
    def get_by_mcc(self, mcc: str) -> MccCategory | None:
        raise NotImplementedError
