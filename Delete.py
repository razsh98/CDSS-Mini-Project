import tkinter as tk
from tkinter import messagebox
from UI_Elements import *
import pandas as pd

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "C:/_Information Systems Engineering/_Senior Year/Semester H/Decision Support Systems in Medicine/" \
           "Assignments/Mini Project/project_db_test_publish.xlsx"


def run_window():
    global ent_name,ent_date,ent_hour,ent_minute,lbl_value,DB

    delete_window = tk.Tk()
    delete_window.geometry("500x350")
    lbl_name = create_label(col=2, row=1, text="name patient", window=delete_window)
    ent_name = create_entry(col=3, row=1, text="name", window=delete_window)

    lbl_date = create_label(col=2, row=2, text="date", window=delete_window)
    ent_date=create_DateEntry(col=3, row=2, window=delete_window)
    lbl_time = create_label(col=2, row=3, text="hh:mm", window=delete_window)
    ent_hour=create_Spinbox(col=3, row=3, max=23,min=0,window=delete_window)
    ent_minute=create_Spinbox(col=4, row=3, max=59,min=0,window=delete_window)

    global ent_date_view, ent_hour_view, ent_minute_view
    lbl_date_view = create_label(col=2, row=4, text="date view", window=delete_window)
    ent_date_view = create_DateEntry(col=3, row=4, window=delete_window)
    lbl_time_view = create_label(col=2, row=5, text="hh:mm", window=delete_window)
    ent_hour_view = create_Spinbox(col=3, row=5, max=23, min=0, window=delete_window)
    ent_minute_view = create_Spinbox(col=4, row=5, max=59, min=0, window=delete_window)

    btn_submit = create_button(col=4, row=7, text="submit", command=delete, window=delete_window)
    DB = pd.read_excel(raz_path)
    lbl_value = create_label(col=4, row=5, text="", window=delete_window)
    delete_window.mainloop()


def delete():
    if DB is None:
        show_alert(title="DB loading error", info="cant load th BI DB")
    name=ent_name.get()
    date=ent_date.get()
    hours=ent_hour.get()
    minutes=ent_minute.get()
    fine=input_check(name,date,hours,minutes)
    if not fine:
        show_alert(title="input error", info="empty name or illegal time")


def input_check(name, date, hours,minutes):
    if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
        return 1 == 0

# run_window()
