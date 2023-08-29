from tkinter import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import sqlite3
from PIL import Image

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

def frame():
    global button_frame, login_frame,signup_frame
    button_frame = ctk.CTkFrame(welcome2_frame,width=50,fg_color='white')
    button_frame.grid(row=5,column=0)

    signup_frame = ctk.CTkFrame(welcome2_frame,fg_color='white')
    # signup_frame.grid(row=6,column=0)

    login_frame = ctk.CTkFrame(welcome2_frame,fg_color='white')
    # login_frame.grid(row=6,column=0)

    login_btn = ctk.CTkButton(button_frame,text='LOGIN',width=150,fg_color='black',command=login_page)
    login_btn.grid(row=0,column=0,pady=(15,30),padx=20)

    signup_btn = ctk.CTkButton(button_frame,text='SIGNUP',width=150,fg_color='green',command=signup_page)
    signup_btn.grid(row=1,column=0,pady=(0,15),padx=20)

    

def signup_page():
    global first_nameEntry,lastnameEntry,UsernameEntry,emailaddress_Entry,phoneNumber_Entry,password_Entry,confirmPassword_Entry,gender_comboBox
    button_frame.grid_remove()
    login_frame.grid_remove()
    message_frame.grid_remove()
    signup_frame.grid(row=0,column=0)

    #Creating a signup page
    title_label = ctk.CTkLabel(signup_frame, text = "Register", font=('Cooper Black', 20, 'bold'), fg_color='green')
    title_label.grid(row=0,column=0,pady=25,ipadx=10,ipady=10)

    firstname_Label = ctk.CTkLabel(signup_frame, text="FIRST NAME")
    firstname_Label.grid(row=1,column=0)
    
    first_nameEntry = ctk.CTkEntry(signup_frame, placeholder_text = 'First Name', width=350)
    first_nameEntry.grid(row=2,column=0)

    lastname_Label = ctk.CTkLabel(signup_frame, text = "LAST NAME")
    lastname_Label.grid(row=3,column=0)
    
    lastnameEntry = ctk.CTkEntry(signup_frame, placeholder_text = "Last Name", width=350)
    lastnameEntry.grid(row=4,column=0)

    Username_Label = ctk.CTkLabel(signup_frame, text = "USERNAME")
    Username_Label.grid(row=5,column=0)
    
    UsernameEntry = ctk.CTkEntry(signup_frame, placeholder_text = "Username", width=350)
    UsernameEntry.grid(row=6,column=0)

    gender_label = ctk.CTkLabel(signup_frame, text = "GENDER")
    gender_label.grid(row=7, column=0)
    gender_var = ctk.StringVar(value="Male")
    gender_comboBox = ctk.CTkComboBox(signup_frame,values=["Male","Female","Transgender","I rather not say"], width=350,variable=gender_var)
    gender_comboBox.grid(row=8,column=0)

    emailaddress_Label = ctk.CTkLabel(signup_frame, text = "EMAIL ADDRESS")
    emailaddress_Label.grid(row=9,column=0)
    
    emailaddress_Entry = ctk.CTkEntry(signup_frame, placeholder_text="example@gmail.com", width=350)
    emailaddress_Entry.grid(row=10,column=0,padx=30)
    
    phoneNumber_Label = ctk.CTkLabel(signup_frame, text = "PHONE NUMBER")
    phoneNumber_Label.grid(row=11,column=0, padx=(15,10))
    phoneNumber_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Phone Number", width=350)
    phoneNumber_Entry.grid(row=12,column=0, padx=(15,10))

    password_label = ctk.CTkLabel(signup_frame, text = "PASSWORD")
    password_label.grid(row=13,column=0)
    password_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Password", width=350, show = '*')
    password_Entry.grid(row=14,column=0,padx=5)

    confirmPassword_Label = ctk.CTkLabel(signup_frame, text = "CONFIRM PASSWORD")
    confirmPassword_Label.grid(row=15,column=0,pady=(0,0))
    confirmPassword_Entry = ctk.CTkEntry(signup_frame, placeholder_text = "Confirm Password", width=350, show ='*')
    confirmPassword_Entry.grid(row=16,column=0,padx=30)

    check_btn = ctk.CTkCheckBox(signup_frame, text = "I agree to the Terms & Conditions of this App")
    check_btn.grid(row=17,column=0,pady=(20,0))

    signup = ctk.CTkButton(signup_frame, text='Sign Up', command=signup_info_msg, fg_color='black')
    signup.grid(row=18,column=0,padx=30,pady=15)

    title = ctk.CTkLabel(signup_frame, text='Already have an account?')
    title.grid(row=19,column=0,padx=(0,20),pady = (20,0))

    login_btn = ctk.CTkButton(signup_frame,text='Login',fg_color='grey',command=login_page)
    login_btn.grid(row=19, column=0, padx = (300,0), pady = (20,0))
#login section
def login_page():
    global usersnameEntry2,password_Entry2
    button_frame.grid_remove()
    signup_frame.grid_remove()
    message_frame.grid_remove()
    login_frame.grid(row=0,column=0, padx=0)

    login_title = ctk.CTkLabel(login_frame, text='Login Section', font=('Cooper Black',18),fg_color='green')
    login_title.grid(row=0, column=0, pady=(130,25),ipadx=10,ipady=10)
    
    usersname = ctk.CTkLabel(login_frame, text= 'Username')
    usersname.grid(row=1, column=0)
    usersnameEntry2 = ctk.CTkEntry(login_frame,placeholder_text='Username', width=250)
    usersnameEntry2.grid(row=2,column=0, padx=30, pady=(0,15))

    password_label = ctk.CTkLabel(login_frame, text = "PASSWORD")
    password_label.grid(row=3,column=0)
    password_Entry2 = ctk.CTkEntry(login_frame,placeholder_text='Password', width=250, show = '*')
    password_Entry2.grid(row=4,column=0,padx=30,pady=(0,15))

    chekbtn = ctk.CTkButton(password_Entry2,text='SHOW',width=50,fg_color='grey')
    chekbtn.grid(row=0,column=0,padx=(200,0))

    login = ctk.CTkButton(login_frame, text = 'LOGIN', fg_color='black', command=login_get_info)
    login.grid(row=5,column=0,padx=30, pady=(15))

    add = ctk.CTkLabel(login_frame, text="---------------------------- OR ----------------------------------")
    add.grid(row=6,column=0,padx=(0,2),pady = (5,20))

    title = ctk.CTkLabel(login_frame, text="Don't have an account yet?")
    title.grid(row=7,column=0,padx=(0,20),pady = (20,200))

    signup_btn = ctk.CTkButton(login_frame,text='Sign Up',fg_color='grey',width=100,command=signup_page)
    signup_btn.grid(row=7, column=0, padx = (300,0), pady = (20,200))

def signup_info_msg():
    first_name = first_nameEntry.get()
    last_name = lastnameEntry.get()
    user_name = UsernameEntry.get()
    gend = gender_comboBox.get()
    phoneNumber = phoneNumber_Entry.get()
    email_address = emailaddress_Entry.get()
    password = password_Entry.get()
    confirm_password = confirmPassword_Entry.get()
    if first_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your First Name")
    elif last_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your Last Name")
    elif user_name == '':
        CTkMessagebox(title='Signup Page ', message="Fill in your UserName")
    elif gend == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Gender")
    elif phoneNumber == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Phone Number")
    elif email_address == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Email Address")
    elif password == '':
        CTkMessagebox(title='Signup Page ', message="Fill in Your Password")
    elif confirm_password == '':
        CTkMessagebox(title='Signup Page ', message="Confirm Your Password")
    elif password != confirm_password:
        CTkMessagebox(title='Signup Page', message="Invalid Password.\nInput the correct password ")
    elif password == confirm_password:
        CTkMessagebox(title='Signup Page ', message="Correct Password")
        conn = sqlite3.connect('VotersDatabase.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS EntryTable
                (FirstName TEXT,LastName TEXT,Username TEXT,Gender TEXT,EmailAddress TEXT,Phone_Number INTEGER,Password TEXT)''')
        c.execute('''INSERT INTO EntryTable(FirstName,LastName,Username,Gender,EmailAddress,Phone_Number,Password)VALUES(?,?,?,?,?,?,?)
                ''',
                (first_name,last_name,user_name,gend,email_address,phoneNumber,password))
        conn.commit()     
        CTkMessagebox(title='Signup Page ', message="You have successfully signed in")

def login_get_info():
    email = usersnameEntry2.get()
    password = password_Entry2.get()

    con=sqlite3.connect('VotersDatabase.db')
    cur = con.cursor()
    statement = f"SELECT email from EntryTable WHERE Email='{email}' AND Password='{password}"
                 
if __name__ == "__main__":
    window = ctk.CTk()
    window.geometry('1400x800+0+0')
    window.title("VoteStream")
    window.iconbitmap("C:\\Users\\HP\\Downloads\\votelogs.ico")

    logo_frame = ctk.CTkFrame(window,bg_color='white',width=1200,height=600)
    logo_frame.grid()
    logo_frame.columnconfigure(0, weight=2)
    logo_frame.rowconfigure(0, weight=2)

    img = ctk.CTkImage(light_image=Image.open('coderslogo.png'),size=(920,600))
    lbl_img = ctk.CTkLabel(logo_frame,image=img,bg_color='white',text='')
    lbl_img.grid(row=0,column=0,ipadx=220,ipady=35,sticky='nw,sw,ne,se')

    logo_frame.after(6000, logo_frame.destroy)

    #welcome_frame = ctk.CTkFrame(window,bg_color='white',width=600,height=600)
    #welcome_frame.grid()

    bg = ctk.CTkImage(light_image=Image.open('coderslogo.png'),size=(900,700))
    lbl_bg = ctk.CTkLabel(window,image=bg,bg_color='white',text='')
    lbl_bg.grid(row=0,column=0)

    welcome2_frame = ctk.CTkFrame(window,fg_color='white',width=600,height=600)
    welcome2_frame.grid(row=0,column=1)

    message_frame = ctk.CTkFrame(welcome2_frame, fg_color='white',width=600,height=600)
    message_frame.grid(row=0, column=0)

    lbel = ctk.CTkLabel(message_frame,text='Good Day',font=('Cooper Black',25))
    lbel.grid(row=0,column=0,pady=(50,50))
    lbel = ctk.CTkLabel(message_frame,text='Our Esteemed Voters',font=('Cooper Black',25))
    lbel.grid(row=1,column=0,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Welcome to',font=('Cooper Black',25))
    labl.grid(row=2,column=0,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Your Number 1 Voting System',font=('Cooper Black',25))
    labl.grid(row=3,column=0,pady=(0,50))
    labl = ctk.CTkLabel(message_frame,text='Powered by the Exceptional coders',font=('Cooper Black',25))
    labl.grid(row=4,column=0,pady=(0,50),ipadx=10)

    frame()



    #welcome2_frame = ctk.CTkFrame(window,bg_color='white',width=1200,height=600)
    #welcome2_frame.grid()
    
    #anoda_frame = ctk.CTkFrame(welcome2_frame,width=50,height=50,fg_color='white')
    #anoda_frame.grid(row=0,column=1,padx=(0,0),pady=3)
    #lbel = ctk.CTkLabel(anoda_frame,text='Good Day\nOur Esteemed Voters\nWelcome to\nYour Number 1 Voting System\nPowered by the Exceptional coders  ',font=('Cooper Black',20))
    #lbel.grid(row=0,column=2,padx=20,pady=10)
    
   
    window.mainloop()








