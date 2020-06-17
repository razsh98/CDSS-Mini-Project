import tkinter as tk
from tkinter import messagebox


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

def create_entery(col, row, text, window):
    height = 1
    width = 15
    entery = tk.Entry(window,
                    text=text)
    entery.grid(column=col, row=row)
    return entery

def create_label(col, row, text, window):
    height = 1
    width = 15
    label = tk.Label(window,
                    text=text)
    label.grid(column=col, row=row)
    return label

def click():
    messagebox.showinfo("Title", "a Tk MessageBox")


def close_window(window):
    messagebox.showinfo("Alert", "This window will now close")
    window.destroy()

