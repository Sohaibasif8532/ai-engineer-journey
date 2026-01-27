import pandas as pd
import logging
import sys
import os
import matplotlib.pyplot as plt
class LARG:
    FileDir=os.path.dirname(os.path.abspath(__file__))
    csvPath=os.path.join(FileDir, "LARG.csv")
    logPath=os.path.join(FileDir, "LARG.log")
    LARGError=os.path.join(FileDir, "LARGError.log")
    logging.basicConfig(
        filename=(LARGError),
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
        
    def CountErrors():
        LARGErrorCount=0
        ErrosPerDay= 0
        if os.path.exists(LARG.logPath) and os.path.getsize(LARG.logPath) > 0:
            print("Log File Exists")
            logging.info("Log File Exists")
        else:
            print("Log File Does Not Exist")
            logging.info("Log File Does Not Exist")
        if os.path.exists(LARG.csvPath) and os.path.getsize(LARG.csvPath) > 0:
            print("CSV File Exists")
            logging.info("CSV File Exists")
        
        else:
            print("CSV File Does Not Exist")
            logging.info("CSV File Does Not Exist")
            


        df=pd.read_csv(LARG.csvPath)
        with open(LARG.logPath , "r") as file:
            for line in file:
                if "Error" in line:
                    ErrosPerDay= df['Date'].value_counts()
                    print(f"Error Exists :{line}")
                    logging.info(f"Error Exists :{line} Error Count So far : {LARGErrorCount}")
                    LARGErrorCount +=1
            if LARGErrorCount == 0:
                print("No Errors Found")
                logging.info("No Errors Found")
            else:
                print(f"Total Errors Found: {LARGErrorCount}")
                logging.info(f"Total Errors Found: {LARGErrorCount}")
                

                plt.plot(LARGErrorCount)
                plt.show()

                


LARG.CountErrors()
        
            
        