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
    s = tk.StringVar(master=window)
    entry = create_entry(col=col+1, row=row, text=s, window=window)
    s.set(entry_text)
    return entry


def create_date_entry(col, row, window, day, month, year):
    de = DateEntry(window, width=17, day=day, month=month, year=year, background='darkblue', foreground='white',
                   borderwidth=2)
    de.grid(row=row, column=col)
    return de


def create_spinbox(col, row, min_value, max_value, window):
    sb = tk.Spinbox(window, from_=min_value, to=max_value)
    sb.grid(row=row, column=col)
    return sb


def create_datetime_entry(
        col, row, window, date_label_text, time_label_text="hh:mm", default_day=17, default_month=5, default_year=18):
    create_label(col=col, row=row, text=date_label_text, window=window)
    ent_date = create_date_entry(
        col=col+1, row=row, window=window, day=default_day, month=default_month, year=default_year)
    create_label(col=col, row=row+1, text=time_label_text, window=window)
    ent_hour = create_spinbox(col=col+1, row=row+1, max_value=23, min_value=0, window=window)
    ent_minute = create_spinbox(col=col+2, row=row+1, max_value=59, min_value=0, window=window)
    return ent_date, ent_hour, ent_minute


def create_checkbox(col, row, label_text, window):
    var = tk.IntVar(master=window)
    checkbox = tk.Checkbutton(window, text=label_text, variable=var, onvalue=1, offvalue=0)
    checkbox.grid(column=col, row=row)
    return var, checkbox


def create_popup(answer):
    popup = tk.Tk()
    popup.geometry("400x400")
    scroll = tk.Scrollbar(master=popup, orient='vertical')
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    popup_text = tk.Text(master=popup, yscrollcommand=scroll.set)
    popup_text.pack(side=tk.TOP, fill=tk.X)
    scroll.config(command=popup_text.yview)

    for row in answer.iterrows():
        for column in row:
            popup_text.insert(tk.END, repr(column) + '\n')
        popup_text.insert(tk.END, "-----------------------------------------------\n")


def show_alert(title="Title", info="a Tk MessageBox"):
    messagebox.showinfo(title, info)


def close_window(window):
    messagebox.showinfo("Alert", "This window will now close")
    window.destroy()
