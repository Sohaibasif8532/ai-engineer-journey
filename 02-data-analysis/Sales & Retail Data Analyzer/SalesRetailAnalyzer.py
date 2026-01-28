import matplotlib.pyplot as pyplot
import pandas as pd
import os
import sys
from datetime import datetime


filedirectory= os.path.dirname(os.path.abspath(__file__))
datapath= os.path.join(filedirectory, "Data.csv")
ResultsPath= os.path.join(filedirectory, "Results.csv")

class SalesRetailAnalyzer:
    @staticmethod
    def TotalSalesSummaryStats():
        if os.path.exists(datapath):
            data= pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            data["TotalSales"]= data["Quantity"]*data["UnitPrice"]
            print(data["TotalSales"].sum())
            data.to_csv(ResultsPath,index=False)
        else:
            print("File not found")
    @staticmethod
    def AverageSummaryStats():
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            data["TotalSales"]=data["Quantity"]*data["UnitPrice"]
            data["AverageSales"]=data["TotalSales"].mean()
            data.to_csv(ResultsPath,index=False)
        else:
            print("File not found") 
    @staticmethod
    def MaxMinSummaryStats():
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            data["TotalSales"]=data["Quantity"]*data["UnitPrice"]
            data["MaxSales"]=data["TotalSales"].max()
            data["MinSales"]=data["TotalSales"].min()
            data.to_csv(ResultsPath,index=False)
        else:
            print("File not found")

    @staticmethod
    def LenResultsStats():
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            data["TotalSales"]=data["Quantity"]*data["UnitPrice"]
            data["LengthSales"]=data["TotalSales"].count()+1
            data.to_csv(ResultsPath,index=False)
        else:
            print("File not found")

    @staticmethod
    def FilterbyDate(Userdate):
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            data["Date"]=pd.to_datetime(data["Date"])
            for index,row in data.iterrows():
                if Userdate in str(row["Date"]): 
                    print("Entries for Date found",row)
                    break
            else:
                print("Date not found")
        else:
            print("File not found")
    @staticmethod
    def FilterbyProduct(UserProduct):
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            for index,row in data.iterrows():
                if UserProduct in str(row["Product"]): 
                    print("Entries for Product found",row)
                    break
            else:
                print("Product not found")
        else:
            print("File not found")
    @staticmethod
    def FilterbyCategory(UserCategory):
        if os.path.exists(datapath):
            data=pd.read_csv(datapath)
            data["Product"] = data["Product"].str.lower()
            data["Category"] = data["Category"].str.lower()
            for index,row in data.iterrows():
                if UserCategory in str(row["Category"]): 
                    print("Entries for Category found",row)
                    break
            else:
                print("Category not found")
        else:
            print("File not found")
    

                
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Invalid arguments")
        sys.exit(1)
    print("="*50)
    print("1. Total Sales Summary Stats")
    print("2. Average Sales Summary Stats")
    print("3. Max Min Sales Summary Stats")
    print("4. Length Sales Summary Stats")
    print("5. Filter by Date")
    print("6. Filter by Product")
    print("7. Filter by Category")
    print("="*50)
    match sys.argv[1]:
        case "1":
            if len(sys.argv)==2:
                SalesRetailAnalyzer.TotalSalesSummaryStats()
            else:
                print("Invalid arguments")
        case "2":
            if len(sys.argv)==2:
                SalesRetailAnalyzer.AverageSummaryStats()
            else:
                print("Invalid arguments")
        case "3":
            if len(sys.argv)==2:
                SalesRetailAnalyzer.MaxMinSummaryStats()
            else:
                print("Invalid arguments")
        case "4":
            if len(sys.argv)==2:
                SalesRetailAnalyzer.LenResultsStats()
            else:
                print("Invalid arguments")
        case "5":
            if len(sys.argv)==3:
                SalesRetailAnalyzer.FilterbyDate(sys.argv[2])
            else:
                print("Invalid arguments")
        case "6":
            if len(sys.argv)==3:
                SalesRetailAnalyzer.FilterbyProduct(sys.argv[2])
            else:
                print("Invalid arguments")
        case "7":
            if len(sys.argv)==3:
                SalesRetailAnalyzer.FilterbyCategory(sys.argv[2])
            else:
                print("Invalid arguments")
        case _:
            print("Invalid arguments")
            sys.exit(1)




