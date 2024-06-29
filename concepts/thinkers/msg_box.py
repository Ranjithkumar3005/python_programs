from tkinter import *
from tkinter import messagebox
def submit():
    #messagebox.showinfo(title="This is the msg box",message="You are a person")
    #messagebox.showwarning(title="Thisis a warning msg",message="You are not a person")
    
    if messagebox.askokcancel(title="This is a ok or not",message="You are look handsome buddy "):
        print("You clicked ok")
    else:
        print("You clicked no")
    
    #See more in video or website

window=Tk()

button=Button(window,
              text="Submit",
              command=submit,
              )
button.pack()

window.mainloop()