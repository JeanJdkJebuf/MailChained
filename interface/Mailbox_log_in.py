import sys

import tkinter as tk

# all strings are located in that file
sys.path.append("conf/")
import Mailbox_log_in_conf as text

# Partial import of other interfaces, preventing circles
import interface.main_interface as mi

class MailLogIn(tk.Frame):
    """To activate this tkinter window, instanciate it, then use the launch() function on
    your object"""

    def __init__(self, parent, provider):
        # Building main window
        tk.Frame.__init__(self)

        # Creating self.parent fo follow up interfaces
        self.parent = parent
        self.provider = provider

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
        self.label_1.config(text=text.LABEL_1_TEXT)
        self.label_1.grid(columnspan='2', padx='5', pady='5')

        self.label_2 = tk.Label(self.frame_1)
        self.label_2.config(text=text.LABEL_2_TEXT)
        self.label_2.grid(column='0', padx='5', pady='5', row='1', sticky='e')

        self.entry_1 = tk.Entry(self.frame_1)
        self.entry_1.grid(column='1', padx='5', pady='5', row='1', sticky='w')

        self.label_3 = tk.Label(self.frame_1)
        self.label_3.config(text=text.LABEL_3_TEXT)
        self.label_3.grid(column='0', padx='5', pady='5', row='2', sticky='e')

        self.entry_2 = tk.Entry(self.frame_1)
        self.entry_2.grid(column='1', padx='5', pady='5', row='2', sticky='w')

        self.label_4 = tk.Label(self.frame_1)
        self.label_4.grid(column='0', padx='10', pady='10', row='3', sticky='e')

        self.button_1 = tk.Button(self.frame_1)
        self.button_1.config(text=text.BUTTON_1_TEXT,
                             command=self.button_1_command
                            )
        self.button_1.grid(column='1', padx='10', pady='10', row='3', sticky='w')

    def launch(self):
        '''used as followed : app = MailLogIn()
        app=launch()'''
        self.mainloop()

    # Functions for buttons
    def button_1_command(self):
        '''this function makes button_1 switches interface to MainApp'''
        self.frame_1.destroy()

        app = mi.MainApp(self.parent)
        app.launch()

if __name__ == '__main__':
    app = MailLogIn()
    app.launch()
