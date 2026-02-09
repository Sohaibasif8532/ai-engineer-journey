from Load_Data import Dataloader, inputdata, cleaned, featured, logfiles, analysis, visuals
from Cleaning import DataCleaner
from Feature_engineering import Feature_Engineering
from Exploratory_Analysis_Charts import Exploratory_Analysis

def main():
    loader = Dataloader(inputdata, cleaned, featured, logfiles, analysis, visuals)
    df = loader.loadData()

    if df is not None:
        cleaner = DataCleaner(df)
        cleaner.validate_data()
        cleaner.CleanNumericColumns()
        loader.save_data(cleaner.df, cleaned)
        engineer = Feature_Engineering(cleaner.df) 
        engineer.TargetVariable()
        engineer.Customer_total_spend()
        engineer.AverageOrderValue()
        engineer.PurchaseFrequency()
        engineer.PurchaseRecency()
        engineer.CategoryDiversity()
        engineer.Aggregations(threshold=900)      
        feature_columns = [
            "Customer_ID", "Transaction_ID", "High Value Transaction", 
            "Repeating Customer", "Customer Total Spend", "Average Order Value", 
            "Purchase Frequency", "Purchase Recency", "Category Diversity",
            "High/Low Value Customers", "Most Revenue Segment", "Repeating Behavior Pattern"
        ]
        loader.save_data(engineer.df, featured, columns=feature_columns)

        explorer = Exploratory_Analysis(engineer.df, visuals)
        explorer.ExploratoryAnalysis()

if __name__ == "__main__":
    main()
