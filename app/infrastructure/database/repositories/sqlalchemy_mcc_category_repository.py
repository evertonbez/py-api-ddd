from abc import ABC, abstractmethod

from sqlalchemy import select

from app.domain.entities.mcc_category import MccCategory
from app.domain.repositories.mcc_category_repository import MccCategoryRepository
from app.infrastructure.database.mappers import mcc_categories_to_entity
from app.infrastructure.database.models import MccCategoriesModel
from app.infrastructure.database.session import SessionLocal


class SqlAlchemyMccCategoryRepository(MccCategoryRepository):
    def get_by_mcc(self, mcc: str) -> MccCategory | None:
        with SessionLocal() as session:
            stmt = select(MccCategoriesModel).where(MccCategoriesModel.mcc == mcc)
            result = session.scalars(stmt).first()

            return mcc_categories_to_entity(result) if result else None
