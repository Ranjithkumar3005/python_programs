from tkinter import *

window=Tk()

firstnamelabel=Label(window,text="First name:").grid(row=0,column=0)
firstnamenetry=Entry(window).grid(row=0,column=1)

lastnamelabel=Label(window,text="Last name:").grid(row=1,column=0)
lastnamenetry=Entry(window).grid(row=1,column=1)

emailnamelabel=Label(window,text="Email:").grid(row=2,column=0)
emailnamenetry=Entry(window).grid(row=2,column=1)

button=Button(window,text="Submit").grid(row=3,column=0,columnspan=2)

window.mainloop()


#See other concepts in video