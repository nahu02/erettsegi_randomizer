import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
import json
from erettsegi_random import random_website, random_website_with_history_check, add_website_to_history, open_websites

class Tantargy:
    counter = 0             # Egy számláló, amelyel id adható az objektumoknak
    osszes_tantargy = []    # Egy lista, amiben az osztály összes objektuma megjelenik

    def __init__ (self, canvas, nev, online_nev, angol):
        Tantargy.osszes_tantargy.append(self)
        self.id = Tantargy.counter
        Tantargy.counter += 1
        self.canvas = canvas            # A vászon amin lesznek a dobozok
        self.nev = nev                  # Ami a checkbox mellé van írva
        self.online_nev = online_nev    # Ahogy a tantárgy a linkekben megjelenik (pl. magyir, mat)
        self.angol = angol              # Bool. Van -e angol változata a tantárgynak? (pl. matek,fizika) 
        self.v1 = tk.BooleanVar()       # Az első oszlop változója (ki van választva?)
        self.v2 = tk.BooleanVar()       # A második oszlop változója (emelt?)
        self.v3 = tk.BooleanVar()       # A harmadik oszlop változója (angol?)

        # ------------------ 1. oszlop checkboxai (tantárgyak) ------------------ #
        self.c1 = ttk.Checkbutton(self.canvas, text = self.nev, variable = self.v1, onvalue = True, offvalue = False, command = self.emelt_kikapcs)
        self.c1.grid(row = self.id, column = 0, sticky = "w")
        self.v1.set(True)
        # -------------------- 2. oszlop checkboxai (emelt?) -------------------- #
        self.c2 = ttk.Checkbutton(self.canvas, text = "emelt", variable = self.v2, onvalue = True, offvalue = False)
        self.c2.grid(row = self.id, column = 1, sticky = "w")
        self.v2.set(False)
        # -------------------- 3. oszlop checkboxai (angol?) -------------------- #
        if self.angol:
            self.c3 = ttk.Checkbutton(self.canvas, text = "angolul", variable = self.v3, onvalue = True, offvalue = False)
            self.c3.grid(row = self.id, column = 2, sticky = "w")
            self.v3.set(False)

    def emelt_kikapcs(self): # A parancs felel a többi checkbox kikapcsolásáért abban az esetben, ha a tantárgy doboza nincs bepipálva.
        if not self.v1.get():
            self.c2.config(state = "disabled")
            if self.angol:
                self.c3.config(state = "disabled")
        else:
            self.c2.config(state = "normal")
            if self.angol:
                self.c3.config(state = "normal")

    def check(self):
        print(f"Up and running! {self.nev, self.online_nev, self.angol}")


def main():

# --- A munkafelület megteremtése (az ablak és benne a frame-k és a style) --- #
    themeVar = "adapta"

    window = ThemedTk(theme = themeVar)
    window.title("Érettségi GUI - beta") 
    window.iconbitmap("GUI\\book.ico")

    frame0 = ttk.Frame(window)
    frame0.pack(expand = True, fill = tk.BOTH)
    frame = ttk.Frame(frame0)
    frame.pack(expand = True, anchor = "center", side="top")
    frame2 = ttk.Frame(frame0)
    frame2.pack(expand = True, anchor = "center", side="top")

    style = ttk.Style()
    style.configure(".", font = ('Helvetica', 18), justify = tk.LEFT)

# ----------------------------- Beállítások menü ----------------------------- #
    menubar = tk.Menu(window)
    window.config(menu = menubar)

    history = tk.BooleanVar()       # Megjegyezze -e a program a generált linkeket (többször nem generálódnak)
    selected_theme = tk.StringVar() # A kiválasztott téma
    selected_theme.set("adapta")

    def change_theme():
        window.set_theme(selected_theme.get())
        style.configure(".", font = ('Helvetica', 18), justify = tk.LEFT)

    menubar = tk.Menu(window)  

    settings = tk.Menu(menubar, tearoff=0)
    settings.add_checkbutton(label = "Megnyitott linkek megjegyzése (többször nem generálódnak)", variable = history, onvalue = True, offvalue = False)
    menubar.add_cascade(label = "Beállítások", menu = settings)
    
    view = tk.Menu(menubar, tearoff=0)
    theme_selector = tk.Menu(view, tearoff=0)
    for i in window.get_themes():
        theme_selector.add_checkbutton(label = i, variable = selected_theme, onvalue = i, command = change_theme)
    view.add_cascade(label='Téma', menu = theme_selector)
    menubar.add_cascade(label = "Nézet", menu = view)

    window.config(menu = menubar)  
# ------------------------- A tantárgyak létrehozása ------------------------- #
    Tantargy(frame, "Magyar", "magyir", False)
    Tantargy(frame, "Matek", "mat", True)
    Tantargy(frame, "Töri", "tort", False)
    Tantargy(frame, "Angol", "angol", False)
    Tantargy(frame, "Fizika", "fiz", True)
    Tantargy(frame, "Infó", "inf", True)

# ----------------------------- A gomb és a link ----------------------------- #
    def open_link(event):
        if history.get():
            add_website_to_history(linkek)
        open_websites(linkek)

    def click():
        final_options = []

        for targy in Tantargy.osszes_tantargy:
            if targy.v1.get():
                if targy.v2.get():
                    _final = "emelt/e_"
                else:
                    _final = "kozep/k_"
                _final += targy.online_nev
                if targy.v3.get():
                    _final += "ang"
                final_options.append(_final)

        global linkek
        linkek = random_website_with_history_check(options = final_options)
        link_label.config(text = linkek[0])
        link_label.pack()


    b1 = ttk.Button(frame2, text = "Érettségi feladat link", command = click)
    b1.pack()

    link_label = ttk.Label(frame2, cursor = "hand2", font = ("Helvetica", "8"), foreground = "blue")
    link_label.bind("<Button-1>", open_link)

    window.mainloop()

if __name__ == "__main__":
    main()