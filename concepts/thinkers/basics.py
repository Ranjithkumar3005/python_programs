from tkinter import *

def checked():
    if x.get()==1:
        print("Ypu checked")
    else:
        print("Uchecked")


def click():
    print("Clicked")
window=Tk()

def submit():
    t=entry.get()
    print(t)
    
def delete():
    entry.delete(0,END)
def backscape():
    entry.delete(len(entry.get())-1,END)

window.geometry("700x1000")
window.title("Basics")
icon=PhotoImage(file='D://python_programs//concepts//thinkers//logo.png')
window.iconphoto(True,icon)
#window.config(background="black")

label=Label(window,text="Hello",
            font=('Arial',40,'bold'),
            fg="green",
            bg="black",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=icon,
            compound='top')
#label.pack()
label.config(width=200,height=400)
label.place(x=0,y=0)




x=IntVar()

entry=Entry(window,font=('Ariel',30),show='*')
entry.pack(side=RIGHT)

check=Checkbutton(window,
                  text="Select it",
                  variable=x,
                  onvalue=1,
                  offvalue=0,
                  command=checked,
                  compound="top")
check.pack()


button1=Button(window,
              text="Submit!",
              command=submit)

button1.pack()

button2=Button(window,
              text="Delete",
              command=delete)

button2.pack()
button3=Button(window,
              text="Backscape!",
              command=backscape)

button3.pack()
def order():
    if y.get()==0 :
        print("RAnjith")
    elif y.get()==1:
        print("Kumar")
    else:
        print("ar")

y=IntVar()
Radio=["Ran","Kum","ar"]
for i in range(len(Radio)):
    radiobutton=Radiobutton(window,
                            text=Radio[i],
                            value=i,
                            variable=y,
                            command=order
                            )
    radiobutton.pack(anchor=E)
button=Button(window,
              text="Click me!",
              command=click)

button.pack()


window.mainloop()