import tkinter as tk
from tkinter import messagebox
from UI_Elements import *


def run_window():
    update_window = tk.Tk()
    update_window.geometry("500x350")
    btn_test = create_button(col=1, row=0, text="Test", command=click, window=update_window)