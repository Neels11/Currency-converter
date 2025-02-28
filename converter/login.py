from tkinter import *
from PIL import ImageTk

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if password.get()=='Password':
        password.delete(0,END)

#GUI
logn=Tk()
logn.geometry('730x500+50+50')
logn.resizable(0,0)
logn.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bluw.png')

bgLabel=Label(logn,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(logn,text='USER LOGIN', font=('Tahoma',23,'bold'),bg='white',fg='light sky blue')
heading.place(x=270, y=120)

usernameEntry=Entry(logn,width=25, font=('Tahoma',11,'bold'),bd=0,fg='light sky blue')
usernameEntry.place(x=270,y=190)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

Frame(logn, width=200,height=2,bg='light sky blue').place(x=270,y=208)

password=Entry(logn,width=25, font=('Tahoma',11,'bold'),bd=0,fg='light sky blue')
password.place(x=270,y=260)
password.insert(0,'Password')

password.bind('<FocusIn>',password_enter)

Frame(logn, width=200,height=2,bg='light sky blue').place(x=270,y=278)

button = Button(logn, text="Login", width=10, padx=5, height=1, bg='light sky blue', fg='white', font=('Tahoma'))
button.place(x=300, y=330)

button = Button(logn, text="Sig in", width=10, padx=5, height=1, bg='light sky blue', fg='white', font=('Tahoma'))
button.place(x=300, y=400)


logn.mainloop() 