import tkinter as tk
from tkinter import Entry

import ttkbootstrap as tkb

from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from pathlib import Path
from time import time, sleep

from classes.data import Data

LABEL_TEXT_COLOUR = "white"
LABEL_FONT = ("Times New Roman", 15, "bold italic")
class PomodoraClock:

    def __init__(self, root):
        self.root = root
        self.data =  Data().get_data()
        self.start_time = 0

        self.canvas = tkb.Canvas(width=350, height=400, highlightthickness=0)
        self.image_id = self.canvas.create_image(175,200, image="")
        self.text_id = self.canvas.create_text(175, 25, text="CLICK : START", fill="white", font=("Times New Roman", 20, "bold"))
        self.canvas.pack()

        # CONFIGURATION ITEMS #
        # LABELS
        self.ST = self.canvas.create_text(70, 70, text="Study Time:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.RT = self.canvas.create_text(62, 95, text="Rest Time:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.STE = self.canvas.create_text(88, 120, text="Study Extension:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.RTE = self.canvas.create_text(82, 145, text="Rest Extension:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.NOS = self.canvas.create_text(102, 170, text="Number of Sessions:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        # ENTRIES #
        self.st_entry = tk.Entry(root)
        self.st_entry_window = self.canvas.create_window(270, 70, window=self.st_entry)
        self.rt_entry = tk.Entry(root)        
        self.rt_entry_window = self.canvas.create_window(270, 95, window=self.rt_entry)
        self.ste_entry = tk.Entry(root)
        self.ste_entry_window = self.canvas.create_window(270, 120, window=self.ste_entry)
        self.rte_entry = tk.Entry(root)
        self.rte_entry_window = self.canvas.create_window(270, 145, window=self.rte_entry)
        self.nos_entry = tk.Entry(root)
        self.nos_entry_window = self.canvas.create_window(270, 170, window=self.nos_entry)
        # BUTTONS #
        self.left_btn = tkb.Button(bootstyle="success-outline")
        self.center_btn = tkb.Button(bootstyle="danger-outline")
        self.right_btn = tkb.Button(bootstyle="info-outline")

        # LOADING HOMEPAGE #
        self.home_page()


##############  PAGES ##############
    def home_page(self):
        self.start_time = int(self.data.get("study_time")) * 60
        self._hide_entries()
        self.canvas.itemconfig(self.text_id, text="CLICK : START")

        home_page_image = tkb.PhotoImage(file="images/HOME.png")
        self.canvas.itemconfig(self.image_id, image=home_page_image)
        self.canvas.image = home_page_image

        self.left_btn.config(text="START", width=15, command=self.start_page)
        self.right_btn.config(text="CONFIG", width=15, command=self.config_page)


        self.left_btn.place(x=20, y=355)  
        self.center_btn.place_forget()
        self.right_btn.place(x=215, y=355)
      

    def config_page(self):
        config_page_image = tkb.PhotoImage(file=Path('images/CONFIG.png'))
        self._show_entries()

        self.canvas.itemconfig(self.image_id, image=config_page_image)
        self.canvas.image = config_page_image

        self.canvas.itemconfig(self.text_id, text="Clock Custimization")

        self.left_btn.config(text="SAVE", width=10)
        self.center_btn.config(text="RESET", width=10)
        self.right_btn.config(text="BACK", width=10, command=self.home_page)

        self.left_btn.place(x=15, y=355)
        self.center_btn.place(x=135, y=355)
        self.right_btn.place(x=255, y=355)

    def start_page(self):
        start_page_image = tkb.PhotoImage(file=Path('images/STUDYING.png'))
        self._hide_entries()
        self.canvas.itemconfig(self.image_id, image=start_page_image)
        self.canvas.image = start_page_image

        self.canvas.itemconfig(self.text_id, text="FOCUSED:", fill="Silver")
        self.canvas.create_text(180, 80, text="Time Left: " , fill="white", font=("Times New Roman", 20, "bold"))
        self.time_text = self.canvas.create_text(180, 150 , fill="white", font=("Times New Roman", 30, "bold"))
    
        self.start_timer()

    def start_timer(self):
        self._update_time()

    def _update_time(self):
        if self.start_time > 0:
            self.start_time -= 1
            minutes, seconds = divmod(self.start_time,60)
            self.canvas.itemconfig(self.time_text, text= str(minutes) + " min   " + str(seconds) + " sec")
            self.root.after(100, self._update_time)
        else:
            exit(1)
            # LOGIC TO GO TO NEW PAGE
            
        # current_time = self.start_time


##############  ENTRY THINGS ##############
    def _hide_entries(self):
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.RT, state="hidden")
        self.canvas.itemconfigure(self.STE, state="hidden")
        self.canvas.itemconfigure(self.RTE, state="hidden")
        self.canvas.itemconfigure(self.NOS, state="hidden")
        self.canvas.itemconfigure(self.st_entry_window, state="hidden")
        self.canvas.itemconfigure(self.rt_entry_window, state="hidden")
        self.canvas.itemconfigure(self.ste_entry_window, state="hidden")
        self.canvas.itemconfigure(self.rte_entry_window, state="hidden")
        self.canvas.itemconfigure(self.nos_entry_window, state="hidden")

    def _show_entries(self):
        self._populate_entries()
        self.canvas.itemconfigure(self.ST, state="normal")
        self.canvas.itemconfigure(self.RT, state="normal")
        self.canvas.itemconfigure(self.STE, state="normal")
        self.canvas.itemconfigure(self.RTE, state="normal")
        self.canvas.itemconfigure(self.NOS, state="normal")
        self.canvas.itemconfigure(self.st_entry_window, state="normal")
        self.canvas.itemconfigure(self.rt_entry_window, state="normal")
        self.canvas.itemconfigure(self.ste_entry_window, state="normal")
        self.canvas.itemconfigure(self.rte_entry_window, state="normal")
        self.canvas.itemconfigure(self.nos_entry_window, state="normal")

    def _populate_entries(self):
        self.st_entry.delete(0, 'end')
        self.st_entry.insert(0, self.data.get("study_time", 5))        
        self.rt_entry.delete(0, 'end')
        self.rt_entry.insert(0, self.data.get("rest_time", 2))        
        self.ste_entry.delete(0, 'end')
        self.ste_entry.insert(0, self.data.get("study_extension", 5))        
        self.rte_entry.delete(0, 'end')
        self.rte_entry.insert(0, self.data.get("rest_extension", 0))        
        self.nos_entry.delete(0, 'end')
        self.nos_entry.insert(0, self.data.get("num_sessions", 5))