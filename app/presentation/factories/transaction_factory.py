from app.application.usecases.create_transaction import CreateTransactionUsecase
from app.domain.repositories.merchant_mapping_repository import (
    MerchantMappingsRepository,
)
from app.domain.repositories.transaction_repository import TransactionRepository
from app.infrastructure.database.repositories.sqlalchemy_account_repository import (
    SqlAlchemyAccountRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_balance_repository import (
    SqlAlchemyBalanceRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_mcc_category_repository import (
    SqlAlchemyMccCategoryRepository,
)


def create_transaction_factory() -> CreateTransactionUsecase:
    mcc_category_repository = SqlAlchemyMccCategoryRepository()
    account_repository = SqlAlchemyAccountRepository()
    balance_repository = SqlAlchemyBalanceRepository()
    transaction_repository = TransactionRepository()
    merchant_mappings_repository = MerchantMappingsRepository()

    return CreateTransactionUsecase(
        mcc_category_repository=mcc_category_repository,
        account_repository=account_repository,
        balance_repository=balance_repository,
        transaction_repository=transaction_repository,
        merchant_mappings_repository=merchant_mappings_repository,
    )
