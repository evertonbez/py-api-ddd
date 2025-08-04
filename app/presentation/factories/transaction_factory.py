from app.application.usecases.create_transaction import CreateTransactionUsecase
from app.domain.repositories.account_repository import AccountRepository
from app.domain.repositories.balance_repository import BalanceRepository
from app.domain.repositories.mcc_category_repository import MccCategoryRepository
from app.domain.repositories.merchant_mapping_repository import (
    MerchantMappingsRepository,
)
from app.domain.repositories.transaction_repository import TransactionRepository


def create_transaction_factory() -> CreateTransactionUsecase:
    mcc_category_repository = MccCategoryRepository()
    account_repository = AccountRepository()
    balance_repository = BalanceRepository()
    transaction_repository = TransactionRepository()
    merchant_mappings_repository = MerchantMappingsRepository()

    return CreateTransactionUsecase(
        mcc_category_repository=mcc_category_repository,
        account_repository=account_repository,
        balance_repository=balance_repository,
        transaction_repository=transaction_repository,
        merchant_mappings_repository=merchant_mappings_repository,
    )
