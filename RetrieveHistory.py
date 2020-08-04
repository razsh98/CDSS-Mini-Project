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

    ent_loinc_num = create_labeled_entry(
        col=2,
        row=0,
        entry_text="loinc-num",
        label_text="loinc-num",
        window=retrieval_H_window)

    ent_first_name = create_labeled_entry(
        col=2,
        row=1,
        entry_text="loinc-num",
        label_text="loinc-num",
        window=retrieval_H_window)

    ent_last_name = create_labeled_entry(
        col=2,
        row=2,
        entry_text="loinc-num",
        label_text="loinc-num",
        window=retrieval_H_window)

    ent_start_date, ent_start_hour, ent_start_minute = create_datetime_entry(
        col=2,
        row=3,
        date_label_text="start date",
        window=retrieval_H_window,
    )

    ent_end_date, ent_end_hour, ent_end_minute = create_datetime_entry(
        col=2,
        row=5,
        date_label_text="end date",
        window=retrieval_H_window,
    )

    ent_start_date, ent_start_hour, ent_start_minute = create_datetime_entry(
        col=2,
        row=7,
        date_label_text="date view",
        window=retrieval_H_window,
    )

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
