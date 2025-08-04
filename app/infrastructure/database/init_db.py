from datetime import datetime
from app.infrastructure.database.models import (
    AccountModel,
    BalanceModel,
    Base,
    MccCategoriesModel,
    MerchantMappingsModel,
)
from app.infrastructure.database.session import SessionLocal, engine

import app.infrastructure.database.models


def seed_db():
    with SessionLocal(bind=engine) as session:

        contas = [
            AccountModel(id=1, created_at=datetime.now()),
            AccountModel(id=2, created_at=datetime.now()),
        ]

        session.add_all(contas)

        balances = []
        categories = ["CASH", "FOOD", "MEAL"]
        amounts = {
            1: [150.0, 200.0, 250.0],  # valores para account 1
            2: [120.0, 180.0, 300.0],  # valores para account 2
        }

        for acc_id in [1, 2]:
            for cat, amt in zip(categories, amounts[acc_id]):
                balances.append(
                    BalanceModel(
                        account_id=str(acc_id),
                        category=cat,
                        amount=amt,
                        created_at=datetime.now(),
                    )
                )

        session.add_all(balances)

        merchant_mappings = [
            MerchantMappingsModel(
                id=1,
                pattern="UBER TRIP SAO PAULO BR",
                override_mcc="5999",
                created_at=datetime.now(),
            ),
            MerchantMappingsModel(
                id=2,
                pattern="UBER EATS SAO PAULO BR",
                override_mcc="5811",
                created_at=datetime.now(),
            ),
            MerchantMappingsModel(
                id=3,
                pattern="PAG*JoseDaSilva RIO DE JANEI BR",
                override_mcc="5999",
                created_at=datetime.now(),
            ),
            MerchantMappingsModel(
                id=4,
                pattern="PICPAY*BILHETEUNICO GOIANIA BR",
                override_mcc="5999",
                created_at=datetime.now(),
            ),
        ]

        session.add_all(merchant_mappings)

        mcc_categories = [
            MccCategoriesModel(
                mcc="5811",
                category="MEAL",
                created_at=datetime.now(),
            ),
            MccCategoriesModel(
                mcc="5812",
                category="MEAL",
                created_at=datetime.now(),
            ),
            MccCategoriesModel(
                mcc="5412",
                category="FOOD",
                created_at=datetime.now(),
            ),
            MccCategoriesModel(
                mcc="5411",
                category="FOOD",
                created_at=datetime.now(),
            ),
            MccCategoriesModel(
                mcc="5999",
                category="CASH",
                created_at=datetime.now(),
            ),
        ]

        session.add_all(mcc_categories)

        session.commit()
        print("Seed de AccountModel concluída.")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    seed_db()
