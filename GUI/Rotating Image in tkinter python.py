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
    global lab
    global z
    global img
    global a
    a=a-5
    z=m.rotate(a)
    img=ImageTk.PhotoImage(z)
    lab.config(image=img)
    lab.after(50,hello)


z=m.rotate(50)
img=ImageTk.PhotoImage(z)

lab=Label(root,image=img)
lab.pack()

hello()
root.mainloop()

# but=Button(root,image=img, command=hello,borderwidth=0)
# but.pack(padx=10,pady=10)


