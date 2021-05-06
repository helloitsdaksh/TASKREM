import tkinter as tk
import csv
from tkinter import filedialog, messagebox, ttk

import pandas as pd
updatedlist = []
# initalise the tkinter GUI

def viewtask():
    root = tk.Tk()

    root.geometry("500x500")
    root.pack_propagate(False)
    root.resizable(0, 0)  #make sure size of window is fixed

    # Frame for TreeView
    frame1 = tk.LabelFrame(root, text="Task Details")
    frame1.place(height=250, width=500)


    file_frame = tk.Frame(root)
    file_frame.place(height=100, width=400, rely=0.65, relx=0)

    button2 = tk.Button(file_frame, text="View Task", command=lambda: Load_excel_data())
    button2.place(rely=0.65, relx=0.30)
    button3=tk.Button(file_frame,text="remove record",command=lambda: removeselect())
    button3.place(rely=0.65, relx=0.50)

    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame1, orient="vertical",
                            command=tv1.yview)
    treescrollx = tk.Scrollbar(frame1, orient="horizontal",
                            command=tv1.xview)
    tv1.configure(xscrollcommand=treescrollx.set,
                yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")


    def removeselect():
        x=tv1.selection()




        for rec in x:
            item = tv1.set(rec)

            tv1.delete(rec)

            delete = pd.read_csv("Task.csv",index_col=0)
            task = delete.drop(item['task'])
            df = pd.DataFrame(task)

            df.to_csv("Task.csv",mode='w')

        return None






    def Load_excel_data():

        file_path = "Task.csv"
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)


        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        #tv1["column"] = list(df.columns)
        print(list(df.columns))
        tv1["columns"] = 'task','notify time'
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
    




        for row in df_rows:
            tv1.insert("", "end",
                    values=row)

        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    root.mainloop()



















































