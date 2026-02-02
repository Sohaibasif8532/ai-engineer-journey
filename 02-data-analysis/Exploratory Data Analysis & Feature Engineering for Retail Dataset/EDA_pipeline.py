import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

filedir=os.path.dirname(os.path.abspath(__file__))
projectroot=filedir
inputData=os.path.join(projectroot,"data","input","data.csv")
outputDataGeneral=os.path.join(projectroot,"data","output","EDA_general_stats","EDA_Featured_output.csv")
output_data_aggregated=os.path.join(projectroot,"data","output","EDA_aggrevated_results","EDA_Featured_output.csv")
output_data_payment=os.path.join(projectroot,"data","output","EDA_Revenue_output","EDA_Revenue_output.csv")
output_data_top_customers=os.path.join(projectroot,"data","output","EDA_top_customers","EDA_top_customers.csv")
output_data_monthly_revenue=os.path.join(projectroot,"data","output","EDA_monthly_revenue","EDA_monthly_revenue.csv")
logs=os.path.join(projectroot,"logs","EDA_logs.log")


class EDA_Pipeline:
    def __init__(self,inputData,outputDataGeneral,output_data_aggregated,output_data_payment,output_data_top_customers,output_data_monthly_revenue,logs):
        self.inputData=inputData
        self.outputDataGeneral=outputDataGeneral
        self.output_data_aggregated=output_data_aggregated
        self.output_data_payment=output_data_payment
        self.output_data_top_customers=output_data_top_customers
        self.output_data_monthly_revenue=output_data_monthly_revenue
        self.logs=logs

    def loadData(self):
        if os.path.exists(self.inputData):
            df=pd.read_csv(self.inputData)
            print("Data Loaded Successfully")
            return df
        else:
            print("File Not Found")
    
    def descriptive_stats(self):
        df=pd.read_csv(self.inputData)
        Stats=df.groupby("Category").describe().reset_index()
        Friendly_Stats={
            "count":"Total Records",
            "mean":"Average",
            "std":"Standard Deviation",
            "min":"Minimum",
            "25%":"25th Percentile",
            "50%":"50th Percentile",
            "75%":"75th Percentile",
            "max":"Maximum"
        }
        Stats=Stats.rename(columns=Friendly_Stats)
        df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce") 
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
        df["Unit Price"] = df["Total Spent"] / df["Quantity"]                 
        df["HighValueTransaction"] = df["Total Spent"] > 1000   
        TotalRevenue = df.groupby("Category").agg(
            total_revenue=("Total Spent", "sum"),
            average_order_value=("Total Spent", "mean"),
            Total_Orders=("Total Spent", "count"),
            average_unit_price=("Unit Price", "mean"),
            has_high_value_transaction=("HighValueTransaction", lambda x: x.any())  
        ).reset_index()


        RevenuePerPaymentMethod=df.groupby("Payment Method").agg(
            Total_Revenue=("Total Spent","sum")
        ).reset_index()


        customer_stats = df.groupby("Customer ID").agg(
            TotalSpent=("Total Spent", "sum"),
            AverageSpent=("Total Spent", "mean"),
            Customer_Purchase_Count=("Customer ID","count"),
        ).reset_index()


        df["Month"] = pd.to_datetime(df["Transaction Date"]).dt.month
        Monthly_Revenue=df.groupby(df["Month"]).agg(
            MonthlyRevenue=("Total Spent","sum")
        ).reset_index()
        
        Stats.to_csv(self.outputDataGeneral,index=False)
        TotalRevenue.to_csv(self.output_data_aggregated,index=False,mode="w", header=True)
        RevenuePerPaymentMethod.to_csv(self.output_data_payment,index=False,mode="w", header=True)
        customer_stats.to_csv(self.output_data_top_customers,index=False,mode="w", header=True)
        Monthly_Revenue.to_csv(self.output_data_monthly_revenue,index=False,mode="w", header=True)
        with open(self.logs, "w") as f:
            f.write("*"*226)
            f.write("\n")
            f.write("\n")
            f.write(f"General Stats Added at :{datetime.now()}")
            f.write("\n")
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write(Stats.to_string())
            f.write("\n")
            f.write(TotalRevenue.to_string())
            f.write("\n")
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write("\n")
            f.write(f"Revenue Per Payment Method Added at :{datetime.now()}")
            f.write("\n")            
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write(RevenuePerPaymentMethod.to_string())
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write("\n")
            f.write(f"Top Customers Added at :{datetime.now()}")
            f.write("\n")
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write(customer_stats.to_string())
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write("\n")
            f.write(f"Monthly Revenue Added at :{datetime.now()}")
            f.write("\n")
            f.write("\n")
            f.write("*"*226)
            f.write("\n")
            f.write("\n")
            f.write(Monthly_Revenue.to_string())
            f.write("\n")
            f.write("*"*226)
            f.write("\n")





app=EDA_Pipeline(inputData,outputDataGeneral,output_data_aggregated,output_data_payment,output_data_top_customers,output_data_monthly_revenue,logs)
app.loadData()
app.descriptive_stats()