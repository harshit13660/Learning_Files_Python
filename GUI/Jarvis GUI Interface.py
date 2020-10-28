from tkinter import *
from PIL import Image,ImageTk
import pygame

#Initialize tkinter and window
root=Tk()
a=root.geometry('1980x1600')
root.minsize(200,300)
root.title("AI-JARVIS")

#Get window width and height
h=root.winfo_screenheight()
w=root.winfo_screenwidth()

#Open Background Iron Man Jarvis Image
pic=Image.open("iron-man.jpg")
resized=pic.resize((w,h),Image.ANTIALIAS)

#Set Background image
img_backg=ImageTk.PhotoImage(resized)
lab=Label(root,image=img_backg)
lab.pack()


#Jarvis starting rotating function
a=0
def hello():
    global a
    global start_button
    global start_jarvis_img
    a = a - 5
    z = start_jarvis.rotate(a)
    start_jarvis_img = ImageTk.PhotoImage(z)
    start_button.config(image=start_jarvis_img,state=DISABLED)
    start_button.after(50, hello)

start_jarvis = Image.open("start-jarvis.png")
start_jarvis_img = ImageTk.PhotoImage(start_jarvis)

start_button=Button(root,image=start_jarvis_img, command=hello, bd=10, bg='Black')
start_button.place(x=30,y=40)


root.mainloop()


