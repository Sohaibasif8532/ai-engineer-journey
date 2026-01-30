import pandas as pd
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

filedir=os.path.dirname(os.path.abspath(__file__))
datapath=os.path.join(filedir,"SARGA.csv")

class SARGA:
    @staticmethod
    def LoadData():
        if os.path.exists(datapath):
            df=pd.read_csv(datapath)
            return df
        else:
            print("File not found")
            sys.exit(1)
    @staticmethod
    def SalesByCategory():
        df=SARGA.LoadData()
        df=df.groupby("Category")["TotalSales"].agg(TotalSales="sum").reset_index().sort_values(by="TotalSales",ascending=False)
        print(df)
        plt.bar(df["Category"],df["TotalSales"])
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.title("Total Sales by Category")
        plt.show()
    @staticmethod
    def TopProducts():
        df=SARGA.LoadData()
        df=df.groupby("Category")["TotalSales"].agg(TopProducts="sum").reset_index().sort_values(by="TopProducts",ascending=False)
        print(df)
        plt.bar(df["Category"],df["TopProducts"])
        plt.xlabel("Category")
        plt.ylabel("Top Products")
        plt.title("Top Products by Category")
        plt.show()
    @staticmethod
    def SalesbyDay():
        df=SARGA.LoadData()
        df=df.groupby("Date")["TotalSales"].agg(PerdaySale="sum").reset_index().sort_values(by="PerdaySale",ascending=False)
        print(df)
        plt.plot(df["Date"],df["PerdaySale"])
        plt.xlabel("Date")
        plt.ylabel("Perday Sale")
        plt.title("Perday Sale")
        plt.show()

SARGA.SalesbyDay()
