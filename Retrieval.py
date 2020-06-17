import tkinter as tk
from tkinter import messagebox
from UI_Elements import *


def run_window():
    retrieval_window = tk.Tk()
    retrieval_window.geometry("500x350")
    btn_test = create_button(col=1, row=1, text="Test", command=click, window=retrieval_window)
    lbl_test = create_label(col=2, row=1, text="Test", window=retrieval_window)
    ent_test = create_entery(col=3, row=1, text="Test", window=retrieval_window)



