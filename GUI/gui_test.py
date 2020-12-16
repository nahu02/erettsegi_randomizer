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

# --------------------- Bal oszlop változói (tantárgyak) --------------------- #
v_magyar = tk.StringVar()
v_matek = tk.StringVar()
v_töri = tk.StringVar()
v_angol = tk.StringVar()
v_fizika = tk.StringVar()
v_infó = tk.StringVar()



# ---------------------------------------------------------------------------- #
#                                  Checkboxok                                  #
# ---------------------------------------------------------------------------- #

# -------------------- Bal oszlop checkboxai (tantárgyak) -------------------- #
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





def click():
    my_label = tk.Label(window, text = f'''
                                magyar variable is {v_magyar.get()}
                                matek variable is {v_matek.get()}
                                töri variable is {v_töri.get()}
                                angol variable is {v_angol.get()}
                                fizika variable is {v_fizika.get()}
                                infó variable is {v_infó.get()} 
                                ''')
    my_label.grid(row = 7)

b1 = tk.Button(window, text = "Show value", command = click)
b1.grid(row = 6)

window.mainloop()