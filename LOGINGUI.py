import tkinter as tk
from tkinter import *
from functools import partial
from GUI import *
import os



if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

#window
tkWindow = tk.Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

def validateLogin(username, password):
	if username.get() == 'hi5daksh' and password.get() == 'angrybirds':
		messagebox.showinfo('Login Successful', 'User Verified')
		tkWindow.destroy()
		gui()
	else :
		messagebox.showerror('Login Failed', 'User Not Verified')

	return 

#username label and text entry box
usernameLabel = tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = tk.Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()