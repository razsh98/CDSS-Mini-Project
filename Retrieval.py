import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from UI_Elements import *


def run_window():
    global ent_name,ent_date,ent_hour,ent_minute,lbl_vaule,DB
    retrieval_window = tk.Tk()
    retrieval_window.geometry("500x350")
    lbl_name = create_label(col=2, row=1, text="name patient", window=retrieval_window)
    ent_name = create_entery(col=3, row=1, text="name", window=retrieval_window)
    lbl_date = create_label(col=2, row=2, text="date", window=retrieval_window)
    ent_date=create_DateEntry(col=3,row=2,window=retrieval_window)
    lbl_time = create_label(col=2, row=3, text="hh:mm", window=retrieval_window)
    ent_hour=create_Spinbox(col=3,row=3,max=23,min=0,window=retrieval_window)
    ent_minute=create_Spinbox(col=4,row=3,max=59,min=0,window=retrieval_window)
    btn_submit = create_button(col=4, row=4, text="submit", command=retrive, window=retrieval_window)
    DB=pd.read_excel("path")
    lbl_vaule = create_label(col=4, row=5,text="", window=retrieval_window)
    retrieval_window.mainloop()

def retrive():
    name=ent_name.get()
    date=ent_date.get()
    hours=ent_hour.get()
    minutes=ent_minute.get()
    fine=input_check(name,date,hours,minutes)
    if not fine:
        show_alert(title="input error", info="empty name or illegal time")



def input_check(name, date, hours,minutes):
    if name=="" or not isinstance(hours,int) or not isinstance(minutes,int):
        return 1==0


run_window()

