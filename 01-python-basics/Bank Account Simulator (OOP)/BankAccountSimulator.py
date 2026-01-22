import json
class BankAccount:
    Accounts={}



    def LoadAccount():
        try:
            with open("AccountDB.json","r") as file:
                 content = file.read().strip()
            if content == "":
                BankAccount.Accounts = {}
        except FileNotFoundError:
            BankAccount.Accounts={}

    def Save_account():
        with open("AccountDB.json","w") as file:
            json.dump(BankAccount.Accounts,file,indent=1)



    
    
    
    def CreateAccount ():
        BankAccount.LoadAccount()
        AccountName=input("Enter Your Name :")
        if AccountName in BankAccount.Accounts.keys():
            print("Account Already Exists with this name")
            return
        else:
            BankAccount.Accounts[AccountName]={
                "AccountName":AccountName,
                "Balance":0,

            }

        InitalDeposit=int(input("Enter a Amount to Deposit :"))
        if InitalDeposit<0:
            print("Enter a Valid Amount")
        else:
            BankAccount.Accounts[AccountName]["Balance"]+=InitalDeposit
            print("Account Created Successfully")
            BankAccount.Save_account()
            

    
    def deposit():
        BankAccount.LoadAccount()
        AccountName=input("Enter Your Name :")
        if AccountName not in BankAccount.Accounts.keys():
            print("Account Not Found")
        else:
            DepositAmount=int(input("Enter a Amount to Deposit :"))
            if DepositAmount<0:
                print("Enter a Valid Amount")
            else:
                BankAccount.Accounts[AccountName]["Balance"]+=DepositAmount
                print("Amount Deposited Successfully")
                BankAccount.Save_account()


    def Withdraw():
        BankAccount.LoadAccount()
        AccountName=input("Enter your name :")
        if AccountName not in BankAccount.Accounts.keys():
            print("Account not Found")
        else:
            WithdrawAmount=int(input("Enter a Amount to Withdraw :"))
            if WithdrawAmount<0:
                print("Enter a Valid Amount")
            else:
                    BankAccount.Accounts[AccountName]["Balance"]-=WithdrawAmount
                    print("Amount Withdrawn Successfully")
            BankAccount.Save_account()
    
    def DisplayAccount():
        BankAccount.LoadAccount()
        AccountName=input("Enter Your Name : ")
        if AccountName not in BankAccount.Accounts.keys():
            print("Bank Account Not Found")
        else:
            print("Account Holder: ", BankAccount.Accounts[AccountName]["AccountName"])
            print("Account Balance: ", BankAccount.Accounts[AccountName]["Balance"])              
            BankAccount.Save_account()

while True:
    print("\n Welcome to SBA \n") 
    print("Enter 1 to Create Account")
    print("Enter 2 to Deposit")
    print("Enter 3 to Withdraw")
    print("Enter 4 to Display Account")
    print("Enter 5 to Exit")
    choice =int (input())
    match choice:
        case 1:
            BankAccount.CreateAccount()
        case 2:
            BankAccount.deposit()
        case 3:
            BankAccount.Withdraw()
        case 4:
             BankAccount.DisplayAccount()
        case 5:
             break