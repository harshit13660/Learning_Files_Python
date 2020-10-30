from tkinter import *
from PIL import Image,ImageTk
import pygame
import time
import sys

# -----------------------I N I T I A L I S A T I O N------------------

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



# ------------------------F U N C T I O N S--------------

#Jarvis starting rotating function
number=0
po=None
def start_button_function():
    """ Jarvis start button spinning function"""
    global number
    global start_button
    global start_jarvis_img
    global po

    number = number - 7
    z = resized_start_jarvis.rotate(number)
    start_jarvis_img = ImageTk.PhotoImage(z)
    start_button.config(image=start_jarvis_img,state=DISABLED)
    stop_button.config(state=NORMAL)
    po=start_button.after(40, start_button_function)

#Jarvis start buton spin stopping function
def stop_spin():
    """ Stoping start button spin"""
    global start_button
    jarvis_Leye_label.place_forget()
    jarvis_Reye_label.place_forget()
    root.after_cancel(po)
    root.after_cancel(bfo)
    root.after_cancel(sto)
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

# Creating Eye Blinking Function
sto = None
bfo=None
def eye_blink():
    global jarvis_Reye_label
    global jarvis_Leye_label
    global bfo

    jarvis_Reye_label.place_forget()
    jarvis_Leye_label.place_forget()

    def show_eyes():
        global jarvis_Reye_label
        global jarvis_Leye_label
        global sto

        jarvis_Reye_label = Label(root, image=jarvis_Reye, bg="#081f2d")
        jarvis_Reye_label.place(x=703, y=166)

        jarvis_Leye_label = Label(root, image=jarvis_Leye, bg="#081f2d")
        jarvis_Leye_label.place(x=619, y=166)
        sto=jarvis_Leye_label.after(1000, eye_blink)

    bfo=jarvis_Leye_label.after(1000, show_eyes)

def main_start_function():
    start_button_function()
    eye_blink()


root.protocol("WM_DELETE_WINDOW", sys.exit)

#           ---------------L A B E L S--------------------

#initialize Jarvis start button pic
start_jarvis = Image.open("jarvis_start_pic.png")
resized_start_jarvis = start_jarvis.resize((220,220),Image.ANTIALIAS)
start_jarvis_img = ImageTk.PhotoImage(resized_start_jarvis)
lop=start_jarvis_img

#Creating jarvis start button
start_button=Button(root,image=start_jarvis_img,bg="#090909", command=main_start_function,bd=0,activebackground="#090909")
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

# Creating Jarvis Eyes
jarvis_Leye_initialization = Image.open("left-eye.png")
resize_jarvis_Leye= jarvis_Leye_initialization.resize((50,20))
jarvis_Leye= ImageTk.PhotoImage(resize_jarvis_Leye)

#Creating Jarvis Left Eye Label
jarvis_Leye_label=Label(root,image=jarvis_Leye,bg="#081f2d")
jarvis_Leye_label.place(x=619,y=166)

# Creating jarvis right eye
jarvis_Reye_initialization = Image.open("right-eye.png")
resize_jarvis_Reye = jarvis_Reye_initialization.resize((50,20))
jarvis_Reye = ImageTk.PhotoImage(resize_jarvis_Reye)

#Creating Jarvis Right Eye Label
jarvis_Reye_label = Label(root,image=jarvis_Reye,bg="#081f2d")
jarvis_Reye_label.place(x=703,y=166)



heart_spin()
root.mainloop()


