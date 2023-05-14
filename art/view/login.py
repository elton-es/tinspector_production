from tkinter import *
from pathlib import Path


class Login:
    def __init__(self, window=None):
        window.title('TInspector')
        window.geometry('1000x500')
        window.resizable(False, False)

        path = Path(__file__).parent / './../resources/login.png'
        self.bg_image = PhotoImage(file=path)

        self.bg = Label(window, image=self.bg_image)
        self.bg.image = self.bg_image
        self.bg.pack()

        self.urls = ['https://arttool.atlassian.net/']
        self.url = StringVar()
        self.url.set(self.urls[0])

        self.project_url = OptionMenu(window, self.url, *self.urls)
        self.project_url['font'] = ('Calibri', 12)
        self.project_url['bg'] = '#D9D9D9'
        self.project_url['justify'] = 'center'
        self.project_url.place(width=330, height=44, x=590, y=136)

        self.core_id = Entry(window)
        self.core_id['font'] = ('Calibri', 12)
        self.core_id['bg'] = '#D9D9D9'
        self.core_id['justify'] = 'center'
        self.core_id.place(width=330, height=44, x=590, y=227)

        self.password = Entry(window)
        self.password['font'] = ('Calibri', 12)
        self.password['bg'] = '#D9D9D9'
        self.password['justify'] = 'center'
        self.password['show'] = '*'
        self.password.place(width=330, height=44, x=590, y=315)

        self.log_in = Button(window)
        self.log_in['font'] = ('Calibri', 12)
        self.log_in['bg'] = '#783176'
        self.log_in['text'] = 'LOG IN'
        self.log_in.place(width=100, height=42, x=704, y=381)

        self.message = Label(window)
        self.message['text'] = ''
        self.message['font'] = ('Calibri', 8)
        self.message['bg'] = '#F6F7F7'
        self.message.place(width=330, height=25, x=590, y=440)

    def get_project_url(self):
        return self.url.get()

    def get_core_id(self):
        return self.core_id.get()

    def get_password(self):
        return self.password.get()

    def change_message(self, text, color):
        self.message['text'] = text
        self.message['fg'] = color
