import datefinder
import winsound
import datetime
import csv
import pandas as pd
from datetime import datetime
import pyttsx3
import schedule
import time
from twilio.rest import Client 
import smtplib 

engine = pyttsx3.init()

def currentTime():
        now = datetime.now().time()
        time_Rem = str(now.strftime("%I:%M %p"))
        return time_Rem
def sms(Text):
     
    account_sid = "YOUR SID"
    auth_token  = "YOUR TOKEN"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="Your number", 
        from_="number you get from twilio",
        body=Text)
    print(message.sid)
def email(Text):   
    s = smtplib.SMTP('smtp.gmail.com', 587)     
    s.starttls()    
    s.login("sender's email id", "sender's password") 
    message = Text
    s.sendmail("sender's email id", "Reciver's email id", message) 
    s.quit()
class Task_Rem:
    message = " "
    def task(self):
        tasks = pd.read_csv('Task.csv')
        sorted_Tasks = tasks.sort_values('time')
        X = sorted_Tasks.iloc[:,:-1].values
        y = sorted_Tasks.iloc[:,-1].values
        # print(X[i][0])
        #print(y[0])
        message = " "
        if y.size != 0:

            if(y[0]== currentTime()):
                engine.say(X[0][0])
                sms(X[0][0])
                email(X[0][0])
                engine.runAndWait() 
                delete = pd.read_csv('Task.csv',index_col = "Task")
                task= delete.drop(X[0][0])
                df = pd.DataFrame(task,columns = ['time'])
                print(df)
                df.to_csv("Task.csv",mode = 'w')
            message = "task completed"
        else:
            pass
        return message 




count = 0
while True:
    T = Task_Rem()
    p = T.task()
    count+=1
    if(p == "task completed"):
        T.task()
    elif(count==1):
        print("You Have No reminders to be reminded of")
