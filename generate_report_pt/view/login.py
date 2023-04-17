from tkinter import *


class Login:
    def __init__(self, window=None):
        window.title('Cycle review tool')
        window.geometry('500x500')
        window.resizable(False, False)

        self.bg_image = PhotoImage(file='../resources/login.png')

        self.bg = Label(window, image=self.bg_image)
        self.bg.image = self.bg_image
        self.bg.pack()

        self.core_id = Entry(window)
        self.core_id['font'] = ('Calibri', 15)
        self.core_id['bg'] = '#D9D9D9'
        self.core_id['justify'] = 'center'
        self.core_id.place(width=330, height=43, x=85, y=201)

        self.password = Entry(window)
        self.password['font'] = ('Calibri', 15)
        self.password['bg'] = '#D9D9D9'
        self.password['justify'] = 'center'
        self.password['show'] = '*'
        self.password.place(width=330, height=43, x=85, y=289)

        self.log_in = Button(window)
        self.log_in['font'] = ('Calibri', 12)
        self.log_in['bg'] = '#687857'
        self.log_in['text'] = 'LOG IN'
        self.log_in.place(width=100, height=40, x=200, y=356)

        self.message = Label(window)
        self.message['text'] = ''
        self.message['font'] = ('Calibri', 10)
        self.message['bg'] = '#687857'
        self.message.place(width=330, height=30, x=85, y=455)

    def get_core_id(self):
        return self.core_id.get()

    def get_password(self):
        return self.password.get()

    def change_message(self, text, color):
        self.message['text'] = text
        self.message['fg'] = color
