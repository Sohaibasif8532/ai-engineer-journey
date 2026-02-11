import pandas as pd
import logging
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from dataloader import Dataloader, inputdata, Dtreeresult, Rforestresult, logisticresult, MLData
from numpy import hstack
print("Preprocessor file is running")
class preprocessing:
        
    def __init__(self,df):
        self.df=df
    def Preprocess(self):

        X=self.df.drop("Price per Unit",axis=1)
        Y=self.df["Price per Unit"]

        num_cols=X.select_dtypes(include=["int64","float64"]).columns
        cat_cols=X.select_dtypes(include=["object"]).columns
        
        SS=StandardScaler()
        OHE=OneHotEncoder(handle_unknown="ignore",sparse_output=False)

        Xfitted=SS.fit_transform(X[num_cols])
        Xcatfitted=OHE.fit_transform(X[cat_cols])

        X_final=hstack([Xfitted,Xcatfitted])
        df=pd.DataFrame(X_final)
        df.to_csv(MLData,index=False)

        print("yey",X_final)








if __name__=="__main__":
    loader=Dataloader(
        inputdata,
        Dtreeresult,
        Rforestresult,
        logisticresult,
        MLData
    )
    df=loader.loaddata()
    app=preprocessing(df)
    app.Preprocess()