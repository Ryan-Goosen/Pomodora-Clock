import tkinter as tk
import ttkbootstrap as tkb

from ttkbootstrap.constants import *
from PIL import Image, ImageTk


TITLE = " " *20 + "Pomodora-Clock"

def main():

    root = tkb.Window(title=TITLE, themename="darkly")
    root.geometry("1920x1280+800+250")
    root.minsize(width=350, height=400)
    root.maxsize(width=350, height=400)

    main_page = tkb.PhotoImage(file="images\START.png")
    canvas = tkb.Canvas(width=350, height=400, highlightthickness=0)
    image_id = canvas.create_image(175,200, image= main_page)
    canvas.create_text(175, 75, text="CLICK : START", fill="white", font=("Times New Roman", 20, "bold"))
    canvas.pack()

    start_bt = tkb.Button(text="START", width=15, command=lambda: test(canvas,image_id))
    start_bt.place(x=125, y=150)  

    # pause_bt = tkb.Button(text="PAUSE", width=15)
    # pause_bt.grid(row=1, column=1)

    root.mainloop()

def test(canvas, image_id):
    new_image = new_image = tkb.PhotoImage(file="images\PAUSED.png")
    canvas.itemconfig(image_id, image=new_image)
    canvas.image = new_image

if __name__ == "__main__":
    main()
