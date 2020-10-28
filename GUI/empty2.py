from PIL import Image, ImageTk

a=ImageTk.Image.open("start-jarvis.png")
n=a.rotate(-10)
n.show()