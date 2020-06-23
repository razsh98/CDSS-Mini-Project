import tkinter as tk
from tkinter import messagebox
from UI_Elements import *
import pandas as pd


dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "C:/_Information Systems Engineering/_Senior Year/Semester H/Decision Support Systems in Medicine/" \
           "Assignments/Mini Project/project_db_test_publish.xlsx"


def run_window():
    global ent_name,ent_start_date,ent_start_hour,ent_start_minute,lbl_value,DB
    global ent_end_date,ent_end_hour,ent_end_minute,ent_loinc_num
    retrieval_H_window = tk.Tk()
    retrieval_H_window.geometry("500x350")
    lbl_loinc_num = create_label(col=2, row=0, text="loinc-num", window=retrieval_H_window)
    ent_loinc_num = create_entry(col=3, row=0, text="loinc-num", window=retrieval_H_window)
    lbl_name = create_label(col=2, row=1, text="name patient", window=retrieval_H_window)
    ent_name = create_entry(col=3, row=1, text="name", window=retrieval_H_window)

    lbl_date1 = create_label(col=2, row=2, text="start date", window=retrieval_H_window)
    ent_start_date=create_DateEntry(col=3, row=2, window=retrieval_H_window)
    lbl_time = create_label(col=2, row=3, text="hh:mm", window=retrieval_H_window)
    ent_start_hour = create_Spinbox(col=3, row=3, max=23, min=0, window=retrieval_H_window)
    ent_start_minute = create_Spinbox(col=4, row=3, max=59, min=0, window=retrieval_H_window)

    lbl_date2 = create_label(col=2, row=4, text="end date", window=retrieval_H_window)
    ent_start_date = create_DateEntry(col=3, row=4, window=retrieval_H_window)
    lbl_time = create_label(col=2, row=5, text=" hh:mm", window=retrieval_H_window)
    ent_end_hour = create_Spinbox(col=3, row=5, max=23, min=0, window=retrieval_H_window)
    ent_end_minute = create_Spinbox(col=4, row=5, max=59, min=0, window=retrieval_H_window)

    btn_submit = create_button(col=4, row=6, text="submit", command=retrive_H, window=retrieval_H_window)
    DB = pd.read_excel(raz_path)
    lbl_value = create_label(col=4, row=5, text="", window=retrieval_H_window)
    retrieval_H_window.mainloop()


def retrive_H():
    if DB==None:
        show_alert(title="DB loading error", info="cant load th BI DB")
    name=ent_name.get()
    date=ent_start_date.get()
    hours=ent_start_hour.get()
    minutes=ent_start_minute.get()
    fine=input_check(name,date,hours,minutes)
    if not fine:
        show_alert(title="input error", info="empty name or illegal time")


def input_check(name, date, hours, minutes):
    if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
        return 1 == 0

# run_window()
