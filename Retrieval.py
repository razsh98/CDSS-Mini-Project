import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from UI_Elements import *


dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "C:/_Information Systems Engineering/_Senior Year/Semester H/Decision Support Systems in Medicine/" \
           "Assignments/Mini Project/project_db_test_publish.xlsx"


def run_window():
    global ent_name,ent_date,ent_hour,ent_minute,lbl_vaule,DB
    global ent_date_view, ent_hour_view, ent_minute_view

    retrieval_window = tk.Tk()
    retrieval_window.geometry("500x350")
    lbl_name = create_label(col=2, row=1, text="name patient", window=retrieval_window)
    ent_name = create_entry(col=3, row=1, text="name", window=retrieval_window)
    lbl_date = create_label(col=2, row=2, text="date", window=retrieval_window)
    ent_date=create_DateEntry(col=3,row=2,window=retrieval_window)
    lbl_time = create_label(col=2, row=3, text="hh:mm", window=retrieval_window)
    ent_hour=create_Spinbox(col=3,row=3,max=23,min=0,window=retrieval_window)
    ent_minute=create_Spinbox(col=4,row=3,max=59,min=0,window=retrieval_window)

    lbl_date_view = create_label(col=2, row=4, text="date view", window=retrieval_window)
    ent_date_view = create_DateEntry(col=3, row=4, window=retrieval_window)
    lbl_time_view = create_label(col=2, row=5, text="hh:mm", window=retrieval_window)
    ent_hour_view = create_Spinbox(col=3, row=5, max=23, min=0, window=retrieval_window)
    ent_minute_view = create_Spinbox(col=4, row=5, max=59, min=0, window=retrieval_window)

    btn_submit = create_button(col=4, row=6, text="submit", command=retrive, window=retrieval_window)
    DB=pd.read_excel(raz_path)
    lbl_vaule = create_label(col=4, row=8,text="", window=retrieval_window)
    retrieval_window.mainloop()

def retrive():
    name=ent_name.get()
    date=ent_date.get()
    hours=ent_hour.get()
    minutes=ent_minute.get()
    date_view = ent_date_view.get()
    hours_view = ent_hour_view.get()
    minutes_view = ent_minute_view.get()
    fine0=input_check(name,date,hours,minutes)
    fine1=input_check(name,date_view,hours_view,minutes_view)
    # if not fine0 or not fine1:
    #     show_alert(title="input error", info="empty name or illegal time")
    #     return

    answer=""
    lbl_vaule['text']=answer
    print("spiched")



def input_check(name, date, hours,minutes):
    if name=="" or not isinstance(hours,int) or not isinstance(minutes,int):
        return 1==0

# print(pd.read_excel("C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"))
run_window()

