from sqlalchemy import select
from app.domain.entities.merchant_mapping import MerchantMapping
from app.domain.repositories.merchant_mapping_repository import (
    MerchantMappingsRepository,
)
from app.infrastructure.database.mappers import merchant_mapping_to_entity
from app.infrastructure.database.models import MerchantMappingsModel
from app.infrastructure.database.session import SessionLocal


class SqlAlchemyMerchantMappingsRepository(MerchantMappingsRepository):
    def get_by_merchant_pattern(self, merchant: str) -> MerchantMapping | None:
        with SessionLocal() as session:
            stmt = select(MerchantMappingsModel).where(
                MerchantMappingsModel.pattern == merchant
            )
            result = session.scalars(stmt).first()

            return merchant_mapping_to_entity(result) if result else None
