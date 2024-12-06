import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="turquoise")
platno.pack()

lopticky = []

def Start():
    Vytvor_lopticky()

def Vytvor_lopticky():
    x = 10
    y = 10
    for i in range(10):
        x += 20
        lopticka = platno.create_oval(x, y, x+20, y+20, fill="red")
        lopticky.append(lopticka)
Start()        


