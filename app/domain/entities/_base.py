from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(kw_only=True)
class BaseEntity:
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
