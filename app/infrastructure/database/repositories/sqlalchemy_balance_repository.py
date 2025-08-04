from typing import List

from sqlalchemy import select, update
from app.domain.entities.balance import Balance
from app.domain.repositories.balance_repository import BalanceRepository
from app.infrastructure.database.mappers import balance_to_entity
from app.infrastructure.database.models import BalanceModel
from app.infrastructure.database.session import SessionLocal


class SqlAlchemyBalanceRepository(BalanceRepository):
    def get_all_by_account_id(self, account_id: str) -> List[Balance]:
        with SessionLocal() as session:
            stmt = select(BalanceModel).where(BalanceModel.account_id == account_id)
            results = session.scalars(stmt).all()

            return [balance_to_entity(b) for b in results]

    def get_by_account_id_and_category(
        self, account_id: str, category: str
    ) -> Balance | None:
        with SessionLocal() as session:
            stmt = select(BalanceModel).where(
                BalanceModel.account_id == account_id,
                BalanceModel.category == category,
            )
            result = session.scalars(stmt).first()

            return balance_to_entity(result) if result else None

    def update_balance(self, balance: Balance) -> None:
        with SessionLocal() as session:
            stmt = (
                update(BalanceModel)
                .where(
                    BalanceModel.account_id == balance.account_id,
                    BalanceModel.category == balance.category,
                )
                .values(
                    amount=balance.amount,
                    updated_at=balance.updated_at,
                )
            )
            session.execute(stmt)
            session.commit()
