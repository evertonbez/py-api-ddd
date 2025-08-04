from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(kw_only=True)
class BaseEntity:
    id: Optional[int] = None
    created_at: Optional[datetime] = None
