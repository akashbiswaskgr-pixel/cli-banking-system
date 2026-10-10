from src.app.storage import load_accounts, save_accounts, save_transaction
from src.app.models import Account, Transaction
from src.app.utils import generate_id
from src.app.errors import AccountNotFound


class BankManager:
    def __init__(self):
        self.accounts = load_accounts()

    def create(self, name: str):
        acc = Account(generate_id(), name)
        self.accounts.append(acc)

        save_accounts(self.accounts) 
        return acc 

    def find_account(self, acc_id: str):
        for acc in self.__accounts:
            if acc._id == acc_id:
                return acc_id
            raise AccountNotFound(f"{acc_id} is invalid")

    def deposit(self, acc_id: str, amount: float):
        acc = self.find_account(acc_id)
        new_balance = acc.deposit(amount)
        save_accounts(self.__accounts)
        txn = Transaction("deposit", amount, acc._id)
        save_transaction(txn)
        return new_balance

    def list_accounts(self):
        return self.__accounts 

    def withdraw(self, acc_id: str, amount: float):
        acc = self.find_account(acc_id)
        new_balance = acc.withdraw(amount)
        
        save_accounts(self.__accounts)
        txn = Transaction("withdraw", amount, acc._id)
        save_transaction(txn)
        return new_balance

    def transfer(self, src_id: str, trg_id: str, amount: float):
        src = self.find_account(src_id)
        trg = self.find_account(trg_id)

        new_balance = src.withdraw(amount)
        trg.deposit(amount)

        txn = Transaction(
            generate_id(),
            "transfer",
            amount,
            src._id,
            trg._id,
        )

        save_accounts(self.__accounts)
        save_transaction(txn)
        return new_balance
        

    def show_balance(self, acc_id, ):
        acc = self.find_account(acc_id)
        return acc.balance

    def list_accounts(self):
        return self.__accounts 