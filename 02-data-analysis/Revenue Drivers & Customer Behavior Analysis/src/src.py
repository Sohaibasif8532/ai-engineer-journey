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
analysis=os.path.join(projectroot,"data","output","analysis","analysis.csv")
featured=os.path.join(projectroot,"data","output","featured","featured.csv")
logfiles=os.path.join(projectroot,"logs","logs.log")


class RDCBA:
    def __init__(self, inputdata, cleaned, analysis, featured, logfiles):
        self.inputdata=inputdata
        self.cleaned=cleaned
        self.analysis=analysis
        self.featured=featured
        self.logfiles=logfiles

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
        logging.info(f"Outliers Removed using IQR Method")
        
    
    def saveCleanedData(self):
        self.df.to_csv(self.cleaned, index=False)
        print("Cleaned Data Saved Successfully")
        logging.info("Cleaned Data Saved Successfully")


    



app=RDCBA(inputdata, cleaned, analysis, featured, logfiles)
app.loadData()
app.validate_data()
app.IQR()
