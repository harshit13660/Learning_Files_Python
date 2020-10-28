from tkinter import *
from PIL import Image, ImageTk
import pygame
import keyboard as kb
import time

root=Tk()
root.geometry("400x500")
m = Image.open("start-jarvis.png")
a=1
def hello():
    global but
    global img
    global a
    a=a-5
    z=m.rotate(a)
    img=ImageTk.PhotoImage(z)
    but.config(image=img)
    but.after(50,hello)


img=ImageTk.PhotoImage(m)

# lab=Label(root,image=img)
# lab.pack()

but=Button(root,image=img, command=hello,borderwidth=0)
but.pack(pady=10)


root.mainloop()



