from app.domain.contracts.usecase import InputData, Usecase
from app.domain.entities.transaction import Transaction
from app.domain.entities.balance import Balance
from app.domain.entities.mcc_category import MccCategory
from app.domain.repositories.account_repository import AccountRepository
from app.domain.repositories.balance_repository import BalanceRepository
from app.domain.repositories.mcc_category_repository import MccCategoryRepository
from app.domain.repositories.merchant_mapping_repository import (
    MerchantMappingsRepository,
)
from app.domain.repositories.transaction_repository import TransactionRepository


class CreateTransactionRequest(InputData):
    account_id: str
    amount: float
    mcc: str
    merchant: str


class CreateTransactionResponse(InputData):
    code: str
    message: str


class CreateTransactionUsecase(Usecase):

    def __init__(
        self,
        account_repository: AccountRepository,
        balance_repository: BalanceRepository,
        transaction_repository: TransactionRepository,
        mcc_category_repository: MccCategoryRepository,
        merchant_mappings_repository: MerchantMappingsRepository,
    ) -> None:
        super().__init__()
        self.account_repository = account_repository
        self.balance_repository = balance_repository
        self.transaction_repository = transaction_repository
        self.mcc_category_repository = mcc_category_repository
        self.merchant_mappings_repository = merchant_mappings_repository

    def execute(self, request: CreateTransactionRequest) -> CreateTransactionResponse:
        account = self.account_repository.get_by_id(request.account_id)
        if not account:
            return CreateTransactionResponse(code="07", message="Conta não encontrada")

        effective_mcc = self._get_effective_mcc(request.mcc, request.merchant)

        mcc_category = self.mcc_categories_repository.get_by_mcc(effective_mcc)

        if not mcc_category:
            mcc_category = MccCategory(
                mcc=effective_mcc,
                category="CASH",
            )

        balance = self.balance_repository.get_by_account_id_and_category(
            request.account_id, mcc_category.category
        )

        if not balance:
            balance = Balance(
                account_id=account.id,
                category=mcc_category.category,
                amount=0,
            )

        if request.amount <= balance.amount:
            balance.debit_amount(request.amount)
            self.balance_repository.update_balance(balance)

            transaction = Transaction(
                account_id=request.account_id,
                amount=request.amount,
                mcc=effective_mcc,
                merchant=request.merchant,
                used_category=mcc_category.category,
            )

            self.transaction_repository.save(transaction)

            return CreateTransactionResponse(code="00", message="Transação aprovada")

        return CreateTransactionResponse(code="51", message="Saldo insuficiente")

    def _get_effective_mcc(self, original_mcc: str, merchant: str) -> str:
        merchant_mapping = self.merchant_mappings_repository.get_by_merchant_pattern(
            merchant
        )

        if merchant_mapping:
            return merchant_mapping.override_mcc

        return original_mcc
