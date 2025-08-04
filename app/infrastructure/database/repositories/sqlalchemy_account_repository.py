from abc import ABC, abstractmethod

from sqlalchemy import select

from app.domain.entities.account import Account
from app.domain.repositories.account_repository import AccountRepository
from app.infrastructure.database.mappers import account_to_entity
from app.infrastructure.database.models import AccountModel
from app.infrastructure.database.session import SessionLocal


class SqlAlchemyAccountRepository(AccountRepository):
    def get_by_id(self, id: str) -> Account | None:
        with SessionLocal() as session:
            stmt = select(AccountModel).where(AccountModel.id == id)
            result = session.scalars(stmt).first()

            return account_to_entity(result) if result else None
