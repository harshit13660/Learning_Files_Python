from functools import partial
from tkinter import *

root=Tk()

c=[]

def a(v):
    x=c[int(v)]
    x.destroy()

for i in range(5):
    k=Button(root,text=str(i),command=lambda p=i:a(p))
    k.pack()
    c.append(k)

print(c)
root.mainloop()