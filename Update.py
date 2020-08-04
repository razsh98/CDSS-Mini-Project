import pandas as pd

from UI_Elements import *

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"


def run_window():
    global ent_name, ent_date, ent_hour, ent_minute, lbl_value, ent_value, DB
    update_window = tk.Tk()
    update_window.geometry("500x350")

    lbl_name = create_label(col=2, row=1, text="name patient", window=update_window)
    ent_name = create_entry(col=3, row=1, text="name", window=update_window)
    lbl_date = create_label(col=2, row=2, text="date", window=update_window)
    ent_date = create_date_entry(col=3, row=2, window=update_window)
    lbl_time = create_label(col=2, row=3, text="hh:mm", window=update_window)
    ent_hour = create_spinbox(col=3, row=3, max_value=23, min_value=0, window=update_window)
    ent_minute = create_spinbox(col=4, row=3, max_value=59, min_value=0, window=update_window)

    global ent_date_view, ent_hour_view, ent_minute_view
    lbl_date_view = create_label(col=2, row=4, text="date view", window=update_window)
    ent_date_view = create_date_entry(col=3, row=4, window=update_window)
    lbl_time_view = create_label(col=2, row=5, text="hh:mm", window=update_window)
    ent_hour_view = create_spinbox(col=3, row=5, max_value=23, min_value=0, window=update_window)
    ent_minute_view = create_spinbox(col=4, row=5, max_value=59, min_value=0, window=update_window)

    lbl_value = create_label(col=2, row=6, text="value", window=update_window)
    ent_value = create_entry(col=3, row=6, text="value", window=update_window)

    btn_submit = create_button(col=4, row=7, text="submit", command=update, window=update_window)

    DB = pd.read_excel(raz_path)
    lbl_value = create_label(col=4, row=6, text="", window=update_window)
    update_window.mainloop()


def update():
    if DB is None:
        show_alert(title="DB loading error", info="cant load th BI DB")
    name = ent_name.get()
    date = ent_date.get()
    hours = ent_hour.get()
    minutes = ent_minute.get()
    fine = input_check(name, date, hours, minutes)
    if not fine:
        show_alert(title="input error", info="empty name or illegal time")


def input_check(name, date, hours, minutes):
    if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
        return 1 == 0

# run_window()
