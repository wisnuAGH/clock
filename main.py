from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.geometry('699x500')

img = PhotoImage(file="background_3.png")

def time():
    data = strftime('%H:%M:%S')
    label.config(text=data)
    label.after(1000, time)

label0 = Label(root, image=img)
label0.place(x=0, y=-100)

label = Label(root, background='black', font = ("ds-digital", 70), foreground= "green")
label.place(x=200, y=170)

time()
mainloop()