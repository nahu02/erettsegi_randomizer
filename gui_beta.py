import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
import json
from erettsegi_random import random_website, random_website_with_history_check, add_website_to_history, open_websites


class Tantargy:
    counter = 0             # Egy számláló, amelyel id adható az objektumoknak
    osszes_tantargy = []    # Egy lista, amiben az osztály összes objektuma megjelenik

    def __init__(self, canvas, nev, online_nev, angol=False):
        Tantargy.osszes_tantargy.append(self)
        self.id = Tantargy.counter
        Tantargy.counter += 1
        # A vászon amin lesznek a dobozok
        self.canvas = canvas
        # Ami a checkbox mellé van írva
        self.nev = nev
        # Ahogy a tantárgy a linkekben megjelenik (pl. magyir, mat)
        self.online_nev = online_nev
        # Bool. Van -e angol változata a tantárgynak? (pl. matek,fizika)
        self.angol = angol
        # Az első oszlop változója (ki van választva?)
        self.v1 = tk.BooleanVar()
        # A második oszlop változója (emelt?)
        self.v2 = tk.BooleanVar()
        # A harmadik oszlop változója (angol?)
        self.v3 = tk.BooleanVar()

        # ------------------ 1. oszlop checkboxai (tantárgyak) ------------------ #
        self.c1 = ttk.Checkbutton(self.canvas, text=self.nev, variable=self.v1,
                                  onvalue=True, offvalue=False, command=self.emelt_kikapcs)
        self.c1.grid(row=self.id, column=0, sticky="w")
        self.v1.set(True)
        # -------------------- 2. oszlop checkboxai (emelt?) -------------------- #
        self.c2 = ttk.Checkbutton(
            self.canvas, text="emelt", variable=self.v2, onvalue=True, offvalue=False)
        self.c2.grid(row=self.id, column=1, sticky="w")
        self.v2.set(False)
        # -------------------- 3. oszlop checkboxai (angol?) -------------------- #
        if self.angol:
            self.c3 = ttk.Checkbutton(
                self.canvas, text="angolul", variable=self.v3, onvalue=True, offvalue=False)
            self.c3.grid(row=self.id, column=2, sticky="w")
            self.v3.set(False)

    # A parancs felel a többi checkbox kikapcsolásáért abban az esetben, ha a tantárgy doboza nincs bepipálva.
    def emelt_kikapcs(self):
        if not self.v1.get():
            self.c2.config(state="disabled")
            if self.angol:
                self.c3.config(state="disabled")
        else:
            self.c2.config(state="normal")
            if self.angol:
                self.c3.config(state="normal")

    def check(self):
        print(f"Up and running! {self.nev, self.online_nev, self.angol}")


def main():

    # --- A munkafelület megteremtése (az ablak és benne a frame-k és a style) --- #
    themeVar = "adapta"

    window = ThemedTk(theme=themeVar)
    window.title("Érettségi GUI - beta")
    window.iconbitmap("GUI\\book.ico")
    window.geometry("650x480")

    frame0 = ttk.Frame(window)
    frame0.pack(expand=True, fill=tk.BOTH)
    frame1 = ttk.Frame(frame0)
    frame1.pack(expand=True, anchor="center", side="top")
    frame2 = ttk.Frame(frame0)
    frame2.pack(expand=True, anchor="center", side="top")
    frame3 = ttk.Frame(frame0)
    frame3.pack(expand=True, anchor="center", side="top")

    style = ttk.Style()
    style.configure(".", font=('Helvetica', 18), justify=tk.LEFT)
    style.configure("TButton", font=("Helvetica", "11"))
    style.configure("help.TLabel", font=("Helvetica", "14"), justify=tk.CENTER)

# ----------------------------- Beállítások menü ----------------------------- #
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    # Megjegyezze -e a program a generált linkeket (többször nem generálódnak)
    history = tk.BooleanVar()
    selected_theme = tk.StringVar()  # A kiválasztott téma
    selected_theme.set("adapta")

    def change_theme():
        window.set_theme(selected_theme.get())
        style.configure(".", font=('Helvetica', 18), justify=tk.LEFT)
        style.configure("TButton", font=("Helvetica", "11"))
        style.configure("help.TLabel", font=(
            "Helvetica", "14"), justify=tk.CENTER)

    menubar = tk.Menu(window)

    settings = tk.Menu(menubar, tearoff=0)
    settings.add_checkbutton(label="Megnyitott linkek megjegyzése (többször nem generálódnak)",
                             variable=history, onvalue=True, offvalue=False)
    menubar.add_cascade(label="Beállítások", menu=settings)

    view = tk.Menu(menubar, tearoff=0)
    theme_selector = tk.Menu(view, tearoff=0)
    for i in window.get_themes():
        theme_selector.add_checkbutton(
            label=i, variable=selected_theme, onvalue=i, command=change_theme)
    view.add_cascade(label='Téma', menu=theme_selector)
    menubar.add_cascade(label="Nézet", menu=view)

    window.config(menu=menubar)

# ------------------------------ Help feliratok ------------------------------ #

    ttk.Label(frame1, style="help.TLabel", text="Ez egy random érettségi feladatsor generátor.\nVálaszd ki melyik tárgyak közül kapj egy feladatsort (véletlenszerűen),\nmajd az 'Érettségi feladat link' gombra kattintva kaphatsz egy linket!\n\nLejjebb, a dobozba egy érettségi feladatsor linkjét beillesztve\nmegkaphatod a hozzá tartozó javítókulcs elérhetőségét.").grid(
        row=0, column=0, columnspan=3)
    Tantargy.counter += 1
# ------------------------- A tantárgyak létrehozása ------------------------- #
    Tantargy(frame1, "Magyar", "magyir")
    Tantargy(frame1, "Matek", "mat", True)
    Tantargy(frame1, "Töri", "tort", True)
    Tantargy(frame1, "Angol", "angol")
    Tantargy(frame1, "Fizika", "fiz", True)
    Tantargy(frame1, "Infó", "inf", True)

# ----------------------------- A gomb és a link ----------------------------- #
    def open_erettsegi_link(event):
        if history.get():
            add_website_to_history(linkek)
        open_websites(linkek)
        e1_var.set(linkek[0])
        b2_click()

    def b1_click():
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
        linkek = random_website_with_history_check(options=final_options)
        l2.config(text=linkek[0])
        l2.pack()

    b1 = ttk.Button(frame2, text="Érettségi feladat link", command=b1_click)
    b1.pack()

    l2 = ttk.Label(frame2, cursor="hand2", font=(
        "Helvetica", "9"), foreground="blue")
    l2.bind("<Button-1>", open_erettsegi_link)

# ---------------------------- Ellenőrzés felület ---------------------------- #
    e1_var = tk.StringVar()

    def b2_click():
        if e1_var.get():
            global megoldokulcs_link
            megoldokulcs_link = f"{e1_var.get()[:-6]}ut.pdf"
            l3.config(text=megoldokulcs_link)
            l3.grid(row=1, column=0, columnspan=2)

    def open_erettsegi_megoldokulcs_link(event):
        webbrowser.open(megoldokulcs_link, new=2)

    e1 = ttk.Entry(frame3, textvariable=e1_var,
                   width="80", font=("Helvetica", 8))
    e1.grid(row=0, column=0)

    b2 = ttk.Button(frame3, text="Megoldókulcs", command=b2_click)
    b2.grid(row=0, column=1)

    l3 = ttk.Label(frame3, cursor="hand2", font=(
        "Helvetica", "9"), foreground="blue")
    l3.bind("<Button-1>", open_erettsegi_megoldokulcs_link)

    window.mainloop()


if __name__ == "__main__":
    main()
