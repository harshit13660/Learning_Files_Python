from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1980x1600')
root.minsize(200,300)
root.title("AI-JARVIS")

h=root.winfo_screenheight()
w=root.winfo_screenwidth()
print(h,w)

pic=Image.open("pi.jpg")
resized=pic.resize((w,h),Image.ANTIALIAS)

img=ImageTk.PhotoImage(resized)
lab=Label(root,image=img)
lab.pack()




root.mainloop()


