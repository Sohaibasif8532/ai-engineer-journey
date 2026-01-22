import pandas as pd
import os
import json

class todoapp:
    tasklist=[]
    filepath= os.path.join(os.path.dirname(__file__),"todo.json")
    @staticmethod
    def loadtasks():
        if os.path.exists(todoapp.filepath):
            with open(todoapp.filepath, "r") as f:
                todoapp.tasklist=json.load(f)
        else:
            todoapp.tasklist=[]
    @staticmethod
    def savetasks():
        with open(todoapp.filepath, "w") as f:
            json.dump(todoapp.tasklist, f)

    def addtask():
        task = input("Enter your task : ")
        todoapp.tasklist.append(task)
        todoapp.savetasks()
        print("Task Added Successfully!\n")
    def DisplayTasks():
        todoapp.loadtasks()
        print("Your Todays Tasks are :", todoapp.tasklist)
    def Deletetask():
        deltask=int(input("Enter your Task No. to Delete:"))
        del todoapp.tasklist[deltask-1]
        todoapp.savetasks()
        print("Task deleted Successfully! \n")
    def completedTask():
        Completedtask=int(input("Enter a Task No. to mark as Completed:"))
        todoapp.tasklist[Completedtask-1]=todoapp.tasklist[Completedtask-1]+ "✅"
        todoapp.savetasks()
        print("Task marked as Completed Successfully! \n")
        
while True:
    print("\n Welcome to Todo App \n") 
    print("Enter 1 to add task")
    print("Enter 2 to display tasks")
    print("Enter 3 to delete task")
    print("Enter 4 to mark task as completed")
    print("Enter 5 to exit")
    choice =int (input())
    match choice:
        case 1:
            todoapp.addtask()
        case 2:
            todoapp.DisplayTasks()
        case 3:
            todoapp.Deletetask()
        case 4:
            todoapp.completedTask()
        case 5:
            break
