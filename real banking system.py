class Bank_account:
    def __init__(self,account,balance,password):
        self.account=account
        self.__balance=balance
        self.password=password
    def Deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            msg_1=f"your balace becomes {self.__balance}"
            print(msg_1)
            return msg_1
        else:
            msg_2= f"Please add some sufficient amount"
            print(msg_2)
            return msg_2
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            msg_3=f"Now your balance is{self.__balance}"
            print(msg_3)
            return msg_3
        elif self.__balance==0:
            msg_4=f"Your account has 0 balance"
            print(msg_4)
            return msg_4
        else:
            msg_5=f"Your balance is {self.__balance} please add relevent amount"
            print(msg_5)
            return
    def total_balance(self):
        msg=f"Your have {self.__balance} rupees in your bank account"
        print(msg)
        return msg
deep=Bank_account('111111111111',0,"6754")
mahveer=Bank_account('111111111111',0,"6873")
sohail=Bank_account('111111111113',0,"8832")
kanwal=Bank_account('111111111114',0,"7764")
bhawish=Bank_account('111111111115',0,"9965")
accounts=[deep,mahveer,sohail,kanwal,bhawish]

import msvcrt
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
    run=0
    print("Enter account no")
    account_no=f"{get_input(12)}"
    for i in accounts:
        if i.account==account_no:
            account_name=i
            run+=1
            break
    if run==0:
        print("Invalid account no")
        continue
    print("Enter password of your account")
    password=(f"{get_input(4)}")
    if account_name.password==password:
        print(f"Hello Sir \nEnter 1 for \
Deposit amount\nEnter 2 for withdraw amount\nEnter 3 for checking your total balance")
        work=int(get_input(1))
        match work:
            case 1:
                amount_value=int(input("Enter amount for deposit: "))
                account_name.Deposit(amount_value)
            case 2:
                amount_value=int(input("Enter your ammount for withdraw from your accont: "))
                account_name.withdraw(amount_value)
            case 3:
                account_name.total_balance()
    else:
        print("wrong password")
