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


def create_DateEntry(col, row, window):
    de = DateEntry(window, width=17, year=2019, month=6, day=22, background='darkblue', foreground='white',
                   borderwidth=2)
    de.grid(row=row, column=col)
    return de


def create_spinbox(col, row, max, min, window):
    sb = tk.Spinbox(window, from_=min, to=max)
    sb.grid(row=row, column=col)
    return sb


def show_alert(title="Title", info="a Tk MessageBox"):
    messagebox.showinfo(title, info)


def close_window(window):
    messagebox.showinfo("Alert", "This window will now close")
    window.destroy()
