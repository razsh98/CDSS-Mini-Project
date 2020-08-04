import DB_handler
from UI_Elements import *

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"

ent_first_name = ent_last_name = ent_date = ent_hour = ent_minute = lbl_value = tk.Entry()
ent_date_view = ent_hour_view = ent_minute_view = tk.Entry()

last_row = 0


def run_window():
    global ent_first_name, ent_last_name, ent_date, ent_hour, ent_minute, lbl_value
    global ent_date_view, ent_hour_view, ent_minute_view, last_row

    retrieval_window = tk.Tk()
    retrieval_window.geometry("500x350")
    lbl_first_name = create_label(col=2, row=1, text="First Name", window=retrieval_window)
    ent_first_name = create_entry(col=3, row=1, text="first_name", window=retrieval_window)
    lbl_last_name = create_label(col=2, row=2, text="Last Name", window=retrieval_window)
    ent_last_name = create_entry(col=3, row=2, text="last_name", window=retrieval_window)
    lbl_date = create_label(col=2, row=3, text="date", window=retrieval_window)
    ent_date = create_DateEntry(col=3, row=3, window=retrieval_window)
    lbl_time = create_label(col=2, row=4, text="hh:mm", window=retrieval_window)
    ent_hour = create_spinbox(col=3, row=4, max=23, min=0, window=retrieval_window)
    ent_minute = create_spinbox(col=4, row=4, max=59, min=0, window=retrieval_window)

    lbl_date_view = create_label(col=2, row=5, text="date view", window=retrieval_window)
    ent_date_view = create_DateEntry(col=3, row=5, window=retrieval_window)
    lbl_time_view = create_label(col=2, row=6, text="hh:mm", window=retrieval_window)
    ent_hour_view = create_spinbox(col=3, row=6, max=23, min=0, window=retrieval_window)
    ent_minute_view = create_spinbox(col=4, row=6, max=59, min=0, window=retrieval_window)

    btn_submit = create_button(col=4, row=7, text="submit", command=retrieve, window=retrieval_window)
    lbl_value = create_label(col=0, row=9, text="", window=retrieval_window, colspan=5, rowspan=10)
    retrieval_window.mainloop()


def retrieve():
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()

    valid_start_time = parse_date_time_input(ent_date, ent_hour, ent_minute)

    transaction_time = parse_date_time_input(ent_date_view, ent_hour_view, ent_minute_view)

    if validate_not_empty(first_name) and \
            validate_not_empty(last_name) and \
            valid_start_time != "" and \
            transaction_time != "":

        print("hello")
        answer = DB_handler.retrieve(
            first_name=first_name,
            last_name=last_name,
            valid_start_time=valid_start_time,
            transaction_time=transaction_time,
            limit=1
        )
        spaced_entries = ''
        for entry in answer.iterrows():
            spaced_entries = repr(entry) + '\n'
        lbl_value['text'] = spaced_entries


def parse_date_time_input(date, hours, minutes):

    date_val = date.get()
    hours_val = hours.get()
    minutes_val = minutes.get()

    if validate_dates(hours_val, minutes_val):
        if int(hours_val) < 10:
            hours_val = "0" + hours_val
        if int(minutes_val) < 10:
            minutes_val = "0" + minutes_val
        return date_val + " " + hours_val + ":" + minutes_val
    else:
        return ""


def validate_dates(hours, minutes):
    if hours is not None:
        if hours.isdigit():
            hours = int(hours)
            if hours >= 0:
                if hours < 24:
                    if minutes is not None:
                        if minutes.isdigit():
                            minutes = int(minutes)
                            if minutes >= 0:
                                if minutes < 60:
                                    return True
    show_alert(
        title="Input Error",
        info="Error: Illegal Time!"
    )
    return False


def validate_not_empty(field):
    if field is not None:
        if field != "":
            return True
    show_alert(
        title="Input Error",
        info="Error: Mandatory fields are empty!"
    )
    return False


# def input_check(name, date, hours, minutes):
#     if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
#         return 1 == 0


run_window()
