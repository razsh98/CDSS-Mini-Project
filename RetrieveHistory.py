import pandas as pd
import DB_handler
from UI_Elements import *
from Retrieval import validate_not_empty, validate_dates, parse_date_time_input

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"


def run_window():
    global ent_first_name, ent_last_name, ent_start_date, ent_start_hour, ent_start_minute, lbl_value, DB
    global ent_end_date, ent_end_hour, ent_end_minute, ent_loinc_num
    global ent_view_date, ent_view_hour, ent_view_minute
    retrieval_H_window = tk.Tk()
    retrieval_H_window.geometry("500x350")
    lbl_loinc_num = create_label(col=2, row=0, text="loinc-num", window=retrieval_H_window)
    ent_loinc_num = create_entry(col=3, row=0, text="loinc-num", window=retrieval_H_window)
    lbl_first_name = create_label(col=2, row=1, text="First Name", window=retrieval_H_window)
    ent_first_name = create_entry(col=3, row=1, text="first_name", window=retrieval_H_window)
    lbl_last_name = create_label(col=2, row=2, text="Last Name", window=retrieval_H_window)
    ent_last_name = create_entry(col=3, row=2, text="last_name", window=retrieval_H_window)

    lbl_date1 = create_label(col=2, row=3, text="start date", window=retrieval_H_window)
    ent_start_date = create_DateEntry(col=3, row=3, window=retrieval_H_window)
    lbl_time = create_label(col=2, row=4, text="hh:mm", window=retrieval_H_window)
    ent_start_hour = create_spinbox(col=3, row=4, max=23, min=0, window=retrieval_H_window)
    ent_start_minute = create_spinbox(col=4, row=4, max=59, min=0, window=retrieval_H_window)

    lbl_date2 = create_label(col=2, row=5, text="end date", window=retrieval_H_window)
    ent_end_date = create_DateEntry(col=3, row=5, window=retrieval_H_window)
    lbl_time = create_label(col=2, row=6, text=" hh:mm", window=retrieval_H_window)
    ent_end_hour = create_spinbox(col=3, row=6, max=23, min=0, window=retrieval_H_window)
    ent_end_minute = create_spinbox(col=4, row=6, max=59, min=0, window=retrieval_H_window)

    lbl_view_date = create_label(col=2, row=7, text="date view", window=retrieval_H_window)
    ent_view_date = create_DateEntry(col=3, row=7, window=retrieval_H_window)
    lbl_view_time = create_label(col=2, row=8, text="hh:mm", window=retrieval_H_window)
    ent_view_hour = create_spinbox(col=3, row=8, max=23, min=0, window=retrieval_H_window)
    ent_view_minute = create_spinbox(col=4, row=8, max=59, min=0, window=retrieval_H_window)

    btn_submit = create_button(col=4, row=9, text="submit", command=retrieve_h, window=retrieval_H_window)
    DB = pd.read_excel(raz_path)
    lbl_value = create_label(col=4, row=10, text="", window=retrieval_H_window)
    retrieval_H_window.mainloop()


def retrieve_history():
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()

    valid_start_time_from = parse_date_time_input(ent_start_date, ent_start_hour, ent_start_minute)

    valid_start_time_to = parse_date_time_input(ent_end_date, ent_end_hour, ent_end_minute)

    transaction_time = parse_date_time_input(ent_view_date, ent_view_hour, ent_view_minute)

    print("hello")
    answer = DB_handler.retrieve(
        first_name=first_name,
        last_name=last_name,
        valid_start_time=valid_start_time_from,
        valid_start_time_end=valid_start_time_to,
        transaction_time=transaction_time,
    )
    spaced_entries = ''
    for entry in answer.iterrows():
        spaced_entries = repr(entry) + '\n'
    lbl_value['text'] = spaced_entries


def retrieve_h():
    if DB is None:
        show_alert(title="DB loading error", info="cant load th BI DB")
    name = ent_first_name.get()
    date = ent_start_date.get()
    hours = ent_start_hour.get()
    minutes = ent_start_minute.get()
    fine = input_check(name, date, hours, minutes)
    if not fine:
        show_alert(title="input error", info="empty name or illegal time")


def input_check(name, date, hours, minutes):
    if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
        return 1 == 0

# run_window()
