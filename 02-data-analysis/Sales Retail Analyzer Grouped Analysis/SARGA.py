import pandas as pd
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

filedir=os.path.dirname(os.path.abspath(__file__))
datapath=os.path.join(filedir,"SARGA.csv")

class SARGA:

    def __init__(self):
        self.df=self.LoadData()

    def LoadData(self):
        if os.path.exists(datapath):
            df=pd.read_csv(datapath)
            return df
        else:
            print("File not found")
            sys.exit(1)

    def SalesByCategory(self):
        df=self.df.groupby("Category")["TotalSales"].agg(TotalSales="sum").reset_index().sort_values(by="TotalSales",ascending=False)
        print(df)
        plt.bar(df["Category"],df["TotalSales"])
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.title("Total Sales by Category")
        plt.show()


    def TopCategories(self):
        df=self.df.groupby("Category")["TotalSales"].agg(TopProducts="sum").reset_index().sort_values(by="TopProducts",ascending=False)
        print(df)
        plt.bar(df["Category"],df["TopProducts"])
        plt.xlabel("Category")
        plt.ylabel("Top Products")
        plt.title("Top Products by Category")
        plt.show()


    def SalesbyDay(self):
        df=self.df.groupby("Date")["TotalSales"].agg(PerdaySale="sum").reset_index().sort_values(by="PerdaySale",ascending=False)
        print(df)
        plt.plot(df["Date"],df["PerdaySale"])
        plt.xlabel("Date")
        plt.ylabel("Per day Sale")
        plt.title("Sales Per Day")
        plt.show()


    def CategoryPerformanceComparison(self):
        avg_per_cat = (
            self.df.groupby("Category")["TotalSales"]
            .mean()
            .reset_index(name="Average_Per_Category")
        )
        orders_per_cat = (
            self.df.groupby("Category")["OrderID"]
            .count()
            .reset_index(name="CountOrdersPerCategory")
        )
        orders_per_cat=orders_per_cat.sort_values(by="CountOrdersPerCategory",ascending=False)

        plt.bar(avg_per_cat["Category"], avg_per_cat["Average_Per_Category"])
        plt.xlabel("Category")
        plt.ylabel("Average Per Category")
        plt.title("Average Revenue Per Category")
        plt.show()

        plt.bar(orders_per_cat["Category"], orders_per_cat["CountOrdersPerCategory"])
        plt.xlabel("Category")
        plt.ylabel("Number of Orders")
        plt.title("Orders Count Per Category")
        plt.show()


    def FilterByDate(self,Date):
        df=self.df[self.df["Date"]==Date]
        df=df.groupby("Date")["TotalSales"].agg(SalesByDate="sum").reset_index().sort_values(by="SalesByDate",ascending=False)
        print(df)
        plt.bar(df["Date"],df["SalesByDate"])
        plt.xlabel("Date")
        plt.ylabel("Sales By Date")
        plt.title("Sales By Date")
        plt.show()


    def FilterByCategory(self,Category):
        df=self.df[self.df["Category"]==Category]
        df=df.groupby("Category")["TotalSales"].agg(SalesByCategory="sum").reset_index().sort_values(by="SalesByCategory",ascending=False)
        print(df)
        plt.bar(df["Category"],df["SalesByCategory"])
        plt.xlabel("Category")
        plt.ylabel("Sales By Category")
        plt.title("Sales By Category")
        plt.show()


    def FilterByCustomer(self,Customer):
        df=self.df[self.df["Customer"]==Customer]
        df=df.groupby("Customer")["TotalSales"].agg(SalesByCustomer="sum").reset_index().sort_values(by="SalesByCustomer",ascending=False)
        print(df)
        plt.bar(df["Customer"],df["SalesByCustomer"])
        plt.xlabel("Customer")
        plt.ylabel("Sales By Customer")
        plt.title("Sales By Customer")
        plt.show()



app=SARGA()
app.SalesByCategory()
app.TopCategories()
app.SalesbyDay()
app.CategoryPerformanceComparison()
app.FilterByDate("2022-01-01")
app.FilterByCategory("Electronics")
app.FilterByCustomer("Ali")


