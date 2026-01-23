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
        Average.to_csv(outputPath, mode="w", header=False, index=False)

    def TopStudentAnalysis():
        df=StudentMarksAnalyzer.df
        DF=pd.DataFrame()
        DF["Average"]=df[["Math", "Computer", "English"]].mean(axis=1)
        TopMarks=df[df["Average"]]
        TopAvg=DF["Average"].max()
        TopStudent=DF[DF["Average"]==TopAvg]["Name"].values
        print("Top Student:", TopStudent, "with an average of:", TopAvg)
        outputPath=os.path.join(StudentMarksAnalyzer.scriptDir, "StudentReccords.csv")
        TopStudent.to_csv(outputPath, mode="w", header=False, index=False)

    def ClassAveragemarks():
        df=StudentMarksAnalyzer.df
        DF=pd.DataFrame()
        DF["ClassAverage"]=df[["Math", "Computer", "English"]].mean()
        print(DF)

    def belowPassGrade():
        df=StudentMarksAnalyzer.df
        failures = {}
        for subject in ['Math','English','Computer']:
            failed_students = df[df[subject] < 50]['Name'].tolist()
            failures[subject] = failed_students
        print("Failures by subject:", failures)

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