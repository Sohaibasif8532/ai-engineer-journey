from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import joblib
import pandas as pd
import numpy as np
import logging
import os
from dataloader import MLData, ModelPath

class ModelTraining:
    
    def __init__(self,df):
        self.df=df

    def ModelTrainer(self):
        x=self.df.drop("Price per Unit",axis=1)
        y=self.df["Price per Unit"]

        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        x_train,x_eval,y_train,y_eval=train_test_split(x_train,y_train,test_size=0.2,random_state=42)

        rf=RandomForestRegressor(n_estimators=100,random_state=42)
        rfresult=rf.fit(x_train,y_train)
        y_pred=rfresult.predict(x_eval)
        joblib.dump(rfresult, ModelPath)
        print(f"Model saved Successfully at: {ModelPath}")

        mse=mean_squared_error(y_eval,y_pred)
        print("Mean Squared Error:",mse)
        return y_pred

if __name__=="__main__":
    print("Loading data and starting training...")
    df_ml=pd.read_csv(MLData)
    model_app=ModelTraining(df_ml)
    model_app.ModelTrainer()
    print("Training complete.")
