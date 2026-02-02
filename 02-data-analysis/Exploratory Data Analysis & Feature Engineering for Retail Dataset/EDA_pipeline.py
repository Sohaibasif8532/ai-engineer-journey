import numpy as np
import datetime 
import os
import matplotlib.pyplot as plt
import pandas as pd

filedir=os.path.dirname(os.path.abspath(__file__))
projectroot=filedir
inputData=os.path.join(projectroot,"data","input","data.csv")
outputData=os.path.join(projectroot,"data","output","EDA_Featured_output.csv")
logs=os.path.join(projectroot,"logs","EDA_logs.log")


class EDA_Pipeline:
    def __init__(self,inputData,outputData,logs):
        self.inputData=inputData
        self.outputData=outputData
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
        Stats=df.groupby("Category").describe()
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
        Stats.to_csv(self.outputData,index=False)
        with open(self.logs, "a") as f:
            f.write("*"*226)
            f.write("\n")
            f.write(Stats.to_string())
            f.write("\n")
            f.write("*"*226)
            f.write("\n")





app=EDA_Pipeline(inputData,outputData,logs)
app.loadData()
app.descriptive_stats()