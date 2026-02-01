import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import datetime

filedir=os.path.dirname(os.path.abspath(__file__))
Data=os.path.join(filedir,"Data.csv")
logfile=os.path.join(filedir,"Cleaning.log")

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

    def NormalizeTransactionID(self):
        self.df["Transaction ID"]=self.df["Transaction ID"].astype(str).str.lower().str.strip()
        duplicates=self.df["Transaction ID"].duplicated().sum()
        self.df=self.df.drop_duplicates(subset=["Transaction ID"])
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Transaction ID normalized, Duplicates Removed : {duplicates}\n")
        print("Transaction ID normalized")
    
    def NormalizeCustomerID(self):
        self.df["Customer ID"]=self.df["Customer ID"].astype(str).str.lower().str.strip()
        
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Customer ID normalized\n")
        print("Customer ID normalized")
    
    def NormalizeCategory(self):
        self.df["Category"]=self.df["Category"].astype(str).str.lower().str.strip().str.replace(r"\s+"," ",regex=True)
        
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Category normalized\n")
        print("Category normalized")
    
    def NormalizeProduct(self):
        self.df["Item"]=self.df["Item"].astype(str).str.lower().str.strip().str.replace(r"\s+"," ",regex=True)
        self.df=self.df.dropna(subset=["Item"])
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Product normalized\n")
        print("Product normalized")
    
    def NormalizePricePerUnit(self):
        self.df=self.df.dropna(subset=["Price Per Unit"])
        missingvals=self.df["Price Per Unit"].isna().sum()
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Missing Values Removed : {missingvals}\n")
        print("Price Per Unit normalized")
    
    def NormalizeQuantity(self):
        Missingvalues=self.df["Quantity"].isna().sum()
        self.df=self.df.dropna(subset=["Quantity"])
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}:Missing Values Removed : {Missingvalues}\n")
        print("Quantity normalized")
    
    def NormalizeTotalSpent(self):
        missingvals=self.df["Total Spent"].isna().sum()
        print(f"Missing values in Total Spent: {missingvals}")
        self.df=self.df.dropna(subset=["Total Spent"])

        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Missing Values Removed : {missingvals}\n")
        print("Total Spent normalized")
    
    def NormalizePaymentMethod(self):
        self.df["Payment Method"]=self.df["Payment Method"].astype(str).str.lower().str.strip().str.replace(r"\s+"," ",regex=True)
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Payment Method normalized\n")
        print("Payment Method normalized")

    def NormalizeLocation(self):
        self.df["Location"]=self.df["Location"].astype(str).str.lower().str.strip().str.replace(r"\s+"," ",regex=True)
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Location normalized\n")
        print("Location normalized")
    
    def NormalizeDate(self):
        self.df["Transaction Date"]=pd.to_datetime(self.df["Transaction Date"])
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}:Transaction Date normalized\n")
        print("Transaction Date normalized")

    def NormalizeDiscountApplied(self):
        missingvals=self.df["Discount Applied"].isna().sum()
        self.df["Discount Applied"] = self.df["Discount Applied"].fillna("Unknown")
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Missing Values Removed : {missingvals}, Discount Applied normalized\n")
        print("Discount Applied normalized")

    def remove_outliers(self, col):
        Q1 = self.df[col].quantile(0.25)
        Q3 = self.df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = self.df[(self.df[col] < lower) | (self.df[col] > upper)]
        self.df = self.df[(self.df[col] >= lower) & (self.df[col] <= upper)]
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: Outliers Removed : {outliers.shape[0]}, {col} normalized\n")
        print(f"{col} normalized")

    def save_and_log(self, message):
        self.df.to_csv(Data, index=False)
        with open(logfile,"a") as f:
            f.write(f"{datetime.datetime.now()}: {message}\n")
        print(message)


app=DataCleaning()
app.NormalizeTransactionID()
app.NormalizeCustomerID()
app.NormalizeCategory()
app.NormalizeProduct()
app.NormalizePricePerUnit()
app.NormalizeQuantity()
app.NormalizeTotalSpent()
app.NormalizePaymentMethod()
app.NormalizeDate()
app.NormalizeDiscountApplied()
app.save_and_log("Data Cleaning Completed")


    
