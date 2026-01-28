import os
import logging
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import re
import sys


class LARG:
    FileDir = os.path.dirname(os.path.abspath(__file__))
    logPath = os.path.join(FileDir, "LARG.log")
    LARGError = os.path.join(FileDir, "LARGError.log")

    logging.basicConfig(
        filename=LARGError,
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )

    @staticmethod
    def CountErrors():
        errorCountDay = 0
        warningCountDay = 0
        infoCountDay = 0
        dates = []
        with open (LARG.logPath, "r") as file:
            lines= file.readlines()
            for line in lines:
                if "Error" in line:
                    print("Error")
                    errorCountDay += 1
                    match = re.search(r"\d{4}-\d{2}-\d{2}", line)
                    if match:
                        dates.append(match.group())
                elif "Warning" in line:
                    print("Warning")
                    warningCountDay += 1
                elif "Info" in line:
                    print("Info")
                    infoCountDay += 1
        print("Total Error Count :", errorCountDay)
        print("Total Warning Count :", warningCountDay)
        print("Total Info Count :", infoCountDay)
        logging.info("Total Error Count :" + str(errorCountDay))
        logging.info("Total Warning Count :" + str(warningCountDay))
        logging.info("Total Info Count :" + str(infoCountDay))

        totalErrorCount=errorCountDay
        totalWarningCount=warningCountDay
        totalInfoCount=infoCountDay

        categories = ["Error", "Warning", "Info"]
        counts = [totalErrorCount, totalWarningCount, totalInfoCount]
        date_counts = Counter(dates)
        
        plt.plot(list(date_counts.keys()), list(date_counts.values()))
        plt.xlabel("Date")
        plt.ylabel("Error Count")
        plt.title("Errors Over Time")
        plt.xticks(rotation=45)
        plt.show()

        plt.plot(list(date_counts.keys()), list(date_counts.values()), marker='o')
        plt.xlabel("Date")
        plt.ylabel("Error Count")
        plt.title("Error Count")
        plt.show()
       
           



if __name__ == "__main__":
    inputP= int(input("Press 1 to Count Errors, Warnings and Info: "))
    if inputP == 1:
        LARG.CountErrors()
    else:
        print("Invalid Input")
        sys.exit()
