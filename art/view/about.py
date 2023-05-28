from tkinter import *
from pathlib import Path


class About:
    def __init__(self, window=None):
        self.top = Tk()
        self.top.geometry('1000x500')
        self.top.title("About TInspector")
        self.path = Path(__file__).parent / './../resources/about.png'
        self.bg_image = PhotoImage(file=self.path)
        self.label_image = Label(self.top, image=self.bg_image)
        self.label_image.pack()
        self.label_image.img_ref = self.bg_image
