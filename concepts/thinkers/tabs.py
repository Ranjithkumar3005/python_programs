from tkinter import *
from tkinter import ttk

window=Tk()

notebook=ttk.Notebook(window)
tab1=Frame(notebook)
tab2=Frame(notebook)
notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack()


Label(tab1,text="Heloo My name is ranjth",width=50,height=50).pack()
Label(tab2,text="ranjth",width=50,height=50).pack()
window.mainloop()