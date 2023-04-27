from tkinter import *
from art.controller import main as main_controller


def main():
    root = Tk()
    main_controller.Controller(root)
    root.mainloop()


if __name__ == '__main__':
    main()
