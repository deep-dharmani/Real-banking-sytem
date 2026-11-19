import json
import os
import msvcrt
FILE_NAME = "accounts.json"
class Bank_account:
    def __init__(self, account, balance, password):
        self.account = account
        self.__balance = balance
        self.password = password
    def Deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            save_accounts()
            msg = f"Your balance becomes {self.__balance}"
            print(msg)
            return msg
        else:
            msg = "Please add a sufficient amount"
            print(msg)
            return msg
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            save_accounts()

            msg = f"Now your balance is {self.__balance}"
            print(msg)
            return msg

        elif self.__balance == 0:
            msg = "Your account has 0 balance"
            print(msg)
            return msg

        else:
            msg = f"Your balance is {self.__balance}. Please enter a relevant amount."
            print(msg)
            return msg
    def total_balance(self):
        msg = f"You have {self.__balance} rupees in your bank account"
        print(msg)
        return msg 
deep = Bank_account('111111111111', 0, "6754")
mahveer = Bank_account('111111111112', 0, "6873")
sohail = Bank_account('111111111113', 0, "8832")
kanwal = Bank_account('111111111114', 0, "7764")
bhawish = Bank_account('111111111115', 0, "9965")
accounts = [deep, mahveer, sohail, kanwal, bhawish]
def save_accounts():
    data = []
    for account in accounts:
        data.append({
            "account": account.account,
            "balance": account._Bank_account__balance,
            "password": account.password
        })
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                data = json.load(file)
                for saved_account in data:
                    for account in accounts:
                        if account.account == saved_account["account"]:
                            account._Bank_account__balance = saved_account["balance"]
                            account.password = saved_account["password"]
                            break
            except json.JSONDecodeError:
                print("Account file is empty or contains invalid data.")
load_accounts()
def get_input(length):
    text = ""
    while len(text) < length:
        char = msvcrt.getwch()

        if char == "\r":
            break

        print(char, end="", flush=True)
        text += char
    print()
    return text
while True:
    print("\nEnter account no")
    account_no = get_input(12)
    account_name = None
    for i in accounts:
        if i.account == account_no:
            account_name = i
            break
    if account_name is None:
        print("Invalid account no")
        continue
    print("Enter password of your account")
    password = get_input(4)
    if account_name.password == password:
        print(f"""
Hello Sir!
Enter 1 for Deposit amount
Enter 2 for Withdraw amount
Enter 3 for checking your total balance
Enter 4 to exit the programme
""")
        try:
            work = int(get_input(1))
            match work:

                case 1:
                    amount_value = int(input("Enter amount for deposit: "))
                    account_name.Deposit(amount_value)

                case 2:
                    amount_value = int(input("Enter amount for withdrawal: "))
                    account_name.withdraw(amount_value)

                case 3:
                    account_name.total_balance()

                case 4:
                    print("Thanks for using our bank")
                    break

                case _:
                    print("Invalid option")

        except ValueError:
            print("Please enter a valid number")

    else:
        print("Wrong password")
