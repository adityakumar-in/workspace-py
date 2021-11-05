from tkinter import *

at = Tk()
width = 600
height = 400
at.geometry(f"{width}x{height}")
at.title("Window Resizer")

def resizer():
    height = cheight.get()
    width = cwidth.get()
    at.geometry(f"{width}x{height}")

cwidth = IntVar()
cheight = IntVar()

Label(at, text="Width: ").grid(row=0, column=0)
Entry(at, textvariable=cwidth).grid(row=0, column=1)
Label(at, text="Width: ").grid(row=1, column=0)
Entry(at, textvariable=cheight).grid(row=1, column=1)
Button(at, text="Submit", command=resizer).grid(row=2, column=1)

at.mainloop()
