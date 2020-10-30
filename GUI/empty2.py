from tkinter import *
import time

root=Tk()
root.geometry("600x600")

def blink():
    global label
    label.pack_forget()

    def show():
        global label
        label = Label(root, text="Hi THIS IS ME")
        label.pack()
        label.after(1000, blink)

    label.after(1000, show)





label=Label(root,text="Hi THIS IS ME")
label.pack()

but=Button(root,text="stop", command=blink)
but.place(x=10,y=20)


root.mainloop()