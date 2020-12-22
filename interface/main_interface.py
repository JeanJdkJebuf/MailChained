import sys

import tkinter as tk

# all strings are located in that file
sys.path.append("conf/")
import conf_main as text

# import other interfaces
import interface.Mailbox_provider as mp

class MainApp(tk.Frame):
    """To activate this tkinter window, instanciate it, then use the launch() function on
    your object"""

    def __init__(self, parent):
        # Building main window
        tk.Frame.__init__(self, parent)

        # Creating self.parent for follow up interfaces
        self.parent = parent

        # Add self.frame_1 as master
        self.add_frame_1()

        # Add widgets to self.frame_1
        self.add_widgets_to_frame_1()

        # Add widgets to self.labelframe_1
        self.add_widgets_to_labelframe_1()

        # Add widgets to self.labelframe_2
        self.add_widgets_to_labelframe_2()

    def add_frame_1(self):
        '''Add master widget called self.frame_1'''

        self.frame_1 = tk.Frame()
        self.frame_1.config(height='200', width='200')
        self.frame_1.grid()

    def add_widgets_to_frame_1(self):
        '''Add widgets to self.frame_1'''

        self.label_1 = tk.Label(self.frame_1)
        self.label_1.config(text=text.LABEL_1_TEXT)
        self.label_1.grid(columnspan='2', ipadx='5', ipady='5')

        self.button_1 = tk.Button(self.frame_1)
        self.button_1.config(text=text.BUTTON_1_TEXT, width='15',
                             command=self.button_1_command
                            )
        self.button_1.grid(column='0', padx='5', pady='5', row='1')

        self.button_2 = tk.Button(self.frame_1)
        self.button_2.config(height='2', text=text.BUTTON_2_TEXT, width='15')
        self.button_2.grid(column='1', padx='5', pady='5', row='1')

        self.labelframe_1 = tk.LabelFrame(self.frame_1)
        self.labelframe_1.config(height='200', text=text.LABELFRAME_1_TEXT, width='200')
        self.labelframe_1.grid(column='0', columnspan='3', padx='5', pady='5', row='2')

        self.labelframe_2 = tk.LabelFrame(self.frame_1)
        self.labelframe_2.config(height='170', text=text.LABELFRAME_2_TEXT, width='485')
        self.labelframe_2.grid(column='0', columnspan='3', padx='5', pady='5', row='3')
        self.labelframe_2.grid_propagate(0)

    def add_widgets_to_labelframe_1(self):
        '''Add widgets to self.labelframe_1'''

        self.label_2 = tk.Label(self.labelframe_1)
        self.label_2.config(text=text.LABEL_2_TEXT)
        self.label_2.grid(columnspan='3', padx='5', pady='5')

        self.button_3 = tk.Button(self.labelframe_1)
        self.button_3.config(text=text.BUTTON_3_TEXT)
        self.button_3.grid(column='0', padx='5', pady='5', row='1')

        self.button_4 = tk.Button(self.labelframe_1)
        self.button_4.config(text=text.BUTTON_4_TEXT)
        self.button_4.grid(column='1', padx='5', pady='5', row='1')

        self.button_5 = tk.Button(self.labelframe_1)
        self.button_5.config(text=text.BUTTON_5_TEXT)
        self.button_5.grid(column='2', padx='5', pady='5', row='1')

    def add_widgets_to_labelframe_2(self):
        '''Add widgets to self.labelframe_2'''

        self.label_3 = tk.Label(self.labelframe_2)
        self.label_3.config(text=text.LABEL_3_TEXT)
        self.label_3.grid(padx='50', pady='5')

        self.button_6 = tk.Button(self.labelframe_2)
        self.button_6.config(text=text.BUTTON_6_TEXT)
        self.button_6.grid(column='0', padx='5', pady='5', row='1')

        self.canvas_1 = tk.Canvas(self.labelframe_2)
        self.canvas_1.config(height='5', width='250')
        self.canvas_1.grid(column='0', padx='5', pady='5', row='2')
        self.canvas_1.grid_propagate(0)

        self.label_4 = tk.Label(self.labelframe_2)
        self.label_4.config(text=text.LABEL_4_TEXT)
        self.label_4.grid(column='0', padx='5', pady='5', row='3')

    # Functions for buttons
    def button_1_command(self):
        '''this function makes button_1 switches interface to MailboxProvider'''
        self.frame_1.destroy()

        app = mp.MailboxProvider(self.parent)
        app.launch()

    def launch(self):
        '''used as followed : app = MainApp()
        app=launch()'''
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.launch()
