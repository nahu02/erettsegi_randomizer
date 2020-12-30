import tkinter as tk

EVSZAK = ["osz", "tavasz"]
TARGY = ["kozep/k_magyir", "emelt/e_matang", "kozep/k_tort", "emelt/e_angol", "kozep/k_fiz", "emelt/e_inf"]
TARGY_alt = ["magyar", "matek", "töri", "angol", "fizika", "info"]

window = tk.Tk()
window.title("Gui - test") 
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
#                                  Checkboxok                                  #
# ---------------------------------------------------------------------------- #

# -------------------- 1. oszlop checkboxai (tantárgyak) -------------------- #
c_magyar = tk.Checkbutton(window, text = "magyar", variable = v_magyar, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
c_magyar.grid(row = 0, column = 0, sticky = "w")
c_magyar.select()

c_matek = tk.Checkbutton(window, text = "matek", variable = v_matek, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
c_matek.grid(row = 1, column = 0, sticky = "w")
c_matek.select()

c_töri = tk.Checkbutton(window, text = "töri", variable = v_töri, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
c_töri.grid(row = 2, column = 0, sticky = "w")
c_töri.select()

c_angol = tk.Checkbutton(window, text = "angol", variable = v_angol, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
c_angol.grid(row = 3, column = 0, sticky = "w")
c_angol.select()

c_fizika = tk.Checkbutton(window, text = "fizika", variable = v_fizika, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
c_fizika.grid(row = 4, column = 0, sticky = "w")
c_fizika.select()

c_infó = tk.Checkbutton(window, text = "infó", variable = v_infó, onvalue = "ON", offvalue = "OFF", font = ('Arial', 20), anchor = "w", justify = "left")
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
    show_value_label = tk.Label(window, text = f'''
                                magyar is {v_magyar.get()}
                                and emelt is {v_magyar_e.get()}
                                matek is {v_matek.get()}
                                and emelt is {v_matek_e.get()}
                                töri is {v_töri.get()}
                                and emelt is {v_töri_e.get()}
                                angol is {v_angol.get()}
                                and emelt is {v_angol_e.get()}
                                fizika is {v_fizika.get()}
                                and emelt is {v_fizika_e.get()}
                                infó is {v_infó.get()}
                                and emelt is {v_infó_e.get()}
                                ''')
    show_value_label.grid(row = 7, column = 1)

b1 = tk.Button(window, text = "Show value", command = click)
b1.grid(row = 6, column = 1)

window.mainloop()