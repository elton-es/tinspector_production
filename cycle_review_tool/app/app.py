from tkinter import *
from cycle_review_tool.controller import main as main_controller


def main():
    root = Tk()
    main_controller.Controller(root)
    root.mainloop()


if __name__ == '__main__':
    main()
