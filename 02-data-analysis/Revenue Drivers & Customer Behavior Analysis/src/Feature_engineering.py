import os
import pandas as pd
import logging


class Feature_Engineering:
    def __init__(self, df):
        self.df=df
    
    def CleanNumericColumns(self):
        for col in ["Price","Quantity"]:
            self.df[col] = pd.to_numeric(
                self.df[col].astype(str).str.replace(r"[^\d.]", "", regex=True),
                errors="coerce"
            )
            
    def TargetVariable(self):
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
        customer_spend = self.df.groupby("Customer_ID")["Price"].sum().reset_index()
        customer_spend["High/Low Value Customers"] = customer_spend["Price"].apply(
            lambda x: "High Value Customer" if x > threshold else "Low Value Customer"
        )
        MostRevenueSegment = customer_spend.groupby("High/Low Value Customers")["Price"].sum().reset_index().sort_values(by="Price", ascending=False).head(1)
        MostRevenueSegment.columns = ["High/Low Value Customers", "Most Revenue Segment"]

        self.df = self.df.merge(customer_spend[["Customer_ID","High/Low Value Customers"]], on="Customer_ID", how="left")
        self.df = self.df.merge(MostRevenueSegment, on="High/Low Value Customers", how="left")

        repeatingBehavior = self.df.groupby("Repeating Customer")["Price"].mean().reset_index()
        repeatingBehavior.columns = ["Repeating Customer", "Repeating Behavior Pattern"]
        
        self.df = self.df.merge(repeatingBehavior, on="Repeating Customer", how="left")
