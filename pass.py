from tkinter import *
import tkinter.messagebox as box

def dialog1():
    username=entry1.get()
    password = entry2.get()
    if (username == 'admin' and  password == 'secret'):
        box.showinfo('info','Correct Login')
    else:
        box.showinfo('info','Invalid Login')


window = Tk()
window.title('Countries Generation')

frame = Frame(window)

Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)




btn = Button(frame, text = 'Check Login',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()


pwdss=StringVar()
pwd=pwdss.get()



Label(f6, text="Name").pack(ipadx=500, ipady=500)
Label(f6, text="Coin Counter - View Data Login",width=20,font=("bold", 20)).place(x=90,y=53)
label_3 = Label(f6, text="Weight of Bag (g)",width=20,font=("bold", 10)).place(x=70,y=230)
entry_1 = Entry(f6,textvar=pwdss)
entry_1.place(x=240,y=230)
Button(f6, text='Home Page',width=20,bg='blue',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=440)

def passlol():
    pwd=pwdss.get()
    import hashlib
    hash_object = hashlib.md5(pwd.encode())
    if hash_object.hexdigest() == "5f4dcc3b5aa765d61d8327deb882cf99":
        print ('YAY')
    else:
        print('NO')

Button(f6, text='Exit',width=20,bg='red',fg='white',command=passlol).place(x=180,y=470)
