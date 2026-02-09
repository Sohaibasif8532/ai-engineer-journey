import pandas as pd
import os
import logging


class DataCleaner:
    def __init__(self, df):
        self.df=df
        self.snapshots = {}

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
            self.df.dropna(subset=["Product_Name"], inplace=True)
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
        self.df["Price"] = pd.to_numeric(self.df["Price"], errors="coerce")
        self.df["Quantity"] = pd.to_numeric(self.df["Quantity"], errors="coerce")                               

    def CleanNumericColumns(self):
        for col in ["Price","Quantity"]:
            self.df[col] = pd.to_numeric(
                self.df[col].astype(str).str.replace(r"[^\d.]", "", regex=True),
                errors="coerce"
            )