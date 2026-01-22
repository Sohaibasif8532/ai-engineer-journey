class BankAccount:
    Accounts={}
    
    
    def CreateAccount ():
        AccountName=input("Enter Your Name :")
        if AccountName in BankAccount.Accounts.keys():
            print("Account Already Exists with this name")
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

    
    def deposit():
        AccountName=input("Enter Your Name :")
        if AccountName not in BankAccount.Accounts.keys():
            print("Account Not Found")
        else:
            DepositAmount=int(input("Enter a Amount to Deposite"))
            if DepositAmount<0:
                print("Enter a Valid Amount")
            else:
                BankAccount.Accounts[AccountName]["Balance"]+=DepositAmount
                print("Amount Deposited Successfully")
    def Withdraw():
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
    
    def DisplayAccount():
        AccountName=input("Enter Your Name : ")
        if AccountName not in BankAccount.Accounts.keys():
            print("Bank Account Not Found")
        else:
            print("Account Holder: ", BankAccount.Accounts[AccountName]["AccountName"])
            print("Account Balance: ", BankAccount.Accounts[AccountName]["Balance"])              

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