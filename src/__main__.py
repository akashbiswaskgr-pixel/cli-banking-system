from src.app.storage import ensure_files
from src.app.manager import BankManager
from src.config import BANK_NAME

choices = {
    1: "Create Account",
    2: "Deposit Amount",
    3: "Withdraw Amount",
    4: "Show balance",
    5: "Transfer Amount",
    6: "Show all Accounts",
    7: "Exit Bank",
}

def main():
    print(f"!!! Welcome to {BANK_NAME} !!!")

    menu = "\nHere's the menu [1-7]:\n"
    for num, value in choices.items():
        menu += f"[{num}]: {value}\n"

    bank = BankManager()

    while True:
        choice = int(input(menu))

        match choice:
            case 1:
                name = input(">>> Enter your name: ")
                acc = bank.create(name)
                print(f"Created! AccId: {acc._id}")
            case 2:
                acc_id = input(">>> Enter your AccId: ")
                amount = float(input(">>> Enter amount to deposit: "))
                new_balance = bank.deposit(acc_id, amount)
                print(f">> Deposited ₹{amount}. Updated Balance is ₹{new_balance}")
            case 3:
                acc_id = input(">>> Enter your AccId: ")
                amount = float(input(">>> Enter amount to withdraw: "))
                new_balance = bank.withdraw(acc_id, amount)
                print(f">> Withdrew ₹{amount}. Updated Balance is ₹{new_balance}")
            case 4:
                acc_id = input(">>> Enter your AccId: ")
                balance = bank.show_balance(acc_id)
                print(f">> Your Balance is: ₹{balance}")
            case 5:
                src_id = input(">>> Enter sender's AccId: ")
                trg_id = input(">>> Enter receiver's AccId: ")
                amount = float(input(">>> Enter amount to transfer: "))
                new_balance = bank.transfer(src_id, trg_id, amount)
                print(f">> Transferred ₹{amount}. Updated Balance is ₹{new_balance}")
            case 6:
                accounts = bank.list_accounts()
                for acc in accounts:
                    print(acc)
            case 7:
                print("Thank you for your service...")
                break


if __name__ == "__main__":
    ensure_files()  # db connection function
    main()
    