import csv
import pandas as pd
import datetime
import datefinder
from datetime import datetime

df = pd.read_csv('Task.csv') 
with open('Task.csv','r') as readobj:
    read = csv.reader(readobj)
    rows = list(read)

   



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


   

answer = input("Do you want to add a task:  (Y/N)")
while True:
    if answer == "Y" or answer == "y":
        Task = str(input("What should i remind you of:"))
        addTask(Task)

    elif answer == "N" or answer == "n":
        print("hello")
