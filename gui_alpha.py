import tkinter as tk
import webbrowser
from erettsegi_random import random_website

EVSZAK = ["osz", "tavasz"]
TARGY = ["kozep/k_magyir", "emelt/e_matang", "kozep/k_tort", "emelt/e_angol", "kozep/k_fiz", "emelt/e_inf"]
TARGY_alt = ["magyar", "matek", "töri", "angol", "fizika", "info"]

window = tk.Tk()
window.title("Érettségi GUI - alpha") 
window.iconbitmap("GUI\\book.ico")

targyak_neve = {"magyar" : "magyir", 
           "matek" : "matang", 
           "töri" : "tort", 
           "angol" : "angol", 
           "fizika" : "fiz",
           "infó" : "inf"}

# ---------------------------------------------------------------------------- #
#                                   Változók                                   #
# ---------------------------------------------------------------------------- #

# --------------------- 1. oszlop változói (tantárgyak) --------------------- #
v_magyar = tk.StringVar()
v_matek = tk.StringVar()
v_töri = tk.StringVar()
v_angol = tk.StringVar()
v_fizika = tk.StringVar()
v_infó = tk.StringVar()

# --------------------- 2. oszlop változói (emelt?) --------------------- #
v_magyar_e = tk.StringVar()
v_matek_e = tk.StringVar()
v_töri_e = tk.StringVar()
v_angol_e = tk.StringVar()
v_fizika_e = tk.StringVar()
v_infó_e = tk.StringVar()


# ---------------------------------------------------------------------------- #
#                                   Parancsok                                  #
# ---------------------------------------------------------------------------- #

# A parancsok felelnek az "emelt" checkbox kikapcsolásáért abban az esetben, ha a tantárgy doboza nincs bepipálva.

def c_magyar_check():
    if v_magyar.get() == "OFF":
        c_magyar_e.config(state = "disabled")
        c_magyar_e.deselect()
    else:
        c_magyar_e.config(state = "normal")

def  c_matek_check():
    if v_matek.get() == "OFF":
        c_matek_e.config(state = "disabled")
        c_matek_e.deselect()
    else:
        c_matek_e.config(state = "normal")

def c_töri_check():
    if v_töri.get() == "OFF":
        c_töri_e.config(state = "disabled")
        c_töri_e.deselect()
    else:
        c_töri_e.config(state = "normal")

def  c_angol_check():
    if v_angol.get() == "OFF":
        c_angol_e.config(state = "disabled")
        c_angol_e.deselect()
    else:
        c_angol_e.config(state = "normal")

def c_fizika_check():
    if v_fizika.get() == "OFF":
        c_fizika_e.config(state = "disabled")
        c_fizika_e.deselect()
    else:
        c_fizika_e.config(state = "normal")

def c_infó_check():
    if v_infó.get() == "OFF":
        c_infó_e.config(state = "disabled")
        c_infó_e.deselect()
    else:
        c_infó_e.config(state = "normal")


# ---------------------------------------------------------------------------- #
#                                  Checkboxok                                  #
# ---------------------------------------------------------------------------- #

# -------------------- 1. oszlop checkboxai (tantárgyak) -------------------- #
c_magyar = tk.Checkbutton(window, text = "magyar", variable = v_magyar, onvalue = "ON", offvalue = "OFF", command = c_magyar_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_magyar.grid(row = 0, column = 0, sticky = "w")
c_magyar.select()

c_matek = tk.Checkbutton(window, text = "matek (angol)", variable = v_matek, onvalue = "ON", offvalue = "OFF", command = c_matek_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_matek.grid(row = 1, column = 0, sticky = "w")
c_matek.select()

c_töri = tk.Checkbutton(window, text = "töri", variable = v_töri, onvalue = "ON", offvalue = "OFF", command = c_töri_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_töri.grid(row = 2, column = 0, sticky = "w")
c_töri.select()

c_angol = tk.Checkbutton(window, text = "angol", variable = v_angol, onvalue = "ON", offvalue = "OFF", command = c_angol_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_angol.grid(row = 3, column = 0, sticky = "w")
c_angol.select()

c_fizika = tk.Checkbutton(window, text = "fizika", variable = v_fizika, onvalue = "ON", offvalue = "OFF", command = c_fizika_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_fizika.grid(row = 4, column = 0, sticky = "w")
c_fizika.select()

c_infó = tk.Checkbutton(window, text = "infó", variable = v_infó, onvalue = "ON", offvalue = "OFF", command = c_infó_check, font = ('Arial', 20), anchor = "w", justify = "left")
c_infó.grid(row = 5, column = 0, sticky = "w")
c_infó.select()

# -------------------- 2. oszlop checkboxai (emelt?) -------------------- #
c_magyar_e = tk.Checkbutton(window, text = "emelt", variable = v_magyar_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_magyar_e.grid(row = 0, column = 1, sticky = "w")
c_magyar_e.deselect()

c_matek_e = tk.Checkbutton(window, text = "emelt", variable = v_matek_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_matek_e.grid(row = 1, column = 1, sticky = "w")
c_matek_e.deselect()

c_töri_e = tk.Checkbutton(window, text = "emelt", variable = v_töri_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_töri_e.grid(row = 2, column = 1, sticky = "w")
c_töri_e.deselect()

c_angol_e = tk.Checkbutton(window, text = "emelt", variable = v_angol_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_angol_e.grid(row = 3, column = 1, sticky = "w")
c_angol_e.deselect()

c_fizika_e = tk.Checkbutton(window, text = "emelt", variable = v_fizika_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_fizika_e.grid(row = 4, column = 1, sticky = "w")
c_fizika_e.deselect()

c_infó_e = tk.Checkbutton(window, text = "emelt", variable = v_infó_e, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "center")
c_infó_e.grid(row = 5, column = 1, sticky = "w")
c_infó_e.deselect()





def click():
    final_options = []

    if v_magyar.get() == "ON":
        if v_magyar_e.get() == "ON":
            final_options.append("emelt/e_magyir")
        elif v_magyar_e.get() == "OFF":
            final_options.append("kozep/k_magyir")    
    if v_matek.get() == "ON":
        if v_matek_e.get() == "ON":
            final_options.append("emelt/e_matang")
        elif v_matek_e.get() == "OFF":
            final_options.append("kozep/k_matang")
    if v_töri.get() == "ON":
        if v_töri_e.get() == "ON":
            final_options.append("emelt/e_tort")
        elif v_töri_e.get() == "OFF":
            final_options.append("kozep/k_tort")
    if v_angol.get() == "ON":
        if v_angol_e.get() == "ON":
            final_options.append("emelt/e_angol")
        elif v_angol_e.get() == "OFF":
            final_options.append("kozep/k_angol")
    if v_fizika.get() == "ON":
        if v_fizika_e.get() == "ON":
            final_options.append("emelt/e_fiz")
        elif v_fizika_e.get() == "OFF":
            final_options.append("kozep/k_fiz")
    if v_infó.get() == "ON":
        if v_infó_e.get() == "ON":
            final_options.append("emelt/e_inf")
        elif v_infó_e.get() == "OFF":
            final_options.append("kozep/k_inf")

    link = tk.Label(window, text = f"{random_website(options = final_options)[0]}", fg = "blue", cursor = "hand2")
    link.grid(row = 8, columnspan = 2)
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))

b1 = tk.Button(window, text = "Érettségi feladat link", command = click)
b1.grid(row = 6, columnspan = 2)

window.mainloop()