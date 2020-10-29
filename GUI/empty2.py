from PIL import Image, ImageTk

a=ImageTk.Image.open("start-jarvis.png")
n=a.resize((300,300))
n.show()