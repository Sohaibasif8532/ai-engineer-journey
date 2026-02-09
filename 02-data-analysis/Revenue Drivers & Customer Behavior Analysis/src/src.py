import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt   
import logging
import os


filedir=os.path.dirname(os.path.abspath(__file__))
projectroot=os.path.dirname(filedir)
inputdata=os.path.join(projectroot,"data","input","input.csv")
cleaned=os.path.join(projectroot,"data","output","cleaned","cleaned.csv")
featured=os.path.join(projectroot,"data","output","features","features.csv")
logfiles=os.path.join(projectroot,"logs","logs.log")



class RDCBA:
    def __init__(self, inputdata, cleaned, featured, logfiles):
        self.inputdata=inputdata
        self.cleaned=cleaned
        self.featured=featured
        self.logfiles=logfiles
        self.snapshots={}

        logging.basicConfig(
            filename=self.logfiles,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def loadData(self):
        if os.path.exists(self.inputdata):
            self.df=pd.read_csv(self.inputdata)
            print("Data Loaded Successfully")
            return self.df
        else:
            print("File Not Found")
            self.df = None
    

    def validate_data(self):
        nullValues=self.df.isnull().sum()
        duplicateValues=self.df.duplicated().sum()
        print(f"Null Values in Data:\n{nullValues}")
        print(f"Duplicate Values in Data:\n{duplicateValues}")
        if nullValues.sum()>0:
            print("Data Contains Null Values")
            self.CleanNullValues()
            
        if duplicateValues>0:
            print("Data Contains Duplicate Values")
            self.RemoveDuplicates()
        
    def CleanNullValues(self):
        self.snapshots["Before Cleaning Null Values"]=self.df.copy()
        
        if self.df["Transaction_ID"].isnull().any():
            self.df["Transaction_ID"].ffill(inplace=True)
            logging.info(f"Null Values Removed from Transaction ID :{self.df['Transaction_ID'].isnull().sum()} ")
        if self.df["Transaction_Date"].isnull().any():
            self.df["Transaction_Date"].ffill(inplace=True)
            logging.info(f"Null Values Removed from Transaction Date :{self.df['Transaction_Date'].isnull().sum()} ")
            
        if self.df["Customer_ID"].isnull().any():
            self.df["Customer_ID"].ffill(inplace=True)  
            logging.info(f"Null Values Removed from Customer ID :{self.df['Customer_ID'].isnull().sum()} ")
           
        if self.df["Product_Name"].isnull().any():
            self.df["Product_Name"].dropna(inplace=True)
            logging.info(f"Null Values Removed from Product Name :{self.df['Product_Name'].isnull().sum()} ")
            
            
        self.df = self.df.dropna(subset=["Quantity", "Price"])
        
            
        if self.df["Transaction_Status"].isnull().any():
            self.df["Transaction_Status"].fillna("Unknown", inplace=True)
            logging.info(f"Null Values Removed from Transaction Status :{self.df['Transaction_Status'].isnull().sum()} ")
            
        print(f"Removed Null Values, \n Current Null Values Count:\n{self.df.isnull().sum()}")
        logging.info(f"Null Values Found : {self.df.isnull().sum()}")
    
    def RemoveDuplicates(self):
        if self.df["Transaction_ID"].duplicated().any():
            self.df.drop_duplicates(subset=["Transaction_ID"], keep="first", inplace=True)
            
            print(f"Removed Duplicates from Transaction_ID : {self.df['Transaction_ID'].duplicated().sum()}")
        else:
            print("No Duplicates Found in Transaction_ID")
            
        print("*"*50)
        print("\n")
        print("Duplicates Removed Safely")
        print(f"Current Duplicates Count : {self.df['Transaction_ID'].duplicated().sum()}")
        print("*"*50)
        print("\n")

    def IQR(self):
        cols= ["Price", "Quantity"]
        self.df[["Price", "Quantity"]] = self.df[["Price", "Quantity"]].apply(
            lambda x: pd.to_numeric(x.astype(str).str.replace(r"[^\d.]", "", regex=True), errors="coerce")
        )
        
        Q1=self.df[cols].quantile(0.25)
        Q3=self.df[cols].quantile(0.75)
        IQR=Q3-Q1
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        mask = ~((self.df[["Price", "Quantity"]] < lower_bound) | (self.df[["Price", "Quantity"]] > upper_bound)).any(axis=1)
        self.df = self.df[mask]
        print(f"Removed Outliers using IQR Method")

    def removespecial(self):
        self.df["Price"]=self.df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True)
        self.df["Quantity"]=self.df["Quantity"].astype(str).str.replace(r"[^\d.]", "", regex=True)
        self.df["Price"] = pd.to_numeric(self.df["Price"], errors="coerce")
        self.df["Quantity"] = pd.to_numeric(self.df["Quantity"], errors="coerce")                               

            
    def TargetVariable(self):
        # Ensure Price is numeric
        self.df["Price"] = pd.to_numeric(self.df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True), errors="coerce")

        self.df["High Value Transaction"]= (self.df["Price"]>500).astype(int)
        
        counts = self.df.groupby("Customer_ID")["Transaction_ID"].transform("count")
        self.df["Repeating Customer"] = (counts > 1).astype(int)
    
    def Customer_total_spend(self):
        self.df["Customer Total Spend"]= self.df.groupby("Customer_ID")["Price"].transform("sum")
        logging.info("Customer Total Spend Calculated")

    def AverageOrderValue(self):
        self.df["Average Order Value"]= self.df.groupby("Customer_ID")["Price"].transform("mean")
        logging.info("Average Order Value Calculated")
    
    def PurchaseFrequency(self):
        self.df["Purchase Frequency"]= self.df.groupby("Customer_ID")["Transaction_Date"].transform("count")
        logging.info("Purchase Frequency Calculated")
    
    def PurchaseRecency(self):
        self.df["Transaction_Date"] = pd.to_datetime(self.df["Transaction_Date"], errors="coerce")
        ref_date = self.df["Transaction_Date"].max()
        self.df["LastPurchase"]= self.df.groupby("Customer_ID")["Transaction_Date"].transform("max")
        self.df["Purchase Recency"]= (ref_date - self.df["LastPurchase"]).dt.days
        logging.info("Purchase Recency Calculated")

    def CategoryDiversity(self):
        self.df["Category Diversity"]= self.df.groupby("Customer_ID")["Product_Name"].transform("nunique")
        logging.info("Category Diversity Calculated")

    def Aggregations(self, threshold=900):
        customer_spend = self.df.groupby("Customer_ID")["Price"].max().reset_index()
        customer_spend["High/Low Value Customers"] = customer_spend["Price"].apply(
            lambda x: "High Value Customer" if x > threshold else "Low Value Customer"
        )
        logging.info("Customer Total Spend Calculated")
        
        # Merge back into main df
        self.df = self.df.merge(customer_spend[["Customer_ID","High/Low Value Customers"]], on="Customer_ID", how="left")

    def save_data(self, file_path, columns=None):
        if columns:
            self.df[columns].to_csv(file_path, index=False)
        else:
            self.df.to_csv(file_path, index=False)
        logging.info(f"Data Saved to {file_path}")
        print(f"Data Saved to {file_path}")



app=RDCBA(inputdata, cleaned, featured, logfiles)
app.loadData()
app.validate_data()
app.save_data(app.cleaned) 
app.TargetVariable()
app.Customer_total_spend()
app.AverageOrderValue()
app.PurchaseFrequency()
app.PurchaseRecency()
app.CategoryDiversity()
app.Aggregations()
app.save_data(app.featured, columns=["Customer_ID","Transaction_ID","High Value Transaction", "Repeating Customer", "Customer Total Spend", "Average Order Value", "Purchase Frequency", "Purchase Recency", "Category Diversity","High/Low Value Customers"]) 