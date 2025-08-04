from abc import ABC, abstractmethod

from app.domain.entities.merchant_mapping import MerchantMapping


class MerchantMappingsRepository(ABC):
    @abstractmethod
    def get_by_merchant_pattern(self, merchant: str) -> MerchantMapping | None:
        raise NotImplementedError
