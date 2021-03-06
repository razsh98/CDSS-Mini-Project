import DB_handler
from UI_Elements import *
from datetime import datetime

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"


def run_window():
    global ent_first_name, ent_last_name, ent_date, ent_hour, ent_minute, lbl_value
    global ent_date_view, ent_hour_view, ent_minute_view, var, checkbox

    retrieval_window = tk.Tk()
    retrieval_window.geometry("500x350")
    ent_first_name = create_labeled_entry(
        col=2,
        row=1,
        entry_text="Eli",
        label_text="First Name",
        window=retrieval_window)

    ent_last_name = create_labeled_entry(
        col=2,
        row=2,
        entry_text="Call",
        label_text="Last Name",
        window=retrieval_window)

    ent_date, ent_hour, ent_minute = create_datetime_entry(
        col=2,
        row=3,
        date_label_text="date",
        default_day=18,
        default_month=5,
        default_year=2018,
        window=retrieval_window)

    ent_date_view, ent_hour_view, ent_minute_view = create_datetime_entry(
        col=2,
        row=5,
        date_label_text="date view",
        default_day=22,
        default_month=5,
        default_year=2018,
        window=retrieval_window)

    var, checkbox = create_checkbox(
        col=4,
        row=5,
        label_text="now",
        window=retrieval_window)

    # now = IntVar(name="checkbox_int_var", master=retrieval_window)
    # Checkbutton(retrieval_window, text="now", variable=now).grid(column=4, row=5)

    create_button(col=4, row=7, text="submit", command=retrieve, window=retrieval_window)
    lbl_value = create_label(col=0, row=9, text="", window=retrieval_window, colspan=5, rowspan=10)
    retrieval_window.mainloop()


def retrieve():
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()

    valid_start_time = parse_date_time_input(ent_date, ent_hour, ent_minute)
    transaction_time = parse_date_time_input(ent_date_view, ent_hour_view, ent_minute_view)
    if var.get():
        transaction_time = datetime.now()

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

        create_popup(answer=answer)


def parse_date_time_input(date, hours, minutes):

    date_val = date.get()
    hours_val = hours.get()
    minutes_val = minutes.get()

    if validate_dates(hours_val, minutes_val):
        if int(hours_val) < 10:
            hours_val = "0" + hours_val
        if int(minutes_val) < 10:
            minutes_val = "0" + minutes_val
        return datetime.strptime(date_val + " " + hours_val + ":" + minutes_val + ":00", '%m/%d/%y %H:%M:%S')
        # return date_val + " " + hours_val + ":" + minutes_val + ":00"
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


# run_window()
