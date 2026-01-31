import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import datetime

filedir=os.path.dirname(os.path.abspath(__file__))
Data=os.path.join(filedir,"Data.csv")

class DataCleaning:
    def __init__(self):
        if os.path.exists(Data):
            self.df=self.loadData()
            print("Found")
        else:
            print("File not found")
            sys.exit(1)

    def loadData(self):
        self.df=pd.read_csv(Data)
        return self.df

    def NormalizeTransactionDate(self):
        self.df["Transaction Date"]=pd.to_datetime(self.df["Transaction Date"])
        missingvalues=self.df.isnull().sum()
        self.df["Transaction Date"].fillna(method="ffill", inplace=True)
        self.df.to_csv(Data,index=False)
        print(missingvalues)
        TranscationDuplicates=self.df["Transaction Date"].duplicated()
        DropDuplicates=self.df.drop_duplicates(subset="Transaction Date",keep="first",inplace=True)
        self.df.to_csv(Data,index=False)
        BoolDups=self.df["Transaction Date"].duplicated()
    def NormalizeItem(self):
        self.df["Item"].fillna(method="ffill", inplace=True)
        Itemdups=self.df["Item"].duplicated()
        dropitemdups=self.df.drop_duplicates(subset="Item",keep="first",inplace=True)
        print("Duplicates :",Itemdups.sum())
        print("Missing values :",self.df["Item"].isnull().sum())
        self.df.to_csv(Data,index=False)
    def NormailzeCustomer(self):
        self.df["Customer ID"].fillna(method="ffill", inplace=True)
        Customerdups=self.df["Customer ID"].duplicated()
        dropdups=self.df.drop_duplicates(subset="Customer ID",keep="first",inplace=True)
        self.df.to_csv(Data,index=False)
        print("Duplicates :",Customerdups.sum())
    def NormalizeDiscountApplied(self):
        self.df["Discount Applied"] = np.where(
            self.df["Price Per Unit"] * self.df["Quantity"] == self.df["Total Spent"],
            "FALSE",  # No discount applied
            "TRUE"    # Discount applied
        )
        self.df.to_csv(Data,index=False)
    
    

DataCleaning().NormalizeDiscountApplied()