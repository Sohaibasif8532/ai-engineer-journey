import pandas as pd
import os
import numpy as np

class StudentMarksAnalyzer:
    scriptDir= os.path.dirname(os.path.abspath(__file__))
    csvPath=os.path.join(scriptDir, "StudentRecords.csv")
    
    df = pd.read_csv(csvPath)

    def AllStudentAnalysis():
        df=StudentMarksAnalyzer.df
        Average=pd.DataFrame()
        Average["Averages"]=df[["Math", "Computer", "English"]].mean(axis=1)
        Average["Names"]=df["Name"]
        print(Average)
        outputPath = os.path.join(StudentMarksAnalyzer.scriptDir, "StudentReccords.csv")
        Average.to_csv(outputPath, mode="a", header=False, index=False)

    def TopStudentAnalysis():
        df=StudentMarksAnalyzer.df
        DF=pd.DataFrame()
        DF["TopMarks"]=df[["Math", "Computer", "English"]].max(axis=1)
        DF["Names"]=df["Name"]
        print(DF)
        DF.to_csv("StudentRecords.csv", mode="a", header=False, index=False)

        outputPath=os.path.join(StudentMarksAnalyzer.scriptDir, "StudentReccords.csv")
        DF.to_csv(outputPath, mode="a", header=False, index=False)

    def ClassAveragemarks():
        df=StudentMarksAnalyzer.df
        DF=pd.DataFrame()
        DF["ClassAverage"]=df[["Math", "Computer", "English"]].mean(axis=1)
        print(DF)

    def belowPassGrade():
        df=StudentMarksAnalyzer.df
        DF=pd.DataFrame()
        DF["Math Failures"]=df[["Math"]]<50
        DF["English Failures"]=df[["English"]]<50
        DF["Computer Failures"]=df[["Computer"]]<50
        DF["Names"]=df["Name"]
        print(DF)
        outputPath=os.path.join(StudentMarksAnalyzer.scriptDir, "StudentReccords.csv")
        DF.to_csv(outputPath, mode="a", header=False, index=False)

while True:
    print("Welcome to Student Marks Analyzer")
    print("----------------------------------------------")
    Choice=input("1. Show all students & averages\n2. Show top student\n3. Show class average per subject\n4. Show students below passing marks\n5. Exit\n")
    match Choice:
        case "1":
            StudentMarksAnalyzer.AllStudentAnalysis()
        case "2":
            StudentMarksAnalyzer.TopStudentAnalysis()
        case "3":
            StudentMarksAnalyzer.ClassAveragemarks()
        case "4":
            StudentMarksAnalyzer.belowPassGrade()
        case "5":
            exit()
        case _:
            print("Invalid choice")