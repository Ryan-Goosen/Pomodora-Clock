import tkinter as tk
import ttkbootstrap as tkb

from ttkbootstrap.constants import *
from PIL import Image, ImageTk

class PomodoraClock:
    def __init__(self, root):
        canvas = tkb.Canvas(width=350, height=400, highlightthickness=0)
        self.home_page(canvas)



    def home_page(self, canvas, image_id=""):
        main_page = tkb.PhotoImage(file="images\START.png")
        image_id = canvas.create_image(175,200, image= main_page)
        canvas.create_text(175, 25, text="CLICK : START", fill="white", font=("Times New Roman", 20, "bold"))
        canvas.pack()
        
        start_bt = tkb.Button(text="START", width=15, command= lambda: start_page(canvas, image_id))
        start_bt.place(x=10, y=355)  

        custom_bt = tkb.Button(text="CUSTOM", width=15, command=lambda: custom_page(canvas, image_id))
        custom_bt.place(x=230, y=355)


        canvas.image = main_page

    def custom_page(canvas, image_id):
        new_image = new_image = tkb.PhotoImage(file="images\CUSTOM.png")
        canvas.itemconfig(image_id, image=new_image)
        canvas.image = new_image

    def start_page(canvas, image_id):
        new_image = new_image = tkb.PhotoImage(file="images\STUDYING.png")
        canvas.itemconfig(image_id, image=new_image)
        canvas.image = new_image