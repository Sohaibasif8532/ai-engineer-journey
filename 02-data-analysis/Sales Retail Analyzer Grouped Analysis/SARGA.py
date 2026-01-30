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
    def TopCategories():
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
        plt.ylabel("Per day Sale")
        plt.title("Sales Per Day")
        plt.show()

    @staticmethod
    def CategoryPerformanceComparison():
        raw=SARGA.LoadData()
        df=raw.groupby("Category")["TotalSales"].agg(Average_Per_Category="mean").reset_index().sort_values(by="Average_Per_Category",ascending=False)
        CountOrdersPerCategory=raw.groupby("OrderID")["Category"].agg(CountOrdersPerCategory="nunique").reset_index().sort_values(by="CountOrdersPerCategory",ascending=False)
        print(df, CountOrdersPerCategory)
        CountOrdersPerCategory=CountOrdersPerCategory.sort_values(by="CountOrdersPerCategory",ascending=False)

        plt.bar(df["Category"],df["Average_Per_Category"])
        plt.xlabel("Category")
        plt.ylabel("Average Per Category")
        plt.title("Average Per Category")
        plt.show()

    @staticmethod
    def FilterByDate(Date):
        df=SARGA.LoadData()
        df=df[df["Date"]==Date]
        df=df.groupby("Date")["TotalSales"].agg(SalesByDate="sum").reset_index().sort_values(by="SalesByDate",ascending=False)
        print(df)
        plt.bar(df["Date"],df["SalesByDate"])
        plt.xlabel("Date")
        plt.ylabel("Sales By Date")
        plt.title("Sales By Date")
        plt.show()

    @staticmethod
    def FilterByCategory(Category):
        df=SARGA.LoadData()
        df=df[df["Category"]==Category]
        df=df.groupby("Category")["TotalSales"].agg(SalesByCategory="sum").reset_index().sort_values(by="SalesByCategory",ascending=False)
        print(df)
        plt.bar(df["Category"],df["SalesByCategory"])
        plt.xlabel("Category")
        plt.ylabel("Sales By Category")
        plt.title("Sales By Category")
        plt.show()
        
    @staticmethod
    def FilterByCustomer(Customer):
        df=SARGA.LoadData()
        df=df[df["Customer"]==Customer]
        df=df.groupby("Customer")["TotalSales"].agg(SalesByCustomer="sum").reset_index().sort_values(by="SalesByCustomer",ascending=False)
        print(df)
        plt.bar(df["Customer"],df["SalesByCustomer"])
        plt.xlabel("Customer")
        plt.ylabel("Sales By Customer")
        plt.title("Sales By Customer")
        plt.show()

SARGA.FilterByCategory("Electronics")
SARGA.FilterByDate("2022-01-01")
SARGA.SalesbyDay()
SARGA.CategoryPerformanceComparison()
SARGA.TopCategories()
SARGA.FilterByCustomer("Ali")


