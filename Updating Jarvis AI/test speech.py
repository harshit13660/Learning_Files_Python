import speech_recognition as sr

r=sr.Recognizer()
r.dynamic_energy_threshold=True
r.dynamic_energy_adjustment_ratio=1.5
mic=sr.Microphone()
with mic as source:
    print('Speak')
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    data=r.recognize_google(audio,language='en-US')
    print(data)

