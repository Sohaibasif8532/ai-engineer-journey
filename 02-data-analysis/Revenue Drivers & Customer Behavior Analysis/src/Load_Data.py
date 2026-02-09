import os
import pandas as pd
import logging

filedir=os.path.dirname(os.path.abspath(__file__))
projectroot=os.path.dirname(filedir)
inputdata=os.path.join(projectroot,"data","input","input.csv")
cleaned=os.path.join(projectroot,"data","output","cleaned","cleaned.csv")
featured=os.path.join(projectroot,"data","output","features","features.csv")
analysis=os.path.join(projectroot,"data","output","analysis","analysis.csv")
logfiles=os.path.join(projectroot,"logs","logs.log")
visuals=os.path.join(projectroot,"data","output","visuals")

class Dataloader:
    def __init__(self, inputdata, cleaned, featured, logfiles, analysis, visuals):
        self.inputdata=inputdata
        self.cleaned=cleaned
        self.featured=featured
        self.logfiles=logfiles
        self.analysis=analysis
        self.visuals=visuals
        self.snapshots={}
 
        logging.basicConfig(
            filename=self.logfiles,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def loadData(self):
        if os.path.exists(self.inputdata):
            self.df=pd.read_csv(self.inputdata)
            logging.info("Data Loaded Successfully")
            return self.df
        else:
            logging.info("File Not Found")
            self.df = None

    def save_data(self, df, file_path, columns=None):
        if columns:
            df[columns].to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, index=False)
        logging.info(f"Data Saved to {file_path}")
        print(f"Data Saved to {file_path}")