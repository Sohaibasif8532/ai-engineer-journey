import pandas as pd
import logging
import os
from datetime import datetime 
import sys
import matplotlib.pyplot as plt



FileDir=os.path.dirname(os.path.abspath(__file__))
csvPath=os.path.join(FileDir, "PET.csv")
logPath=os.path.join(FileDir, "PET.log")
logging.basicConfig(
    filename=(logPath),
    level=logging.INFO,
    format='%(asctime)s - %(message)s'

)
    
class PET:
    csvPath=csvPath
    logPath=logPath
    
    @staticmethod
    def AddExpense(Amount,Category,Description):
        if os.path.exists(PET.csvPath) and os.path.getsize(PET.csvPath) > 0:
            df = pd.read_csv(PET.csvPath)
        else:
            df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        
        newrow={
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Category": Category,
            "Amount": float(Amount),
            "Description": Description
        }
        df=pd.concat([df, pd.DataFrame([newrow])], ignore_index=True)
        df.to_csv(PET.csvPath, index=False)
            
        logging.info(f"Expense added successfully: {Amount}, {Category}, {Description}")
    

    @staticmethod
    def ViewExpenses(category=None, date=None):
        if os.path.exists(PET.csvPath) and os.path.getsize(PET.csvPath) > 0:
            df = pd.read_csv(PET.csvPath)

            if "Category" in df.columns:
                df["Category"] = df["Category"].astype(str).str.strip()
            if "Date" in df.columns:
                df["Date"] = df["Date"].astype(str).str.strip()
            if category:
                df = df[df["Category"].str.lower() == category.lower()]  
            if date:
                df = df[df["Date"] == date]

            if df.empty:
                print("No expenses match the filter")
            else:
                print(df.to_string(index=True))
        else:
            print("No expenses found")

    
    @staticmethod
    def DeleteExpense(index):
        if os.path.exists(PET.csvPath) and os.path.getsize(PET.csvPath) > 0:
            df=pd.read_csv(PET.csvPath)
        else:
            print("No Expenses Found Try adding one : ")
            return
        
        if str(index).isdigit():
            idx = int(index)
            if idx in df.index:
                deletedrow= df.iloc[idx].to_dict()
                df=df.drop(idx)
                df.to_csv(PET.csvPath,index=False)
                logging.info(f"Expense deleted successfully: {deletedrow}")
                print("Expense deleted successfully")
            else:
                print("Index out of range")
        else:
            print("Invalid index")


    @staticmethod
    def summaryanalytics():
        if os.path.exists(PET.csvPath) and os.path.getsize(PET.csvPath) > 0:
            df=pd.read_csv(PET.csvPath)
            Total=df["Amount"].sum()
            Average=df["Amount"].mean()
            Max=df["Amount" ].max()
            Min=df["Amount"].min()
            print(f"Total Expenses : {Total}", f"Average Expenses : {Average}", f"Max Expenses : {Max}", f"Min Expenses : {Min}")
            logging.info(f"Total Expenses : {Total}, Average Expenses : {Average}, Max Expenses : {Max}, Min Expenses : {Min}")

            plt.plot(df["Date"],df["Amount"])
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.title("Expenses Over Time")
            plt.show()


            categorysum= df.groupby("Category")["Amount"].sum()
            plt.bar(categorysum.index,categorysum.values)
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.title("Expenses by Category")
            plt.show()
        else:
            print("No Expenses Found Try adding one : ")
            sys.exit(1)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid Arguments")
        sys.exit(1)
        
    match sys.argv[1]:
        case "add":
            if len(sys.argv) >= 5:
                PET.AddExpense(sys.argv[2],sys.argv[3],sys.argv[4])
            else:
                 print("Add All the Columns : Amount, Category, Description : ")
        case "view":
            # Handle optional arguments safely
            cat = sys.argv[2] if len(sys.argv) > 2 else None
            dt = sys.argv[3] if len(sys.argv) > 3 else None
            PET.ViewExpenses(cat, dt)
        case "delete":
            if len(sys.argv) >= 3:
                PET.DeleteExpense(sys.argv[2])
            else:
                print("Enter Correct Index no To Delete : ")
                logging.error("Error : Enter Correct Index no To Delete : ")

        case "summary":
            if len(sys.argv) == 2:
                PET.summaryanalytics()
            else:
                print("Invalid Arguments")
                logging.error("Error : Invalid Arguments")
        case _:
            print("Invalid command : ")
            logging.error("Error : Invalid command : ")