import tkinter as tk
import ttkbootstrap as tkb
from pathlib import Path

from tkinter import messagebox
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
        self.text_id = self.canvas.create_text(175, 160, text="CLICK : START", fill="white", font=("Times New Roman", 20, "bold"))
        self.canvas.pack()

        # CONFIGURATION ITEMS #
        self.create_spinbox()

        # LABELS
        self.ST = self.canvas.create_text(70, 110, text="Study Time:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.RT = self.canvas.create_text(62, 145, text="Rest Time:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.STE = self.canvas.create_text(88, 180, text="Study Extension:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.RTE = self.canvas.create_text(82, 215, text="Rest Extension:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        self.NOS = self.canvas.create_text(102, 250, text="Number of Sessions:", fill=LABEL_TEXT_COLOUR, font=LABEL_FONT)
        # ENTRIES #

        # BUTTONS #
        self.left_btn = tkb.Button(bootstyle="success-outline")
        self.center_btn = tkb.Button(bootstyle="danger-outline")
        self.right_btn = tkb.Button(bootstyle="info-outline")

        # LOADING HOMEPAGE #
        self.home_page()


##############  PAGES ##############
    def home_page(self):
        self.start_time = int(self.data.get("study_time")) * 60
        self._hide_spinbox()
        self.canvas.itemconfig(self.text_id, text="CLICK : START")
        self.canvas.coords(self.text_id, 175, 160)


        home_page_image = tkb.PhotoImage(file="images/actual/HOME.png")
        self.canvas.itemconfig(self.image_id, image=home_page_image)
        self.canvas.image = home_page_image

        self.left_btn.config(text="START", width=15, command=self.start_page)
        self.right_btn.config(text="CONFIG", width=15, command=self.config_page)


        self.left_btn.place(x=15, y=355)
        self.center_btn.place_forget()
        self.right_btn.place(x=195, y=355)
      

    def config_page(self):
        config_page_image = tkb.PhotoImage(file=Path('images/actual/CONFIG.png'))
        self._show_spinbox()

        self.canvas.itemconfig(self.image_id, image=config_page_image)
        self.canvas.image = config_page_image

        self.canvas.itemconfig(self.text_id, text="Clock Custimization", fill="White")
        self.canvas.coords(self.text_id, 175, 25)

        self.left_btn.config(text="SAVE", width=10, command=self._save_spinbox)
        self.center_btn.config(text="RESET", width=10, command=self._reset_spinbox)
        self.right_btn.config(text="BACK", width=10, command=self.home_page)

        self.left_btn.place(x=15, y=355)
        self.center_btn.place(x=125, y=355)
        self.right_btn.place(x=235, y=355)

    def start_page(self):
        start_page_image = tkb.PhotoImage(file=Path('images/actual/STUDYING.png'))
        self._hide_spinbox()
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
            self.root.after(1000, self._update_time)
        else:
            exit(1)
            # LOGIC TO GO TO NEW PAGE
            
        # current_time = self.start_time

# TIME TO STOP AND TIME TO STUDY ALERTS #

##############  Spinbox THINGS ##############
    def create_spinbox(self):
        self.st_spinbox = tk.Spinbox(self.root, from_=0, to=100, width=5)
        self.st_spinbox_window = self.canvas.create_window(270, 110, window=self.st_spinbox)
        self.rt_spinbox = tk.Spinbox(self.root, from_=0, to=100, width=5)
        self.rt_spinbox_window = self.canvas.create_window(270, 145, window=self.rt_spinbox)
        self.ste_spinbox = tk.Spinbox(self.root, from_=0, to=100, width=5)
        self.ste_spinbox_window = self.canvas.create_window(270, 180, window=self.ste_spinbox)
        self.rte_spinbox = tk.Spinbox(self.root, from_=0, to=100, width=5)
        self.rte_spinbox_window = self.canvas.create_window(270, 215, window=self.rte_spinbox)
        self.nos_spinbox = tk.Spinbox(self.root, from_=0, to=100, width=5)
        self.nos_spinbox_window = self.canvas.create_window(270, 250, window=self.nos_spinbox)

    def _hide_spinbox(self):
        self.canvas.itemconfigure(self.ST, state="hidden")
        self.canvas.itemconfigure(self.RT, state="hidden")
        self.canvas.itemconfigure(self.STE, state="hidden")
        self.canvas.itemconfigure(self.RTE, state="hidden")
        self.canvas.itemconfigure(self.NOS, state="hidden")
        self.canvas.itemconfigure(self.st_spinbox_window, state="hidden")
        self.canvas.itemconfigure(self.rt_spinbox_window, state="hidden")
        self.canvas.itemconfigure(self.ste_spinbox_window, state="hidden")
        self.canvas.itemconfigure(self.rte_spinbox_window, state="hidden")
        self.canvas.itemconfigure(self.nos_spinbox_window, state="hidden")

    def _show_spinbox(self):
        self._populate_spinbox()
        self.canvas.itemconfigure(self.ST, state="normal")
        self.canvas.itemconfigure(self.RT, state="normal")
        self.canvas.itemconfigure(self.STE, state="normal")
        self.canvas.itemconfigure(self.RTE, state="normal")
        self.canvas.itemconfigure(self.NOS, state="normal")
        self.canvas.itemconfigure(self.st_spinbox_window, state="normal")
        self.canvas.itemconfigure(self.rt_spinbox_window, state="normal")
        self.canvas.itemconfigure(self.ste_spinbox_window, state="normal")
        self.canvas.itemconfigure(self.rte_spinbox_window, state="normal")
        self.canvas.itemconfigure(self.nos_spinbox_window, state="normal")

    def _populate_spinbox(self):
        self.st_spinbox.delete(0, 'end')
        self.st_spinbox.insert(0, self.data.get("study_time", 5))        
        self.rt_spinbox.delete(0, 'end')
        self.rt_spinbox.insert(0, self.data.get("rest_time", 2))        
        self.ste_spinbox.delete(0, 'end')
        self.ste_spinbox.insert(0, self.data.get("study_extension", 5))        
        self.rte_spinbox.delete(0, 'end')
        self.rte_spinbox.insert(0, self.data.get("rest_extension", 0))        
        self.nos_spinbox.delete(0, 'end')
        self.nos_spinbox.insert(0, self.data.get("num_sessions", 5))

    def _reset_spinbox(self):
        self.st_spinbox.delete(0, 'end')
        self.st_spinbox.insert(0, "5")
        self.rt_spinbox.delete(0, 'end')
        self.rt_spinbox.insert(0, "2")
        self.ste_spinbox.delete(0, 'end')
        self.ste_spinbox.insert(0, "5")
        self.rte_spinbox.delete(0, 'end')
        self.rte_spinbox.insert(0, "0")
        self.nos_spinbox.delete(0, 'end')
        self.nos_spinbox.insert(0, "5")

    def _save_spinbox(self):
        try:
            study_time = int(self.st_spinbox.get())
            rest_time = int(self.rt_spinbox.get())
            study_extension = int(self.ste_spinbox.get())
            rest_extension = int(self.rte_spinbox.get())
            num_sessions = int(self.nos_spinbox.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please only use numerical values in all spinboxes.")
            return None  # or you could raise or handle it differently

        Data._write_file(
            input_study_time = study_time,
            input_rest_time = rest_time,
            input_study_extension = study_extension,
            input_rest_extension = rest_extension,
            input_num_sessions = num_sessions
        )