from tkinter import *
import cv2
import os
from PIL import ImageTk,Image
import time

root=Tk()
# root.geometry("500x500")
# cap=cv2.VideoCapture("voice.mp4")
# a=0
# ret=True
# os.chdir("C:\\Users\\Harshit\\Desktop\\new")
# while ret:
#     ret,frame=cap.read()
#     if ret==False:
#         break
#     cv2.imwrite(f"h{a}.jpg",frame)
#     a=a+1

# def hello():
#     m=0
#     for i in range(a):
#         di="C:\\Users\\Harshit\\Desktop\\new" + f"\\h{m}.jpg"
#         img=ImageTk.PhotoImage(Image.open(di))
#         lab=Label(image=img).pack()
#         time.sleep(1)
#          m+=1
#
#
# b=Button(text="button",bg="green",command=hello).pack()
a=1
def imor():
    # global a
    img=ImageTk.PhotoImage(Image.open("2.png"))
    lab=Label(image=img)
    lab.pack()
    # a=a+1
    # lab.grid_forget()


b=Button(root,text="load",command=imor)
b.grid(row=1,column=2)

root.mainloop()

