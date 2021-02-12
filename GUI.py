import tkinter as tk
from tkinter import Label,Entry,Button
from tkinter import messagebox
import os ,time,winsound
import csv
import pandas as pd
import datetime
import datefinder
from datetime import datetime
import pyttsx3
import schedule
import time

engine = pyttsx3.init()

def createWidget():
    label1 = Label(root,text = "Enter the message with time",font=('calibre',10, 'bold'))
    label1.grid(row = 1,column =1, padx=(10,10),pady=(10,10))
    global entry1
    entry1 = Entry(root, width=30)
    entry1.grid(row = 1,column =2, padx=(5,5),pady=(10,10))
    but = Button(root,text = "Submit",width = 20,command =submit) 
    but.grid(row = 2,column = 2)

def submit():
    Task = entry1.get()
    date_Time_Rem = datefinder.find_dates(Task)
    for i in date_Time_Rem:
        # print(i)
        time_Rem_normal= i.time()
        time_Rem_12hrs = time_Rem_normal.strftime('%I:%M %p')
        message = Task
    with open('Task.csv','a',newline='') as appendobj:
        append = csv.writer(appendobj)
        append.writerow([message,time_Rem_12hrs])
    


root = tk.Tk()
root.title("TASKREM")
root.geometry("400x75")
createWidget()
root.mainloop()