import tkinter as tk
import ttkbootstrap as tkb

from classes.gui import PomodoraClock

# from classes.gui_class import PomodoraClock
TITLE = " " + "Pomodora-Clock"

def main():

    root = tkb.Window(title=TITLE)
    root.maxsize(350, 400)
    root.minsize(350, 400)
    app = PomodoraClock(root)

    root.mainloop()

if __name__ == "__main__":
    main()
