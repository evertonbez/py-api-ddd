from app.domain.contracts.usecase import InputData, Usecase
from app.domain.respositories.account_repository import AccountRepository
from app.domain.respositories.balance_repository import BalanceRepository
from app.domain.respositories.transaction_repository import TransactionRepository


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
    ) -> None:
        super().__init__()
        self.account_repository = account_repository
        self.balance_repository = balance_repository
        self.transaction_repository = transaction_repository

    def execute(self, request: CreateTransactionRequest) -> CreateTransactionResponse:
        account = self.account_repository.get_by_id(request.account_id)
        if not account:
            return CreateTransactionResponse(code="07", message="Conta não encontrada")

        balance = self.balance_repository.get_by_account_id_and_category(
            request.account_id, request.mcc
        )

        return CreateTransactionResponse(code="51", message="Saldo insuficiente")
