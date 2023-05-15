from tkinter import *


class Main:
    def __init__(self, window=None):
        self.window = window

        self.window.title('TInpector - Automatic Test Cycle Inspector')
        self.window.geometry('1280x720')
        self.window.resizable(True, True)

        self.menu = Menu(self.window)
        self.menu['background'] = '#10069F'
        self.menu['foreground'] = '#F6F7F7'
        self.menu['font'] = ('Helvetica', 10)
        self.menu.option_add('*tearOff', False)
        self.window.config(menu=self.menu)

        self.file_menu = Menu(self.menu)
        self.show_menu = Menu(self.menu)
        self.help_menu = Menu(self.menu)

        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.menu.add_cascade(label='Show', menu=self.show_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)

        self.file_menu.add_command(label='Exit', command=self.window.destroy)
        self.show_menu.add_command(label='Test Cycles')
        self.show_menu.add_command(label='Test Executions')
        self.show_menu.add_command(label='Issues')
        self.help_menu.add_command(label='About')
