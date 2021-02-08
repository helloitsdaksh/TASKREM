import datefinder
import winsound
import datetime
import csv
import pandas as pd
from datetime import datetime
import pyttsx3
engine = pyttsx3.init()


def currentTime():
    now = datetime.now().time()
    time_Rem = str(now.strftime("%I:%M %p"))
    return time_Rem

while True:
    def task():
        tasks = pd.read_csv('Task.csv')
        sorted_Tasks = tasks.sort_values('time')
        X = sorted_Tasks.iloc[:,:-1].values
        y = sorted_Tasks.iloc[:,-1].values
        
        for i in range(0,len(X)):    
            # print(X[i][0])
            # print(y[i])
            if(y[i] == currentTime()):
                engine.say(X[i][0])
                engine.runAndWait() 
                delete = pd.read_csv('Task.csv',index_col = "Task")
                task= delete.drop(X[i][0])
                df = pd.DataFrame(task,columns = ['time'])
                print(df)
                df.to_csv("Task.csv",mode = 'w')
            
            else:
                print("error")
task()






