from tkinter import *


window=Tk()

frame=Frame(window)
#
# frame.pack()
frame.place(x=100,y=100)
Button(frame,text="W",width=3).pack(side=TOP)
Button(frame,text="T",width=3).pack(side=LEFT)
Button(frame,text="A",width=3).pack(side=LEFT)
Button(frame,text="C",width=3).pack(side=LEFT)
window.mainloop()


#Using window.destory() to remove the current window