import datetime
from typing import Literal, Union

from src.app.errors import InvalidAmount
from src.app.utils import generate_id


class Account:
    def __init__(self, _id: int, name: str, balance: float = 0):
        self._id = _id
        self.name = name
        self.__balance = balance

    def __str__(self):
        return f"ACC_ID : {self._id}, Name: {self.name}, Balance: {self.__balance}"

    @property
    def balance(self):
        return self.__balance

    def deposit(self, value: float) -> float:
        if value <= 0:
            raise InvalidAmount("Amount must be greater than 0")
        self.__balance += value
        return self.__balance

    def withdraw(self, value: float) -> float:
        if value <= 0:
            raise InvalidAmount("Amount must be greater than 0")

        if value > self.__balance:
            raise InvalidAmount(f"Your entered amount must be within your balance {self.__balance}")

        self.__balance -= value
        return self.__balance

    def to_dict(self) -> dict[str, str | float]:
        return {
            "id": self._id,
            "name": self.name,
            "balance": self.__balance,
        }

    @classmethod
    def from_dict(cls, data: dict[str, str | float]):
        return cls(data["id"], data["name"], data["balance"])


class Transaction:
    def __init__(
        self,
        txn_type: Literal["deposit", "withdraw", "transfer"],
        amount: float,
        source_id: str,
        target_id: Union[str, None] = None,
    ):
        self._id = generate_id()
        self.txn_type = txn_type
        self.amount = amount
        self.source_id = source_id
        self.target_id = target_id
        self.timestamp = datetime.datetime.now().isoformat()

    def to_dict(self) -> dict[str, Union[str, float, None]]:
        return {
            "id": self._id,
            "txn_type": self.txn_type,
            "amount": self.amount,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "timestamp": self.timestamp,
        }