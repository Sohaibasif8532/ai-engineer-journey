import pandas as pd
import logging
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from dataloader import Dataloader, inputdata, Dtreeresult, Rforestresult, logisticresult, MLData
from numpy import hstack

class preprocessing:
        
    def __init__(self,df):
        self.df=df
    def Preprocess(self):

        Data=self.df.drop(["Date","Customer ID"],axis=1)

        num_cols=Data.select_dtypes(include=["int64","float64"]).columns
        cat_cols=Data.select_dtypes(include=["object"]).columns
        
        SS=StandardScaler()
        OHE=OneHotEncoder(handle_unknown="ignore",sparse_output=False)

        Xfitted=SS.fit_transform(Data[num_cols])
        Xcatfitted=OHE.fit_transform(Data[cat_cols])

        encodedcols=OHE.get_feature_names_out(cat_cols)
        final_cols= list(num_cols) + list(encodedcols)

        X_final=hstack([Xfitted,Xcatfitted])
        df=pd.DataFrame(X_final,columns=final_cols)
        df.to_csv(MLData,index=False)
        print("Data Preprocessed and Stored in MLData")
        logging.info(f"Data Preprocessed and Stored in MLData")








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