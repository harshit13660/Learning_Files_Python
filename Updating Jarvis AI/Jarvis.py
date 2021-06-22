from tkinter import *
from PIL import Image,ImageTk
from urllib.request import urlopen
from tkinter import filedialog
from tkinter import messagebox
from email.message import EmailMessage
import smtplib



import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import requests
import threading
import os
import time
import json
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

r.dynamic_energy_threshold=True
r.dynamic_energy_adjustment_ratio=1.5

r1.dynamic_energy_threshold=True
r1.dynamic_energy_adjustment_ratio=1.5
#https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
# For Speech recognition Documentation

termin=1
check_flag=0


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
    global check_flag

    jarvis_Reye_label.place_forget()
    jarvis_Leye_label.place_forget()

    def show_eyes():
        global jarvis_Reye_label
        global jarvis_Leye_label
        global sto
        if check_flag==1:
            eye_blink()
        elif check_flag==0:
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


def speaker(audio):
    engine.say(audio)
    engine.runAndWait()



#Creating Main Speaking Core Function
def Main_Jarvis_Speak():
    if termin==0:
        print("Speak terminated")
        return None
    else:

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
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source,timeout=7)
                    data = r.recognize_google(audio,language='en-US')
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
            print("Say! ( Wake Up) to awake......")
            lab_canvas.config(text="Say! (Wake Up) to awake...")
            lab_canvas.place(x=530,y=680)

            while True:
                try:
                    with mic as so:
                        r1.adjust_for_ambient_noise(so)
                        con = r1.listen(so,timeout=60)
                        jag = r1.recognize_google(con,language='en-US')
                        print(jag)
                        if jag == "wake up":
                            speaker("Yes Sir!")
                            break

                except Exception as e:
                    print(e)


        if __name__ == "__main__":
            wishme()
            while termin!=0:
                query = take()
                if query != None:
                    print(query)

                    if 'who are you' in query:
                        speaker(" Hi am jarvis! i can do basic tasks for you like playing songs,search, wikipedia, and weather forcast ")

                    elif 'tell me about' in query:
                        newsr = query.split("about", 1)
                        if newsr[1] == "":
                            speaker("about what?")
                            continue
                        speaker("ok")
                        a = wikipedia.summary(newsr[1], sentences=3)
                        print(a)
                        speaker(a)
                        awake()

                    elif 'search' in query:
                        speaker("ok")
                        newsr = query.split("search", 1)
                        kit.search(newsr[1])
                        awake()

                    elif 'play song' in query or 'play music' in query:
                        speaker("ok")
                        try:
                            newsr = query.split("song", 1)
                            kit.playonyt(newsr[1])
                            awake()
                        except Exception as e:
                            newsr = query.split("music", 1)
                            kit.playonyt(newsr[1])
                            awake()

                    elif 'weather' in query:
                        speaker("ok")
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=68355932828ffd7a3e72c27cad53d8ee'
                        a = requests.get(url).json()
                        wea = a['weather'][0]['description']
                        tem1 = round((a['main']['temp_min']) - 273.15, 2)
                        tem2 = round((a['main']['temp_max']) - 273.15, 2)
                        speaker(f"Today weather is {wea} with minimum temperature {tem1} degree celcius and Maximum temperature {tem2} degree celcius")
                        awake()

                    elif 'open' in query:
                        with open('Programs_Dict.json','r') as pd:
                            program_data=json.load(pd)
                            for p_data in program_data:
                                if query.split('open ')[1]==p_data:
                                    speaker("ok")
                                    os.startfile(program_data[p_data])
                                    pd.close()
                                    break

                                elif(list(program_data)[len(list(program_data))-1] != p_data):
                                    continue

                                else:
                                    speaker("No Target Found, Please Add Location")

                                    def user_entry(top_argument,top_win):
                                        write_to_dict = eval('{ "%s" : "%s" }' % (top_argument.lower(), root.filename.name))
                                        program_data.update(write_to_dict)
                                        print(program_data)
                                        with open('Programs_Dict.json', 'w') as pd:
                                            pd.write(json.dumps(program_data))
                                            pd.close()
                                        top_win.destroy()



                                    def top_asking():
                                        top_win = Toplevel()
                                        top_win.title("Add Files")
                                        top_win.geometry("400x100+483+234")
                                        top_win.config(background='#5bc4e8')
                                        top_Label = Label(top_win, text='How Would You Like To Call It?',bg='Black',fg='white').pack()
                                        speaker("How Would You Like To Call It?")
                                        top_Entry = Entry(top_win, width=80,bg='Black',fg="White",font=('Arial',13))
                                        top_Entry.pack()
                                        top_asking_button=Button(top_win,text="Ok",command=lambda:user_entry(top_Entry.get(),top_win)).pack()

                                    root.filename= filedialog.askopenfile(initialdir='C:\Program Files',title="Select a File ",filetypes=(("exe files",".exe"),("all files","*.*")))
                                    if root.filename!= None:
                                        top_asking()
                                        break
                            awake()

                    elif 'send email' in query:
                        speaker("ok")

                        global grid_row_data
                        grid_row_data = 4

                        def type_message(sender_email, server):
                            message = EmailMessage()
                            global email_send_dict
                            email_send_dict = {}

                            global add_files_count
                            add_files_count = 0

                            email_validating_label=0

                            def sending_threader():
                                threading.Thread(target=send_message).start()

                            def Add_files_func():
                                global email_validating_label
                                def remove_attached_files(rem_index, rem_cross):
                                    email_send_dict.pop(rem_index['text'])
                                    rem_cross.destroy()
                                    rem_index.destroy()

                                global add_files_count
                                global grid_row_data
                                global email_send_dict
                                message_type_window.address_of_file_em = filedialog.askopenfile(initialdir='C:\Program Files', title="Select a File ",filetypes=(("jpeg files", ".jpg"), ("all files", "*.*")),parent=message_type_window)
                                with open(message_type_window.address_of_file_em.name, 'rb') as em_file_obj:
                                    email_send_dict[message_type_window.address_of_file_em.name.split('/')[-1]] = em_file_obj.read()

                                if email_validating_label != 0:
                                    email_validating_label.destroy()
                                attachment_Label = Label(message_type_window, text=(message_type_window.address_of_file_em.name.split("/")[-1]),font="Ethnocentric 8 bold", bg="#042438", fg="white")
                                attachment_Label.grid(row=(grid_row_data + 1), column=1)
                                grid_row_data = attachment_Label.grid_info()['row']

                                remove_attachment_button = Button(message_type_window, text="X",font="Ethnocentric 8 bold", bg="#042438",fg="white", border=2)
                                remove_attachment_button.grid(row=grid_row_data, column=2)
                                remove_attachment_button.config(command=lambda rem_index=attachment_Label,rem_cross=remove_attachment_button: remove_attached_files(rem_index, rem_cross))
                                add_files_count += 1

                            def send_message():
                                global email_validating_label
                                message['From'] = sender_email
                                message['To'] = message_To_Entry.get()
                                message['Subject'] = message_Subject_Entry.get()
                                message.set_content(message_Body_Text.get('1.0', END))
                                if add_files_count != 0:
                                    for att_file_name, att_file in email_send_dict.items():
                                        message.add_attachment(att_file, maintype='application',subtype='octet-stream', filename=att_file_name)

                                try:
                                    if '@gmail.com' in message_To_Entry.get():
                                        message_type_window.destroy()
                                        server.send_message(message)
                                        speaker("Email has been Sent")
                                    else:
                                        email_validating_label=Label(message_type_window,text='Please Enter Valid Data or Check Your Network!',
                                              font="Ethnocentric 8 bold",
                                              bg="#042438",fg="red")
                                        email_validating_label.grid(row=5, column=1)
                                        message.clear()
                                        email_send_dict.clear()
                                        speaker("please enter valid email id")
                                except Exception as e:
                                    speaker("Email Not Sent, check you network")

                            message_type_window = Toplevel()
                            message_type_window.title('Message Body')
                            message_type_window.geometry("730x450+318+159")
                            message_type_window.config(background="#042438")
                            message_type_window.attributes('-topmost', 'true')
                            message_from_Label = Label(message_type_window,
                                                       text='From : ',
                                                       font="Ethnocentric 11 bold",
                                                       bg="#042438",fg="white").grid(row=0, column=0, pady=5)

                            message_from_Label = Label(message_type_window,
                                                       text=sender_email,
                                                       font="Helvetica 15 bold",
                                                       bg="#042438",fg="white").grid(row=0, column=1, pady=5)

                            message_To_Label = Label(message_type_window,
                                                     text="To",
                                                     font="Ethnocentric 11 bold",
                                                     bg="#042438",fg="white").grid(row=1, column=0, pady=5)

                            message_To_Entry = Entry(message_type_window, width=40, font="Helvetica 15 bold")
                            message_To_Entry.grid(row=1, column=1, pady=5)
                            message_Subject_label = Label(message_type_window,
                                                          text='Subject',
                                                          font="Ethnocentric 11 bold",
                                                          bg="#042438",fg="white").grid(row=2, column=0, pady=5)

                            message_Subject_Entry = Entry(message_type_window, width=40, font="Helvetica 15 bold")
                            message_Subject_Entry.grid(row=2, column=1, pady=5)
                            message_Body_Label = Label(message_type_window,
                                                       text="Body",
                                                       font="Ethnocentric 11 bold",
                                                       bg="#042438", fg="white").grid(row=3, column=0, pady=5)

                            message_Body_Text = Text(message_type_window, width=40, height=5,font="Helvetica 15 bold")
                            message_Body_Text.grid(row=3, column=1, pady=5)

                            Send_Button = Button(message_type_window, text='Send',command=sending_threader,font="Ethnocentric 15 bold")
                            Send_Button.grid(row=4, column=2, pady=5)

                            Add_Files_Button = Button(message_type_window,
                                                      text='Add Files',
                                                      command=Add_files_func,
                                                      font="Ethnocentric 11 bold").grid(row=4, column=1, pady=5)

                        def encript_data(sen, pas):
                            list_sen = [ord(x1) for x1 in sen]
                            encrypted_list_sen = ' '.join([str(x1 + 20) for x1 in list_sen])
                            list_pas = [ord(x2) for x2 in pas]
                            encrypted_list_pas = ' '.join([str(x2 + 20) for x2 in list_pas])
                            return encrypted_list_sen, encrypted_list_pas

                        def decrypt_data(em_saved, ps_saved):
                            list_em_saved = em_saved.split(" ")
                            decrypt_em_saved = "".join([chr(int(f) - 20) for f in list_em_saved])
                            list_ps_saved = ps_saved.split(" ")
                            decrypt_ps_saved = "".join([chr(int(po) - 20) for po in list_ps_saved])
                            return decrypt_em_saved, decrypt_ps_saved

                        def email_pass_entry():
                            first_email_window = Toplevel()
                            first_email_window.title('Login')
                            first_email_window.geometry("700x150+333+309")
                            first_email_window.config(background='#042438')
                            first_email_window.resizable(False, True)
                            first_email_window.attributes('-topmost', 'true')
                            first_email_username = Label(first_email_window, text="Enter Email",
                                                         font="Ethnocentric 11 bold", bg="#042438",
                                                         fg="white").grid(row=0, column=0)

                            first_email_entry = Entry(first_email_window, width=30, font=('Arial 20'))
                            first_email_entry.grid(row=0, column=1)

                            first_email_pass = Label(first_email_window,
                                                     text="Enter Password",
                                                     font="Ethnocentric 11 bold",
                                                     bg="#042438",fg="white").grid(row=1, column=0)

                            first_pass_entry = Entry(first_email_window, width=30, font=('Arial 20'))
                            first_pass_entry.grid(row=1, column=1)

                            first_login = Button(first_email_window,
                                                 text='Login',
                                                 command=lambda: Email_Login(first_email_entry.get(),first_pass_entry.get(),first_email_window),
                                                 font=("Ethnocentric 11 bold"))
                            first_login.grid(column=1, pady=10)


                        def Email_Login(sender_email, sender_password, first_email_window):
                            try:
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.ehlo()
                                server.starttls()
                                server.login(sender_email, sender_password)
                                print("Login success")
                                ascii_email, ascii_pass = encript_data(sender_email, sender_password)
                                saved_emails = eval('{"%s":"%s"}' % (ascii_email, ascii_pass))
                                with open("data.json", 'r+') as e_object:
                                    new_em_upodate = eval(e_object.read())
                                    new_em_upodate.update(saved_emails)
                                    e_object.seek(0)
                                    e_object.write(json.dumps(new_em_upodate))
                                    e_object.close()
                                first_email_window.destroy()
                                type_message(sender_email, server)
                            except Exception as e:
                                speaker("Wrong Email or Password! Login Failed")

                        def choose_or_add_email(em_saved, ps_saved, saved_email_window):
                            Email_Login(em_saved, ps_saved, saved_email_window)

                        def Add_email_func(saved_email_window):
                            saved_email_window.destroy()
                            email_pass_entry()

                        def saved_email_login():
                            def confirm_em_remove(frame_index, button_index):
                                pop_message = messagebox.askyesno("Confirm","Do you really want to remove account?",parent=saved_email_window)
                                if pop_message == 1:
                                    file_to_remove = open("data.json", 'r')
                                    updated_file_to_remove = eval(file_to_remove.read())
                                    updated_file_to_remove.pop(button_index)
                                    file_to_remove.close()
                                    file_to_remove = open("data.json", 'w')
                                    file_to_remove.write(json.dumps(updated_file_to_remove))
                                    file_to_remove.close()
                                    frame_index.destroy()

                            saved_email_window = Toplevel()
                            saved_email_window.title("Select Email")
                            saved_email_window.geometry("700x200+333+284")
                            saved_email_window.config(background='#042438')
                            saved_email_window.resizable(False, True)
                            saved_email_window.attributes('-topmost','true')
                            saved_em_file = eval(open('data.json', 'r').read())
                            for em_saved, ps_saved in saved_em_file.items():
                                decrypted_em_saved, decrypted_ps_saved = decrypt_data(em_saved, ps_saved)
                                frame = LabelFrame(saved_email_window, borderwidth=0, bg="#042438", pady=5)
                                frame.pack()
                                saved_em_button = Button(frame,text=decrypted_em_saved,
                                                         command=lambda lam_em_saved=decrypted_em_saved,lam_ps_saved=decrypted_ps_saved: choose_or_add_email(lam_em_saved,lam_ps_saved,saved_email_window),
                                                         font="Ethnocentric 11 bold",
                                                         bg="#042438", fg="white",
                                                         pady=6, border=6)
                                saved_em_button.grid(row=0, column=0, pady=10)

                                remove_saved_em_button = Button(frame,text="X",
                                                                command=lambda frame_index=frame,button_index=em_saved: confirm_em_remove(frame_index, button_index),
                                                                font="Ethnocentric 11 bold",
                                                                bg="#042438",fg="white",
                                                                pady=6, border=4)
                                remove_saved_em_button.grid(row=0, column=2, padx=15, pady=10)

                            add_new_email = Button(saved_email_window, text="Add New Email",
                                                   command=lambda: Add_email_func(saved_email_window),
                                                   font="Ethnocentric 11 bold",
                                                   fg="black",border=5).pack(pady=10)

                        if (os.stat('data.json').st_size == 0):
                            email_pass_entry()
                            awake()
                        else:
                            saved_email_login()
                            awake()


                    elif 'turn off' in query:
                        os._exit(1)
                    else:
                        speaker("Sorry! i didn't recognize speak again")



def canvas_expand():
    canvas_size=0
    global check_flag
    while canvas_size != 500:
        commands_Label.config(width=(canvas_size)+200, height=(canvas_size),highlightthickness=1)
        canvas_size += 10
        time.sleep(0.01)
    commands_Label.create_text(350,40,text="Who Are You",font="Ethnocentric 11 bold",fill='white')
    commands_Label.create_text(350, 70, text="Tell Me About 'querry'", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 100, text="Play Song 'song name'", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 130, text="Search 'querry'", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 160, text="Weather Forcast", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 190, text="Open 'Filename'", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 220, text="Send Email", font="Ethnocentric 11 bold", fill='white')
    commands_Label.create_text(350, 250, text="Turn Off", font="Ethnocentric 11 bold", fill='white')
    check_flag = 1

def canvas_contract():
    canvas_size=500
    global check_flag
    while canvas_size!=0:
        commands_Label.config(width=(canvas_size+100),height=(canvas_size),highlightthickness=1)
        canvas_size-=10
        time.sleep(0.005)
    commands_Label.config(highlightthickness=0)
    check_flag = 0


def command_list():
    global check_flag
    if po!= None:
        stop_spin()
        if check_flag==0:
            jarvis_Reye_label.place_forget()
            jarvis_Leye_label.place_forget()
            command_button.config(fg='grey')
            threading.Thread(target=canvas_expand).start()

        elif check_flag==1:
            command_button.config(fg='white')
            threading.Thread(target=canvas_contract).start()
    else:
        if check_flag == 0:
            jarvis_Reye_label.place_forget()
            jarvis_Leye_label.place_forget()
            command_button.config(fg='grey')
            threading.Thread(target=canvas_expand).start()

        elif check_flag == 1:
            command_button.config(fg='white')
            threading.Thread(target=canvas_contract).start()





#Window kill function
def kill():
    os._exit(1)

#Function to check internet connection
def internet():
    global termin
    while True:
        try:
            urlopen('https://www.google.com',timeout=1)
            canvas_internet.config(text="Internet Connection",fg="white")

        except Exception as e:
            termin=0
            stop_spin()
            speaker("Your Internet Connection Is Not Stable")
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


#-----------------------Top Left command button-----------------
command_button=Button(root,text='Commands',command=command_list, font="Ethnocentric 11 bold" ,padx=2, pady=2,bg="#090909",fg="#e8feff",border=10)
command_button.place(x=80,y=45)

#------------------------Command Label----------------------------
commands_Label=Canvas(width=1,height=1,bg='#0a0a0a',highlightthickness=0,highlightbackground='#5bc4e8')
commands_Label.place(x=335,y=66)



canvas_internet=Label(root,text=" ",font="Ethnocentric 11 bold", fg="#e8feff",bg="#090909")
canvas_internet.place(x=1000,y=45)



root.resizable(0,0)
threading.Thread(target=internet).start()
heart_spin()
root.mainloop()


