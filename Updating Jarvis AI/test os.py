from tkinter import *
import smtplib
import os
import json

root=Tk()
root.geometry("700x700")
def send_email():

    def encript_data(sen,pas):
        list_sen = [ord(x1) for x1 in sen]
        encrypted_list_sen = ' '.join([str(x1+20) for x1 in list_sen])
        list_pas = [ord(x2) for x2 in pas]
        encrypted_list_pas = ' '.join([str(x2+20) for x2 in list_pas])
        return encrypted_list_sen,encrypted_list_pas

    def decrypt_data(em_saved,ps_saved):
        list_em_saved=em_saved.split(" ")
        decrypt_em_saved="".join([chr(int(f)-20) for f in list_em_saved])
        list_ps_saved=ps_saved.split(" ")
        decrypt_ps_saved="".join([chr(int(po)-20) for po in list_ps_saved])
        return decrypt_em_saved, decrypt_ps_saved


    def email_pass_entry():
        first_email_window= Toplevel()
        first_email_window.title('Login')
        first_email_window.geometry("700x100+483+234")
        first_email_username= Label(first_email_window,text="Enter Email",font="Ethnocentric 9 bold").grid(row=0,column=0)
        first_email_entry= Entry(first_email_window, width=30,font=('Arial 20'))
        first_email_entry.grid(row=0,column=1)
        first_email_pass = Label(first_email_window, text="Enter Password",font="Ethnocentric 9 bold").grid(row=1,column=0)
        first_pass_entry = Entry(first_email_window, width=30,font=('Arial 20'))
        first_pass_entry.grid(row=1,column=1)
        first_login=Button(first_email_window,text='Login',command=lambda:Email_Login(first_email_entry.get(),first_pass_entry.get(),first_email_window),font=("Ethnocentric 11 bold"))
        first_login.grid(column=1)

#"Wrong Email or Password! Login Failed"
    def Email_Login(sender_email,sender_password,first_email_window):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(sender_email,sender_password)
            print("Login success")
            ascii_email, ascii_pass=encript_data(sender_email,sender_password)
            saved_emails=eval('{"%s":"%s"}'% (ascii_email,ascii_pass))
            with open("data.json",'r+') as e_object:
                new_em_upodate=eval(e_object.read())
                new_em_upodate.update(saved_emails)
                e_object.seek(0)
                e_object.write(json.dumps(new_em_upodate))
                e_object.close()
            first_email_window.destroy()
        except Exception as e:
            print(e)

    def choose_or_add_email(em_saved,ps_saved,saved_email_window):
        Email_Login(em_saved,ps_saved,saved_email_window)

    def Add_email_func(saved_email_window):
        saved_email_window.destroy()
        email_pass_entry()


    def saved_email_login():
        saved_email_window=Toplevel()
        saved_email_window.title("Select Email")
        saved_email_window.geometry("700x100+483+234")
        saved_em_file=eval(open('data.json','r').read())
        for em_saved,ps_saved in saved_em_file.items():
            decrypted_em_saved,decrypted_ps_saved=decrypt_data(em_saved,ps_saved)
            saved_em_button=Button(saved_email_window,text=decrypted_em_saved,command=lambda:choose_or_add_email(decrypted_em_saved,decrypted_ps_saved,saved_email_window)).pack(pady=3)
        add_new_email=Button(saved_email_window,text="Add New Email",command=lambda:Add_email_func(saved_email_window)).pack(pady=3)


    if (os.stat('data.json').st_size == 0):
        email_pass_entry()
    else:
        saved_email_login()


send_email()
root.mainloop()
