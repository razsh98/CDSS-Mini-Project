import tkinter as tk
from tkinter import messagebox
from UI_Elements import *


def run_window():
    delete_window = tk.Tk()
    delete_window.geometry("500x350")
    btn_test = create_button(col=1, row=0, text="Test", command=click, window=delete_window)