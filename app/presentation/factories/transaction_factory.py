from app.application.usecases.create_transaction_usecase import (
    CreateTransactionUsecase,
)
from app.infrastructure.database.repositories.sqlalchemy_account_repository import (
    SqlAlchemyAccountRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_balance_repository import (
    SqlAlchemyBalanceRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_mcc_category_repository import (
    SqlAlchemyMccCategoryRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_merchant_mapping_repository import (
    SqlAlchemyMerchantMappingsRepository,
)
from app.infrastructure.database.repositories.sqlalchemy_transaction_repository import (
    SqlAlchemyTransactionRepository,
)


def create_transaction_factory() -> CreateTransactionUsecase:
    mcc_category_repository = SqlAlchemyMccCategoryRepository()
    account_repository = SqlAlchemyAccountRepository()
    balance_repository = SqlAlchemyBalanceRepository()
    merchant_mappings_repository = SqlAlchemyMerchantMappingsRepository()
    transaction_repository = SqlAlchemyTransactionRepository()

    return CreateTransactionUsecase(
        mcc_category_repository=mcc_category_repository,
        account_repository=account_repository,
        balance_repository=balance_repository,
        transaction_repository=transaction_repository,
        merchant_mappings_repository=merchant_mappings_repository,
    )
