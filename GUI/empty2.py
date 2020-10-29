from tkinter import *

main=Tk()

main['bg']='green'

photo=PhotoImage(file='pen.png')
Label(main,image=photo,bg='grey').place(x=20,y=30)
#your other label or button or ...
main.wm_attributes("-transparentcolor", 'black')
main.mainloop()