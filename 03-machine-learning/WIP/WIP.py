import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os


filedir=os.path.dirname(os.path.abspath(__file__))
data=os.path.join(filedir,"Data/Data.csv")

df=pd.read_csv(data)

X=df.drop("Price",axis=1)
Y=df["Price"]


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

print(X_train.shape)
print(X_eval.shape)
print(X_test.shape)

