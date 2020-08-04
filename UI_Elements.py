import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry


def create_button(col, row, text, command, window):
    height = 1
    width = 15
    btn = tk.Button(window,
                    command=command,
                    height=height,
                    text=text,
                    width=width)
    btn.grid(column=col, row=row)
    return btn


def create_entry(col, row, text, window):
    entry = tk.Entry(window, text=text)
    entry.grid(column=col, row=row)
    return entry


def create_label(col, row, text, window, colspan=1, rowspan=1):
    label = tk.Label(window,
                     text=text)
    label.grid(column=col, row=row, columnspan=colspan, rowspan=rowspan)
    return label


def create_labeled_entry(col, row, entry_text, label_text, window, colspan=1, rowspan=1):
    create_label(col=col, row=row, text=label_text, window=window, colspan=colspan, rowspan=rowspan)
    entry = create_entry(col=col+1, row=row, text=entry_text, window=window)
    return entry


def create_date_entry(col, row, window):
    de = DateEntry(window, width=17, year=2018, month=5, day=17, background='darkblue', foreground='white',
                   borderwidth=2)
    de.grid(row=row, column=col)
    return de


def create_spinbox(col, row, min_value, max_value, window):
    sb = tk.Spinbox(window, from_=min_value, to=max_value)
    sb.grid(row=row, column=col)
    return sb


def create_datetime_entry(col, row, date_label_text, window, time_label_text="hh:mm"):
    create_label(col=col, row=row, text=date_label_text, window=window)
    ent_date = create_date_entry(col=col+1, row=3, window=window)
    create_label(col=col, row=row+1, text=time_label_text, window=window)
    ent_hour = create_spinbox(col=col+1, row=row+1, max_value=23, min_value=0, window=window)
    ent_minute = create_spinbox(col=col+2, row=row+1, max_value=59, min_value=0, window=window)
    return ent_date, ent_hour, ent_minute


def show_alert(title="Title", info="a Tk MessageBox"):
    messagebox.showinfo(title, info)


def close_window(window):
    messagebox.showinfo("Alert", "This window will now close")
    window.destroy()
