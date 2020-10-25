import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import requests


engine= pyttsx3.init('sapi5')
engine.setProperty('rate',180)

r=sr.Recognizer()
r1=sr.Recognizer()

mic=sr.Microphone()

r.energy_threshold=700
r1.energy_threshold=700
r.pause_threshold=0.7
r1.pause_threshold=0.5


def speaker(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    a=datetime.datetime.now().hour
    if a<12:
        speaker("Good Morning")
    elif a>=12 and a<16:
        speaker("Good Afternoon")
    else:
        speaker("Good Evening")
    speaker("How can i help you")

def take():
    try:
        with mic as source:
            print("Speak......")
            audio=r.listen(source)
            data=r.recognize_google(audio)
            return data.lower()

    except Exception as e:
        speaker("Sorry! Please say again")
        take()



def awake():
    print("Say! ( Jarvis ) to awake......")
    w=0
    while w!=1:
        try:
            with mic as so:
                con = r1.listen(so)
                jag=r1.recognize_google(con)
                print(jag)
                if jag=="Jarvis":
                    speaker("Yes Sir!")
                    w=1
        except Exception as e:
            pass


if __name__=="__main__":
    wishme()
    while True:
        query=take()
        if query!= None:
            print(query)

            if 'hi jarvis' in query:
                speaker(" Hi am jarvis! i can do basic tasks for you like playing songs,search, wikipedia, and weather forcast ")

            elif 'tell me about' in query:
                newsr=query.split("about",1)
                if newsr[1]=="":
                    speaker("about what?")
                    continue
                a=wikipedia.summary(newsr[1],sentences=3)
                print(a)
                speaker(a)
                awake()

            elif 'search' in query:
                newsr=query.split("search",1)
                kit.search(newsr[1])
                awake()

            elif 'play song' in query or 'play music' in query:
                try:
                    newsr=query.split("song",1)
                    kit.playonyt(newsr[1])
                    awake()
                except Exception as e:
                    newsr = query.split("music",1)
                    kit.playonyt(newsr[1])
                    awake()

            elif 'weather' in query:
                url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=68355932828ffd7a3e72c27cad53d8ee'
                a = requests.get(url).json()
                wea= a['weather'][0]['description']
                tem1= (a['main']['temp_min'])-273.15
                tem2= (a['main']['temp_max'])-273.15
                speaker(f"Today weather is {wea} with minimum temperature {tem1} degree celcius and Maximum temperature {tem2} degree celcius")

            elif 'exit' in query:
                exit()
            else:
                speaker("Sorry! i didn't recognize speak again")



