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
    

                
                



SalesRetailAnalyzer.TotalSalesSummaryStats()
SalesRetailAnalyzer.AverageSummaryStats()
SalesRetailAnalyzer.MaxMinSummaryStats()
SalesRetailAnalyzer.LenResultsStats()
SalesRetailAnalyzer.FilterbyProduct("laptop")
SalesRetailAnalyzer.FilterbyDate("2026-01-01")

