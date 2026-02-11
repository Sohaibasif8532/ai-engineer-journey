import os
import pandas as pd
import logging

file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(file_dir)
inputdata = os.path.join(project_root, "Data/input/input.csv")
Dtreeresult = os.path.join(project_root, "Data/output/Algorithm Results/decision_tree/decision_tree.csv")
Rforestresult = os.path.join(project_root, "Data/output/Algorithm Results/random_forest/r_forest_tree.csv")
logisticresult = os.path.join(project_root, "Data/output/Algorithm Results/logistic_regression/logistic_regression.csv")
MLData = os.path.join(project_root, "Data/output/ML Ready Data/MLdata.csv")

class Dataloader:

    def __init__(self,inputdata,Dtreeresult,Rforestresult,logisticresult,MLData):
        self.inputdata=inputdata
        self.Dtreeresult=Dtreeresult
        self.Rforestresult=Rforestresult
        self.logisticresult=logisticresult
        self.MLData=MLData
        self.df=None
    
    logging.basicConfig(
        filename="logs.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    def loaddata(self):
        if os.path.exists(self.inputdata):
            self.df=pd.read_csv(self.inputdata)
            logging.info("Data loaded successfully")
        else:
            logging.info("Data not found")



app=Dataloader(inputdata,Dtreeresult,Rforestresult,logisticresult,MLData)
app.loaddata()