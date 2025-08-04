from app.domain.entities.balance import Balance
from app.domain.entities.mcc_category import MccCategory
from app.domain.entities.merchant_mapping import MerchantMapping
from app.infrastructure.database.models import (
    AccountModel,
    BalanceModel,
    MccCategoriesModel,
    MerchantMappingsModel,
)
from app.domain.entities.account import Account


def account_to_entity(orm: AccountModel) -> Account:
    return Account(id=orm.id, created_at=orm.created_at)


def entity_to_account(entity: Account) -> AccountModel:
    return AccountModel(id=entity.id, created_at=entity.created_at)


def balance_to_entity(orm: BalanceModel) -> Balance:
    return Balance(
        id=orm.id,
        account_id=orm.account_id,
        category=orm.category,
        amount=orm.amount,
        created_at=orm.created_at,
    )


def entity_to_balance(entity: Balance) -> BalanceModel:
    return BalanceModel(
        id=entity.id,
        account_id=entity.account_id,
        category=entity.category,
        amount=entity.amount,
        created_at=entity.created_at,
    )


def mcc_categories_to_entity(orm: MccCategoriesModel) -> MccCategory:
    return MccCategory(
        id=orm.id, mcc=orm.mcc, category=orm.category, created_at=orm.created_at
    )


def merchant_mapping_to_entity(orm: MerchantMappingsModel) -> MerchantMapping:
    return MerchantMapping(
        id=orm.id,
        pattern=orm.pattern,
        override_mcc=orm.override_mcc,
        created_at=orm.created_at,
    )
