from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)


class BalanceModel(Base):
    __tablename__ = "balances"

    id = Column(Integer, primary_key=True)
    account_id = Column(String, ForeignKey("accounts.id"), nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime, nullable=False)


class MccCategoriesModel(Base):
    __tablename__ = "mcc_categories"

    id = Column(Integer, primary_key=True)
    mcc = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)


class MerchantMappingsModel(Base):
    __tablename__ = "merchant_mappings"

    id = Column(Integer, primary_key=True)
    pattern = Column(String, nullable=False, unique=True)
    override_mcc = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)


class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account_id = Column(String, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    mcc = Column(String, nullable=False)
    merchant = Column(String, nullable=True)
    used_category = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
