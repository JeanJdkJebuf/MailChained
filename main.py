"""
Welcome to MailChained program

To launch program, simply type
'
python main.py
'

Thanks for downloading MailChained. Enjoy !
"""

from interface.main_interface import MainApp

try:
    app = MainApp()
    app.launch()
except:
    pass
