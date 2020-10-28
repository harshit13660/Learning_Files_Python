from tkinter import *
from PIL import Image,ImageTk
import pygame

root=Tk()
a=root.geometry('1980x1600')
root.minsize(200,300)
root.title("AI-JARVIS")

h=root.winfo_screenheight()
w=root.winfo_screenwidth()

pic=Image.open("iron-man.jpg")
resized=pic.resize((w,h),Image.ANTIALIAS)

img_backg=ImageTk.PhotoImage(resized)
lab=Label(root,image=img_backg)
lab.pack()

img_start= pygame.image.load("start-jarvis.png")
a.blit(img_start,(200,200))





root.mainloop()


