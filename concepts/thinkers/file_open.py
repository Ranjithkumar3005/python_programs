from tkinter import *
from tkinter import filedialog


def chooser():
    #
    # file=filedialog.askdirectory()
    file=filedialog.askopenfilename(title="Open file ok!",
                                    filetypes=(("text files","*.txt"),
                                               ("all files","*.*")))
    print(file)

window=Tk()
window.geometry("500x500")

button=Button(window,
              text="Button",
              command=chooser)
button.pack()

window.mainloop()



#See text area in video