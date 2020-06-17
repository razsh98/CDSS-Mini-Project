# import numpy as np
# import pandas as pd
import tkinter as tk
from UI_Elements import *
import Retrieval
import RetrieveHistory
import Update
import Delete

main_window = tk.Tk()
main_window.iconbitmap("favicon.ico")

def main():

    main_window.title("BiTemporal DB GUI built by the R&D Team")

    main_window.geometry('600x400')

    btn_retrieval = create_button(col=1, row=0, text="Retrieve", command=Retrieval.run_window, window=main_window)
    btn_retrieval_history = create_button(col=1, row=2, text="Retrieve History", command=RetrieveHistory.run_window, window=main_window)
    btn_update = create_button(col=1, row=4, text="Update", command=Update.run_window, window=main_window)
    btn_delete = create_button(col=1, row=6, text="Delete", command=Delete.run_window, window=main_window)

    main_window.mainloop()


main()
