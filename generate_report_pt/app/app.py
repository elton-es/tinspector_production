from tkinter import *
from generate_report_pt.controller import main as main_controller


def main():
    root = Tk()
    main_controller.Controller(root)
    root.mainloop()


if __name__ == '__main__':
    main()
