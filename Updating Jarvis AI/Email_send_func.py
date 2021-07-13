from tkinter import *
import smtplib
import os
import json
from tkinter import messagebox
from email.message import EmailMessage
from tkinter import filedialog
import threading

root=Tk()
root.geometry("700x700")
def send_email():

    global grid_row_data
    grid_row_data=4

    def type_message(sender_email,server):
        message = EmailMessage()
        global email_send_dict
        email_send_dict = {}

        global add_files_count
        add_files_count=0

        def sending_threader():
            threading.Thread(target=send_message).start()

        def Add_files_func():

            def remove_attached_files(rem_index,rem_cross):
                email_send_dict.pop(rem_index['text'])
                rem_cross.destroy()
                rem_index.destroy()


            global add_files_count
            global grid_row_data
            global email_send_dict
            message_type_window.address_of_file_em=filedialog.askopenfile(initialdir='C:\Program Files',title="Select a File ",filetypes=(("jpeg files",".jpg"),("all files","*.*")))
            with open(message_type_window.address_of_file_em.name,'rb') as em_file_obj:
                email_send_dict[message_type_window.address_of_file_em.name.split('/')[-1]] = em_file_obj.read()

            attachment_Label=Label(message_type_window,text=(message_type_window.address_of_file_em.name.split("/")[-1]),font="Ethnocentric 8 bold",bg="#042438",fg="white")
            attachment_Label.grid(row=(grid_row_data+1),column=1)
            grid_row_data=attachment_Label.grid_info()['row']

            remove_attachment_button=Button(message_type_window,text="X",font="Ethnocentric 8 bold",bg="#042438",fg="white",border=2)
            remove_attachment_button.grid(row=grid_row_data,column=2)
            remove_attachment_button.config(command=lambda rem_index=attachment_Label,rem_cross=remove_attachment_button:remove_attached_files(rem_index,rem_cross))
            add_files_count += 1


        def send_message():
            message['From'] = sender_email
            message['To'] = message_To_Entry.get()
            message['Subject'] = message_Subject_Entry.get()
            message.set_content(message_Body_Text.get('1.0',END))
            if add_files_count!=0:
                for att_file_name, att_file in email_send_dict.items():
                    message.add_attachment(att_file, maintype='application', subtype='octet-stream',filename=att_file_name)
            if '@gmail.com' in message_To_Entry.get():
                message_type_window.destroy()
                server.send_message(message)
            else:
                Label(message_type_window,text='Please Enter Valid Data or Check Your Network!',font="Ethnocentric 8 bold",bg="#042438",fg="red").grid(row=5,column=1)
                message.clear()
                email_send_dict.clear()


        message_type_window=Toplevel()
        message_type_window.title('Message Body')
        message_type_window.geometry("750x450+483+234")
        message_type_window.config(background="#042438")
        message_from_Label=Label(message_type_window,text='From : ',font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=0,column=0,pady=5)
        message_from_Label=Label(message_type_window,text=sender_email,font="Helvetica 15 bold",bg="#042438",fg="white").grid(row=0,column=1,pady=5)
        message_To_Label=Label(message_type_window,text="To",font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=1,column=0,pady=5)
        message_To_Entry=Entry(message_type_window,width=40,font="Helvetica 15 bold")
        message_To_Entry.grid(row=1,column=1,pady=5)
        message_Subject_label=Label(message_type_window,text='Subject',font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=2,column=0,pady=5)
        message_Subject_Entry=Entry(message_type_window,width=40,font="Helvetica 15 bold")
        message_Subject_Entry.grid(row=2,column=1,pady=5)
        message_Body_Label=Label(message_type_window,text="Body",font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=3,column=0,pady=5)
        message_Body_Text=Text(message_type_window,width=40,height=5,font="Helvetica 15 bold")
        message_Body_Text.grid(row=3,column=1,pady=5)
        Send_Button=Button(message_type_window,text='Send',command=sending_threader,font="Ethnocentric 15 bold")
        Send_Button.grid(row=4,column=2,pady=5)
        Add_Files_Button=Button(message_type_window,text='Add Files',command=Add_files_func,font="Ethnocentric 11 bold").grid(row=4,column=1,pady=5)


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
        first_email_window.geometry("700x150+483+234")
        first_email_window.config(background='#042438')
        first_email_window.resizable(False,True)
        first_email_username= Label(first_email_window,text="Enter Email",font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=0,column=0)
        first_email_entry= Entry(first_email_window, width=30,font=('Arial 20'))
        first_email_entry.grid(row=0,column=1)
        first_email_pass = Label(first_email_window, text="Enter Password",font="Ethnocentric 11 bold",bg="#042438",fg="white").grid(row=1,column=0)
        first_pass_entry = Entry(first_email_window, width=30,font=('Arial 20'))
        first_pass_entry.grid(row=1,column=1)
        first_login=Button(first_email_window,text='Login',command=lambda:Email_Login(first_email_entry.get(),first_pass_entry.get(),first_email_window),font=("Ethnocentric 11 bold"))
        first_login.grid(column=1,pady=10)

#"Wrong Email or Password! Login Failed"
    def Email_Login(decrypted_em_saved,decrypted_ps_saved,first_email_window):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(decrypted_em_saved,decrypted_ps_saved)
            print("Login success")
            ascii_email, ascii_pass=encript_data(decrypted_em_saved,decrypted_ps_saved)
            saved_emails=eval('{"%s":"%s"}'% (ascii_email,ascii_pass))
            with open("data.json",'r+') as e_object:
                new_em_upodate=eval(e_object.read())
                new_em_upodate.update(saved_emails)
                e_object.seek(0)
                e_object.write(json.dumps(new_em_upodate))
                e_object.close()
            first_email_window.destroy()
            type_message(decrypted_em_saved,server)
        except Exception as e:
            print(e)

    def choose_or_add_email(decrypted_em_saved,decrypted_ps_saved,saved_email_window):
        Email_Login(decrypted_em_saved,decrypted_ps_saved,saved_email_window)

    def Add_email_func(saved_email_window):
        saved_email_window.destroy()
        email_pass_entry()


    def saved_email_login():

        def confirm_em_remove(frame_index,button_index):
            pop_message=messagebox.askyesno("Confirm","Do you really want to remove account?")
            if pop_message==1:
                file_to_remove=open("data.json",'r')
                updated_file_to_remove=eval(file_to_remove.read())
                updated_file_to_remove.pop(button_index)
                file_to_remove.close()
                file_to_remove = open("data.json", 'w')
                file_to_remove.write(json.dumps(updated_file_to_remove))
                file_to_remove.close()
                frame_index.destroy()

        saved_email_window=Toplevel()
        saved_email_window.title("Select Email")
        saved_email_window.geometry("700x200+483+234")
        saved_email_window.config(background='#042438')
        saved_email_window.resizable(False,True)
        saved_em_file=eval(open('data.json','r').read())
        for em_saved,ps_saved in saved_em_file.items():
            decrypted_em_saved,decrypted_ps_saved=decrypt_data(em_saved,ps_saved)
            print(decrypted_em_saved,decrypted_ps_saved)
            frame=LabelFrame(saved_email_window,borderwidth=0,bg="#042438",pady=5)
            frame.pack()
            saved_em_button=Button(frame,text=decrypted_em_saved,command=lambda lam_saved_em=decrypted_em_saved,lam_saved_pass=decrypted_ps_saved:choose_or_add_email(lam_saved_em,lam_saved_pass,saved_email_window),font="Ethnocentric 11 bold",bg="#042438",fg="white",pady=6,border=6)
            saved_em_button.grid(row=0,column=0,pady=10)
            remove_saved_em_button = Button(frame, text="X",command=lambda frame_index=frame,button_index=em_saved:confirm_em_remove(frame_index,button_index),font="Ethnocentric 11 bold",bg="#042438",fg="white",pady=6,border=4)
            remove_saved_em_button.grid(row=0,column=2,padx=15,pady=10)
        add_new_email=Button(saved_email_window,text="Add New Email",command=lambda:Add_email_func(saved_email_window),font="Ethnocentric 11 bold",fg="black",border=5).pack(pady=10)


    if (os.stat('data.json').st_size == 0):
        email_pass_entry()
    else:
        saved_email_login()


send_email()
root.mainloop()
