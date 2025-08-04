from abc import ABC, abstractmethod
from datetime import datetime

from app.domain.entities.transaction import Transaction
from app.domain.repositories.transaction_repository import TransactionRepository
from app.infrastructure.database.models import TransactionModel
from app.infrastructure.database.session import SessionLocal


class SqlAlchemyTransactionRepository(TransactionRepository):
    def save(self, transaction: Transaction) -> None:
        with SessionLocal() as session:
            db_transaction = TransactionModel(
                id=transaction.id,
                account_id=transaction.account_id,
                amount=transaction.amount,
                mcc=transaction.mcc,
                merchant=transaction.merchant,
                used_category=transaction.used_category,
                created_at=transaction.created_at or datetime.now(),
            )
            session.add(db_transaction)
            session.commit()
