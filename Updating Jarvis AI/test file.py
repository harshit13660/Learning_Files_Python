from tkinter import *
from functools import partial

win = Tk()
button_identities = []

def change(n):
    # function to get the index and the identity (bname)
    # print(n)
    bname = (button_identities[n])
    bname.destroy()

for i in range(5):
    # creating the buttons, assigning a unique argument (i) to run the function (change)
    button = Button(win, width=10, text=str(i), command=partial(change,i))
    button.pack()
    # add the button's identity to a list:
    print(button['command'])
    button_identities.append(button)

# just to show what happens:
print(button_identities)

win.mainloop()