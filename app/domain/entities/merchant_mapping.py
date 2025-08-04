from dataclasses import dataclass

from app.domain.entities._base import BaseEntity


@dataclass
class MerchantMapping(BaseEntity):
    pattern: str
    override_mcc: str
