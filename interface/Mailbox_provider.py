import sys

import tkinter as tk

# all strings are located in that file
sys.path.append("conf/")
import mail_provider_conf as text

class MailboxProvider(tk.Frame):
    """To activate this tkinter window, instanciate it, then use the launch() function on
    your object"""

    def __init__(self, parent):
        # Building main window
        tk.Frame.__init__(self)

        # Add self.frame_1 as master
        self.add_frame_1()

        # Add widgets to self.frame_1
        self.add_widgets_to_frame_1()

    def add_frame_1(self):
        '''Add master widget called self.frame_1'''

        self.frame_1 = tk.Frame()
        self.frame_1.config(height='200', width='200')
        self.frame_1.grid()

    def add_widgets_to_frame_1(self):
        '''Add widgets to self.frame_1'''

        self.label_1 = tk.Label(self.frame_1)
        self.label_1.config(anchor='w', cursor='arrow', font='TkDefaultFont', text=text.LABEL_1_TEXT)
        self.label_1.grid(padx='10', pady='5')

        self.button_1 = tk.Button(self.frame_1)
        self.button_1.config(height='2', text=text.BUTTON_1_TEXT, width='20')
        self.button_1.grid(column='0', padx='10', pady='10', row='1')

        self.button_2 = tk.Button(self.frame_1)
        self.button_2.config(height='2', text=text.BUTTON_2_TEXT, width='20')
        self.button_2.grid(column='0', padx='10', pady='10', row='2')

        self.button_3 = tk.Button(self.frame_1)
        self.button_3.config(height='2', text=text.BUTTON_3_TEXT, width='20')
        self.button_3.grid(column='0', padx='10', pady='10', row='3')

        self.button_4 = tk.Button(self.frame_1)
        self.button_4.config(text=text.BUTTON_4_TEXT)
        self.button_4.grid(column='1', padx='5', pady='5', row='4')

    def launch(self):
        '''used as followed : app = MailboxProvider()
        app=launch()'''
        self.mainloop()

if __name__ == '__main__':
    app = MailboxProvider()
    app.launch()
