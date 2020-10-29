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
po=None
def start_button_function():
    """ Jarvis start button spinning function"""
    global number
    global start_button
    global start_jarvis_img
    global po

    number = number - 10
    z = resized_start_jarvis.rotate(number)
    start_jarvis_img = ImageTk.PhotoImage(z)
    start_button.config(image=start_jarvis_img,state=DISABLED)
    stop_button.config(state=NORMAL)
    po=start_button.after(50, start_button_function)


def stop_spin():
    """ Stoping start button spin"""
    global start_button
    root.after_cancel(po)
    start_button.config(image=lop,state=NORMAL,bg="#090909")
    stop_button.config(state=DISABLED)


#jarvis heart spining function
ang=0
def heart_spin():
    global resized_jarvis_heart_initialize
    global ang
    global jarvis_heart
    global jarvis_heart_label

    ang=ang-5
    rotated_heart= resized_jarvis_heart_initialize.rotate(ang)
    jarvis_heart=ImageTk.PhotoImage(rotated_heart)
    jarvis_heart_label.config(image=jarvis_heart)
    jarvis_heart_label.after(50, heart_spin)


#initialize Jarvis start button pic
start_jarvis = Image.open("jarvis_start_pic.png")
resized_start_jarvis = start_jarvis.resize((220,220),Image.ANTIALIAS)
start_jarvis_img = ImageTk.PhotoImage(resized_start_jarvis)
lop=start_jarvis_img

#Creating jarvis start button
start_button=Button(root,image=start_jarvis_img,bg="#090909", command=start_button_function,bd=0,activebackground="#090909")
start_button.place(x=100,y=420)

#Creating Stop Image and Button
stop_image = ImageTk.PhotoImage(Image.open("stop.png"))
stop_button = Button(root,image=stop_image,command=stop_spin,bg="#090909",bd=0,state=DISABLED,activebackground="#090909")
stop_button.place(x=1050,y=420)

#Initialising Jarvis heart image
jarvis_heart_initialize = Image.open("jarvis-heart.png")
resized_jarvis_heart_initialize = jarvis_heart_initialize.resize((130,130))
jarvis_heart=ImageTk.PhotoImage(resized_jarvis_heart_initialize)

#Creating jarvis heart label
jarvis_heart_label=Label(root,image=jarvis_heart,bg="#081f2d")
jarvis_heart_label.place(x=621,y=480)



heart_spin()
root.mainloop()


