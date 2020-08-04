import DB_handler
from UI_Elements import *
from Retrieval import parse_date_time_input

dvir_path = "C:\\Users\\dvir levi\\PycharmProjects\\CDSS-Mini-Project\\project_db_test_publish.xlsx"
raz_path = "project_db_test_publish_1.xlsx"


def run_window():
    global ent_first_name, ent_last_name, ent_start_date, ent_start_hour, ent_start_minute, lbl_value
    global ent_end_date, ent_end_hour, ent_end_minute, ent_loinc_num
    global ent_view_date, ent_view_hour, ent_view_minute
    retrieval_H_window = tk.Tk()
    retrieval_H_window.geometry("500x350")
    create_label(col=2, row=0, text="loinc-num", window=retrieval_H_window)
    ent_loinc_num = create_entry(col=3, row=0, text="loinc-num", window=retrieval_H_window)
    create_label(col=2, row=1, text="First Name", window=retrieval_H_window)
    ent_first_name = create_entry(col=3, row=1, text="first_name", window=retrieval_H_window)
    create_label(col=2, row=2, text="Last Name", window=retrieval_H_window)
    ent_last_name = create_entry(col=3, row=2, text="last_name", window=retrieval_H_window)

    create_label(col=2, row=3, text="start date", window=retrieval_H_window)
    ent_start_date = create_date_entry(col=3, row=3, window=retrieval_H_window)
    create_label(col=2, row=4, text="hh:mm", window=retrieval_H_window)
    ent_start_hour = create_spinbox(col=3, row=4, max_value=23, min_value=0, window=retrieval_H_window)
    ent_start_minute = create_spinbox(col=4, row=4, max_value=59, min_value=0, window=retrieval_H_window)

    create_label(col=2, row=5, text="end date", window=retrieval_H_window)
    ent_end_date = create_date_entry(col=3, row=5, window=retrieval_H_window)
    create_label(col=2, row=6, text=" hh:mm", window=retrieval_H_window)
    ent_end_hour = create_spinbox(col=3, row=6, max_value=23, min_value=0, window=retrieval_H_window)
    ent_end_minute = create_spinbox(col=4, row=6, max_value=59, min_value=0, window=retrieval_H_window)

    create_label(col=2, row=7, text="date view", window=retrieval_H_window)
    ent_view_date = create_date_entry(col=3, row=7, window=retrieval_H_window)
    create_label(col=2, row=8, text="hh:mm", window=retrieval_H_window)
    ent_view_hour = create_spinbox(col=3, row=8, max_value=23, min_value=0, window=retrieval_H_window)
    ent_view_minute = create_spinbox(col=4, row=8, max_value=59, min_value=0, window=retrieval_H_window)

    create_button(col=4, row=9, text="submit", command=retrieve_history, window=retrieval_H_window)
    lbl_value = create_label(col=4, row=10, text="", window=retrieval_H_window)
    retrieval_H_window.mainloop()


def retrieve_history():
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()
    loinc_num = ent_loinc_num.get()

    valid_start_time_from = parse_date_time_input(ent_start_date, ent_start_hour, ent_start_minute)

    valid_start_time_to = parse_date_time_input(ent_end_date, ent_end_hour, ent_end_minute)

    transaction_time = parse_date_time_input(ent_view_date, ent_view_hour, ent_view_minute)

    print("hello")
    answer = DB_handler.retrieve(
        loinc_num=loinc_num,
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


def input_check(name, date, hours, minutes):
    if name == "" or not isinstance(hours, int) or not isinstance(minutes, int):
        return 1 == 0
