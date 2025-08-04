from dataclasses import dataclass

from app.domain.entities._base import BaseEntity


@dataclass
class MccCategory(BaseEntity):
    mcc: str
    category: str
