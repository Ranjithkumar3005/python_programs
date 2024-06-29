from tkinter import *
from tkinter import colorchooser


def chooser():
    choose=colorchooser.askcolor()
    colurHEX=choose[1]
    window.config(bg=colurHEX)

window=Tk()
window.geometry("500x500")

button=Button(window,
              text="Button",
              command=chooser)
button.pack()

window.mainloop()



#See text area in video