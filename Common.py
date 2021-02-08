import datefinder
import winsound
import datetime
import csv
import pandas as pd
from datetime import datetime
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()


def currentTime():
    now = datetime.now().time()
    time_Rem = str(now.strftime("%I:%M %p"))
    return time_Rem


def task():
    tasks = pd.read_csv('Task.csv')
    sorted_Tasks = tasks.sort_values('time')
    X = sorted_Tasks.iloc[:,:-1].values
    y = sorted_Tasks.iloc[:,-1].values
        # print(X[0][0])
        # print(y[0])
    while True:
        if(y[0] == currentTime()):
            engine.say(X[0][0])
            engine.runAndWait() 
            delete = pd.read_csv('Task.csv',index_col = "Task")
            task= delete.drop(X[0][0])
            df = pd.DataFrame(task,columns = ['time'])
            print(df)
            df.to_csv("Task.csv",mode = 'w')
            break
        
# task()

df = pd.read_csv('Task.csv') 

def addTask(Task):
    date_Time_Rem = datefinder.find_dates(Task)
    for i in date_Time_Rem:
        # print(i)
        time_Rem_normal= i.time()
        time_Rem_12hrs = time_Rem_normal.strftime('%I:%M %p')
        message = Task
    with open('Task.csv','a',newline='') as appendobj:
        append = csv.writer(appendobj)
        append.writerow([message,time_Rem_12hrs])      

def Input():
    while True:
        answer = input("Do you want to add a task:  (Y/N)")
        if answer == "Y" or answer == "y":
            Task = str(input("What should i remind you of:"))
            addTask(Task)
            
            

        elif answer == "N" or answer == "n":
            print("error")
            task()
            

