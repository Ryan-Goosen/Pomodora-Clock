import tkinter as tk
from tkinter import Entry

import ttkbootstrap as tkb

from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class PomodoraClock:

    def __init__(self, root):
        self.canvas = tkb.Canvas(width=350, height=400, highlightthickness=0)
        self.image_id = self.canvas.create_image(175,200, image="")
        self.text_id = self.canvas.create_text(175, 25, text="CLICK : START", fill="white", font=("Times New Roman", 20, "bold"))
        self.canvas.pack()

        # CONFIGURATION ITEMS
        self.ST = self.canvas.create_text(70, 70, text="Study Time:", fill="grey", font=("Times New Roman", 15, "bold italic"))
        self.RT = self.canvas.create_text(62, 95, text="Rest Time:", fill="grey", font=("Times New Roman", 15, "bold italic"))

        self.entry = tk.Entry(root)
        self.canvas.create_window(150, 100, window=self.entry)


        self.left_btn = tkb.Button(bootstyle="success-outline")
        self.center_btn = tkb.Button(bootstyle="danger-outline")
        self.right_btn = tkb.Button(bootstyle="info-outline")

        self.home_page()

    def home_page(self):
        self.canvas.itemconfig(self.text_id, text="CLICK : START")

        home_page_image = tkb.PhotoImage(file="images/HOME.png")
        self.canvas.itemconfig(self.image_id, image=home_page_image)
        self.canvas.image = home_page_image

        self.left_btn.config(text="START", width=15)
        self.right_btn.config(text="CONFIG", width=15, command=self.config_page)


        self.left_btn.place(x=10, y=355)  
        self.center_btn.place_forget()
        self.right_btn.place(x=195, y=355)


        self.entry.config(state="hidden")
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.RT, state="hidden")
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.ST, state="hidden")

    def config_page(self):
        config_page_image = tkb.PhotoImage(file="images/CONFIG.png")
        self.canvas.itemconfig(self.image_id, image=config_page_image)
        self.canvas.image = config_page_image

        self.canvas.itemconfig(self.text_id, text="Clock Custimization")

        self.left_btn.config(text="SAVE", width=10)
        self.center_btn.config(text="RESET", width=10)
        self.right_btn.config(text="BACK", width=10, command=self.home_page)

        self.left_btn.place(x=5, y=355)
        self.center_btn.place(x=120, y=355)
        self.right_btn.place(x=235, y=355)

        self.canvas.itemconfigure(self.ST, state="normal")
        self.canvas.itemconfigure(self.RT, state="normal")


        