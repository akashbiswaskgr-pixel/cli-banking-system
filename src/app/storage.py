#storage.py
import json
import os

from src.app.models import Account, Transaction
from src.config import ACC_DATA, TXN_DATA


def ensure_files():
    """Ensure data/accounts.json and data/transactions.json are present in the directory."""
    os.makedirs("data", exist_ok=True)

    for path in (ACC_DATA, TXN_DATA):
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            with open(path, "w") as file:
                json.dump([], file, indent=4)


def load_accounts() -> list[Account]:
    """Load every account detail from data/accounts.json into a Python-supported data type."""
    if not os.path.exists(ACC_DATA) or os.path.getsize(ACC_DATA) == 0:
        return []

    with open(ACC_DATA, "r") as f:
        result = json.load(f)

    return [Account.from_dict(data) for data in result]


def save_accounts(accounts: list[Account]):
    """Save account details into data/accounts.json."""
    ensure_files()

    with open(ACC_DATA, "w") as f:
        json.dump([a.to_dict() for a in accounts], f, indent=4)


def save_transaction(txn: Transaction):
    """Save transaction details into data/transactions.json."""
    ensure_files()

    with open(TXN_DATA, "r") as f:
        data = json.load(f) if os.path.getsize(TXN_DATA) > 0 else []

    data.append(txn.to_dict())

    with open(TXN_DATA, "w") as f:
        json.dump(data, f, indent=4)