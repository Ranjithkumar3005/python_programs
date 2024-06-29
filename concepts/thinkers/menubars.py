from tkinter import *


window=Tk()

menubar=Menu(window)
window.config(menu=menubar)

filename=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filename)

filename.add_command(label="Open")

editname=Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=editname)

window.mainloop()