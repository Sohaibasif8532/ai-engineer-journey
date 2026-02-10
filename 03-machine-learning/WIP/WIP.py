import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from numpy import hstack
import os
import datetime as dt


filedir=os.path.dirname(os.path.abspath(__file__))
data=os.path.join(filedir,"Data/Data.csv")
Result=os.path.join(filedir,"Data/Result.csv")

df=pd.read_csv(data)

df["Date"] = pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.month
df["Year"]=df["Date"].dt.year
df["Day"]=df["Date"].dt.day


X=df.drop(["Price per Unit","Date","Customer ID"],axis=1)
Y=df["Price per Unit"]


X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

X_train,X_eval,Y_train,Y_eval=train_test_split(
    X_train,
    Y_train,
    test_size=0.2,
    random_state=42
)



num_cols=X_train.select_dtypes(include=["int64","float64"]).columns
cat_cols=X_train.select_dtypes(include=["object"]).columns

scaler=StandardScaler()
OHE=OneHotEncoder(handle_unknown='ignore', sparse_output=False)

X_train_cat=OHE.fit_transform(X_train[cat_cols])
X_test_cat=OHE.transform(X_test[cat_cols])
X_eval_cat=OHE.transform(X_eval[cat_cols])

X_train_num=scaler.fit_transform(X_train[num_cols])
X_test_num=scaler.transform(X_test[num_cols])
X_eval_num=scaler.transform(X_eval[num_cols])

encoded_cols = OHE.get_feature_names_out(cat_cols)
final_cols = list(num_cols) + list(encoded_cols)

X_train_Final=hstack([X_train_num,X_train_cat])
X_test_Final=hstack([X_test_num,X_test_cat])
X_eval_Final=hstack([X_eval_num,X_eval_cat])

X_train_Final=pd.DataFrame(X_train_Final,columns=final_cols)
X_test_Final=pd.DataFrame(X_test_Final,columns=final_cols)
X_eval_Final=pd.DataFrame(X_eval_Final,columns=final_cols)

X_train_Final.to_csv(Result,index=False)
X_test_Final.to_csv(Result,index=False)
X_eval_Final.to_csv(Result,index=False)

model=RandomForestRegressor()
model.fit(X_train_Final,Y_train)

Y_predict=model.predict(X_train_Final)
Y_predict_test=model.predict(X_test_Final)
Y_predict_eval=model.predict(X_eval_Final)

def Evaluation(y_true,y_pred):
    mae=mean_absolute_error(y_true,y_pred)
    mse=mean_squared_error(y_true,y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(y_true,y_pred)
    
    print("MAE:",mae)
    print("MSE:",mse)
    print("RMSE:",rmse)
    print("R2:",r2)

Evaluation(Y_train,Y_predict)
Evaluation(Y_test,Y_predict_test)
Evaluation(Y_eval,Y_predict_eval)


print(X_train_Final.head())
