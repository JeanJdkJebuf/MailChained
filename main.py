"""
Welcome to MailChained program

To launch program, simply type
'
python main.py
'

Thanks for downloading MailChained. Enjoy !
"""
import tkinter as tk

from interface.main_interface import MainApp

try:
    fen = tk.Tk()
    fen.title("MailChained")

    app = MainApp(fen)
    app.launch()
except:
    pass
