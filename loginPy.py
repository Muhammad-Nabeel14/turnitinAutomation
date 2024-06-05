from tkinter import *
import time
from tkinter import filedialog

def login():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="kapil" and pwd=="123":
       message.set("Login success")
       time.sleep(2)
       login_screen.destroy()
       FileUpload()
      else:
       message.set("Wrong username or password!!!")


def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x250")

    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()

    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

    Label(login_screen, text="Username * ").place(x=20,y=40)

    Entry(login_screen, textvariable=username).place(x=90,y=42)

    Label(login_screen, text="Password * ").place(x=20,y=80)

    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)

    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()

def FileUpload():
    fileUpload = Tk()
    fileUpload.geometry("400x300")  # Size of the window 
    fileUpload.title('www.plus2net.com')
    my_font1=('times', 18, 'bold')
    l1 = Label(fileUpload,text='Upload File & read',width=30,font=my_font1,bg="orange")  
    l1.grid(row=1,column=1)
    b1 = Button(fileUpload, text='Upload File', 
    width=20,command = lambda:upload_file())
    b1.grid(row=2,column=1) 

    def upload_file():
        file = filedialog.askopenfilename()
        fob=open(file,'r')
        print(fob.read())
        #file = filedialog.askopenfile()
        #print(file.read())
    fileUpload.mainloop()  # Keep the window open



if __name__=="__main__":
    Loginform()