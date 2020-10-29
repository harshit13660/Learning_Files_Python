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
pic=Image.open("background.png")
resized=pic.resize((w,h),Image.ANTIALIAS)

#Set Background image
img_backg=ImageTk.PhotoImage(resized)
lab=Label(root,image=img_backg)
lab.pack()




#Jarvis starting rotating function
number=0
po="lo"
def hello():
    global number
    global start_button
    global start_jarvis_img
    global po

    number = number - 10
    z = resized_start_jarvis.rotate(number)
    start_jarvis_img = ImageTk.PhotoImage(z)
    start_button.config(image=start_jarvis_img,state=DISABLED)
    stop_button.config(state=NORMAL)
    po=start_button.after(50, hello)

def stop_spin():
    global start_button
    root.after_cancel(po)
    start_button.config(image=lop,state=NORMAL,bg="#090909")
    stop_button.config(state=DISABLED)





start_jarvis = Image.open("123.png")
resized_start_jarvis = start_jarvis.resize((220,220),Image.ANTIALIAS)
start_jarvis_img = ImageTk.PhotoImage(resized_start_jarvis)
lop=start_jarvis_img

start_button=Button(root,image=start_jarvis_img,bg="#090909", command=hello,bd=0,activebackground="#090909")
start_button.place(x=100,y=420)

#Creating Stop Image and Button
stop_image = ImageTk.PhotoImage(Image.open("stop.png"))
stop_button = Button(root,image=stop_image,command=stop_spin,bg="#090909",bd=0,state=DISABLED,activebackground="#090909")
stop_button.place(x=1050,y=420)

root.mainloop()


