from tkinter import font
from tkinter import *
root=Tk()


my=list(font.families())
for i in my:
    if "Ethnocentric" in i:
        print("found")
        break


root.mainloop()