from tkinter import *
from PIL import Image,ImageTk
from urllib.request import urlopen

import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import requests
import threading
import os


# -----------------------I N I T I A L I S A T I O N------------------

#Initialize tkinter and window
root=Tk()
a=root.geometry('1366x768')
root.minsize(200,300)
root.title("AI-JARVIS")


#Open Background Iron Man Jarvis Image
pic=Image.open("background.png")
resized=pic.resize((1366,768),Image.ANTIALIAS)

#Set Background image
img_backg=ImageTk.PhotoImage(resized)
lab=Label(root,image=img_backg)
lab.pack()

engine= pyttsx3.init('sapi5')
engine.setProperty('rate',180)

r=sr.Recognizer()
r1=sr.Recognizer()

mic=sr.Microphone()

r.energy_threshold=1000
r1.energy_threshold=800
r.pause_threshold=0.7
r1.pause_threshold=0.5

termin=1



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

#Jarvis stop buton stopping function
def stop_spin():
    """ Stoping start button spin"""
    global start_button
    global termin
    jarvis_Leye_label.place_forget()
    jarvis_Reye_label.place_forget()
    root.after_cancel(po)
    root.after_cancel(bfo)
    root.after_cancel(sto)
    start_button.config(image=lop, state=NORMAL, bg="#090909")
    stop_button.config(state=DISABLED)
    termin=0
    lab_canvas.config(text="Terminated")
    lab_canvas.place(x=620, y=680)

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
        jarvis_Reye_label.place(x=703, y=180)

        jarvis_Leye_label = Label(root, image=jarvis_Leye, bg="#081f2d")
        jarvis_Leye_label.place(x=619, y=180)
        sto=jarvis_Leye_label.after(1000, eye_blink)

    bfo=jarvis_Leye_label.after(1000, show_eyes)

#Creating combined main start function
def main_start_function():
    global termin
    start_button_function()
    eye_blink()
    termin=1
    threading.Thread(target=Main_Jarvis_Speak).start()



#Creating Main Speaking Core Function
def Main_Jarvis_Speak():
    if termin==0:
        print("Speak terminated")
        return None
    else:
        def speaker(audio):
            engine.say(audio)
            engine.runAndWait()

        def wishme():
            a = datetime.datetime.now().hour
            if a < 12:
                speaker("Good Morning")
            elif a >= 12 and a < 16:
                speaker("Good Afternoon")
            else:
                speaker("Good Evening")
            speaker("How can i help you")

        def take():
            try:
                with mic as source:
                    print("Speak......")
                    lab_canvas.config(text="SPEAK....")
                    lab_canvas.place(x=620,y=680)
                    audio = r.listen(source,timeout=7)
                    data = r.recognize_google(audio)
                    if termin==0:
                        return None
                    else:
                        return data.lower()

            except Exception as e:
                if termin==0:
                    return None
                else:
                    lab_canvas.config(text="Sorry! Please Say Again")
                    lab_canvas.place(x=530,y=680)

                    speaker("Sorry! Please say again")
                    take()

        def awake():
            print("Say! ( Jarvis ) to awake......")
            lab_canvas.config(text="Say! (Jarvis) to awake...")
            lab_canvas.place(x=530,y=680)
            w = 0
            while w != 1:
                try:
                    with mic as so:
                        con = r1.listen(so)
                        jag = r1.recognize_google(con)
                        print(jag)
                        if jag == "Jarvis":
                            speaker("Yes Sir!")
                            w = 1
                except Exception as e:
                    pass

        if __name__ == "__main__":
            wishme()
            while termin!=0:
                query = take()
                if query != None:
                    print(query)

                    if 'hi jarvis' in query:
                        speaker(" Hi am jarvis! i can do basic tasks for you like playing songs,search, wikipedia, and weather forcast ")

                    elif 'tell me about' in query:
                        newsr = query.split("about", 1)
                        if newsr[1] == "":
                            speaker("about what?")
                            continue
                        a = wikipedia.summary(newsr[1], sentences=3)
                        print(a)
                        speaker(a)
                        awake()

                    elif 'search' in query:
                        newsr = query.split("search", 1)
                        kit.search(newsr[1])
                        awake()

                    elif 'play song' in query or 'play music' in query:
                        try:
                            newsr = query.split("song", 1)
                            kit.playonyt(newsr[1])
                            awake()
                        except Exception as e:
                            newsr = query.split("music", 1)
                            kit.playonyt(newsr[1])
                            awake()

                    elif 'weather' in query:
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=68355932828ffd7a3e72c27cad53d8ee'
                        a = requests.get(url).json()
                        wea = a['weather'][0]['description']
                        tem1 = (a['main']['temp_min']) - 273.15
                        tem2 = (a['main']['temp_max']) - 273.15
                        speaker(f"Today weather is {wea} with minimum temperature {tem1} degree celcius and Maximum temperature {tem2} degree celcius")

                    elif 'exit' in query:
                        exit()
                    else:
                        speaker("Sorry! i didn't recognize speak again")


#Window kill function
def kill():
    os._exit(1)

#Function to check internet connection
def internet():
    global termin
    while True:
        try:
            urlopen('https://www.google.com',timeout=1)
            canvas_internet.config(text="Internet Connection")

        except Exception as e:
            termin=0
            canvas_internet.config(text="No Internet Connection",fg="red")




root.protocol("WM_DELETE_WINDOW", kill)

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
jarvis_Leye_label.place(x=619,y=180)

# Creating jarvis right eye
jarvis_Reye_initialization = Image.open("right-eye.png")
resize_jarvis_Reye = jarvis_Reye_initialization.resize((50,20))
jarvis_Reye = ImageTk.PhotoImage(resize_jarvis_Reye)

#Creating Jarvis Right Eye Label
jarvis_Reye_label = Label(root,image=jarvis_Reye,bg="#081f2d")
jarvis_Reye_label.place(x=703,y=180)

# -----------------------C A N V A S -------------------

bottom_canvas= Canvas(root, height=40,width=400,bg="#090909")
bottom_canvas.place(x=490,y=670)
lab_canvas=Label(root,text="J.A.R.V.I.S",font="Ethnocentric 11 bold",fg="white",bg="#090909")
lab_canvas.place(x=620,y=680)

top_right_canvas = Canvas(root, height=140,width=500,bg="#090909",highlightthickness=1)
top_right_canvas.place(x=800,y=25)
top_right_canvas.create_text(50,65,text="SPEAK",font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_line(84,63,130,63,fill="white",)
top_right_canvas.create_line(130,0,130,300,fill="white")
top_right_canvas.create_text(200,13,text="Hi Jarvis",font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_text(290,33,text="Tell Me About 'querry'" ,font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_text(248,55,text="Search 'querry'",font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_text(288,75,text="Play Song 'Song Name'",font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_text(258,94,text="Weather Forcast",font="Ethnocentric 11 bold",fill="#e8feff")
top_right_canvas.create_text(167,113,text="Exit",font="Ethnocentric 11 bold",fill="#e8feff")

top_left_canvas = Canvas(root, height=30,width=350,bg="#090909",highlightthickness=1)
top_left_canvas.place(x=60,y=40)

canvas_internet=Label(root,text=" ",font="Ethnocentric 11 bold", fg="#e8feff",bg="#090909")
canvas_internet.place(x=75,y=45)



root.resizable(0,0)
threading.Thread(target=internet).start()
heart_spin()
root.mainloop()


