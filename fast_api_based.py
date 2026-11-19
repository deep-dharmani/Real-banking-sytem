import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import json
import re
import os
bank_app = FastAPI()
FILE = "C:\\Users\\hp\\Documents\\GitHub\\Real banking sytem\\bank_accounts.json"
class BankAccount(BaseModel):
    name: str
    cnic_number: str
    password: str
class account_no_(BaseModel):
    account:int
    password:str
    money:int
def load_accounts():
    if not os.path.exists(FILE):
        return {"accounts": [], "last_account_no": 100000}
    with open(FILE, "r") as file:
        return json.load(file)
def save_accounts(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
@bank_app.post("/new-account")
def create_account(account: BankAccount):
    pattern = r"^\d{5}-\d{7}-\d{1}$"
    if not re.match(pattern, account.cnic_number):
        return {"error": "Invalid CNIC format"}
    data = load_accounts()
    data["last_account_no"] += 1
    account_no = data["last_account_no"]
    new_account = {
        "account_no": account_no,
        "name": account.name,
        "cnic_number": account.cnic_number,
        "Balance":0,
        "Password":account.password
    }
    data["accounts"].append(new_account)
    save_accounts(data)
    return {
        "message": "Account created successfully",
        "account_no": account_no
    }
@bank_app.post("/exisisting_account/withdraw")
def account_no(acount:account_no_):
    try:
        with open(FILE,"r") as file:
            data = load_accounts()
            account_found=False
            for acc in data["accounts"]:
                if acc["account_no"] == acount.account:
                    account_found=True
                    break
            if account_found:
                if acount.password==acc["Password"]:
                    if 0<acount.money<=acc["Balance"]:
                        acc["Balance"]-=acount.money
                        save_accounts(data)
                        return {"msg":f"your account blance become {acc["Balance"]}"}
                    else:
                        return{"msg":f"Your account balance is {acc["Balance"]}please give some relevent ammount"}
                else:
                    return{"msg":f"wrong password for {acount}"}
            else:
                return{"msg":"wrong account number"}        
    except FileNotFoundError:
        return {"msg":f"{acount} is Invalid number for account"}
@bank_app.post("/exisisting_account/Deposit")
def account_no(acount:account_no_):
    try:
        with open(FILE,"r") as file:
            data = load_accounts()
            account_found=False
            for acc in data["accounts"]:
                if acc["account_no"] == acount.account:
                    account_found=True
                    break
            if account_found:
                if acount.password==acc["Password"]:
                    if acount.money>0:
                        acc["Balance"]+=acount.money
                        save_accounts(data)
                        return {"msg":f"your account blance become {acc["Balance"]}"}
                    else:
                        return{"msg":f"Please add some some relevent ammount"}
                else:
                    return{"msg":f"wrong password for {acount}"}
            else:
                return{"msg":"wrong account number"}        
    except FileNotFoundError:
        return {"msg":f"{acount} is Invalid number for account"}
if __name__ == "__main__":
    uvicorn.run(bank_app, host="127.0.0.1", port=8000)
