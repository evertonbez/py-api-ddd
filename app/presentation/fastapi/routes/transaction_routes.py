from fastapi import APIRouter

from app.application.usecases.create_transaction import (
    CreateTransactionRequest,
    CreateTransactionResponse,
)
from app.presentation.factories.transaction_factory import create_transaction_factory


router = APIRouter()


@router.post("/transactions")
async def create_transaction(request: dict):
    try:
        return create_transaction_factory().execute(CreateTransactionRequest(**request))
    except Exception as e:
        print(e)
        return CreateTransactionResponse(code="07", message="Erro interno")
