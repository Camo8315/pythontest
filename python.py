from tkinter import *
from tkinter import messagebox
import re
import os.path
from tkinter import ttk


def clear():
    entry_1.delete('0', END)
    Coinvalue.set('Select Coin Value') 
    Name.set('Select Name')

def submit():
    datavalid = True # Boolean Trigger assumes all data is true
    coindatavalid = True
    name1=Name.get()
    weight= Weight.get ()
    coinvalue=Coinvalue.get()

    if not re.match (r'^[0-9\.]*$', str(weight)):
        messagebox.showerror("Error", "Weight Feild Must Contain Only Numbers Or Decimal Palces")
        datavalid = False

    if (len(weight)<1): #tests for length of the name
        messagebox.showerror("Error", "Weight Feild Cant Be Empty")
        datavalid = False

    if name1 == "Select Name":
        messagebox.showerror("Error", "Name Feild Cant Be Empty")
        datavalid = False

    if coinvalue == "Select Coin Value":
        messagebox.showerror("Error", "Coin Value Feild Cant Be Empty")
        datavalid = False


    if datavalid == True:
        messagebox.showinfo("Info", "Saving...")
        save()

        

def save():
    name1=Name.get()
    weight=Weight.get()
    coinvalue=Coinvalue.get()
    coindatavalid = True
    if coinvalue == "£2":
        twopoundcoinvalidate = (120 - int(weight))/12
        if twopoundcoinvalidate > 0:
            messagebox.showerror("Error", "Too Few Coins In Bag Add " + str(twopoundcoinvalidate) + " Coin(s)")
            coindatavalid = False
        if twopoundcoinvalidate < 0:
            messagebox.showerror("Error", "Too Many Coins In Bag Remove " + str(twopoundcoinvalidate) + " Coin(s)")
            coindatavalid = False


    if coindatavalid == True:
        coindatavalidyn=("Yes")
    else:
        coindatavalidyn=("No")

    f = open(('CoinCount.txt'), 'a')
    f.write(name1 + ',' + weight + ',' + coinvalue + ',' + coindatavalidyn + '\n')
    f.close()
    messagebox.showinfo("Info", "Saved")
    clear()
    return

def raise_frame(frame):
    frame.tkraise()

################################################################################################################################
    
root = Tk()

root.geometry('500x500')
root.title("Coin Counter")
windowWidth = 500
windowHeight = 500

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
     
root.geometry("+{}+{}".format(positionRight, positionDown))

root.resizable(False, False)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

for frame in (f1, f2, f3, f4,f5):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text="Name").pack(ipadx=500, ipady=500)
Label(f1, text="Coin Counter - Home",width=20,font=("bold", 20)).place(x=90,y=53)
Button(f1, text='Data Entery',width=20,bg='darkcyan',fg='white',command=lambda:raise_frame(f2)).place(x=180,y=200)
Button(f1, text='View Data',width=20,bg='darkcyan',fg='white',command=lambda:raise_frame(f3)).place(x=180,y=230)
Button(f1, text='Exit',width=20,bg='red',fg='white',command=root.destroy).place(x=180,y=470)

Name=StringVar()
Weight=StringVar()
Coinvalue=StringVar()

name1=Name.get()
weight=Weight.get()
coinvalue=Coinvalue.get()   

Label(f2, text="Name").pack(ipadx=500, ipady=500)           
Label(f2, text="Coin Counter - Entery",width=20,font=("bold", 20)).place(x=90,y=53)

Label(f2, text="Name",width=20,font=("bold", 10)).place(x=70, y=130)
list1 = ['Abena','Malcom','Jane','Andy','Sandip','Liz'];
droplist=OptionMenu(f2,Name, *list1)
droplist.config(width=15)
Name.set('Select Name') 
droplist.place(x=240,y=130)

label_2 = Label(f2, text="Coin Value",width=20,font=("bold", 10)).place(x=70,y=180)
list2 = ['£2','£1','50p','20p','10p','5p','2p','1p'];
droplist1=OptionMenu(f2,Coinvalue, *list2)
droplist1.config(width=15)
Coinvalue.set('Select Coin Value') 
droplist1.place(x=240,y= 180)

label_3 = Label(f2, text="Weight of Bag (g)",width=20,font=("bold", 10)).place(x=70,y=230)
entry_1 = Entry(f2,textvar=Weight)
entry_1.place(x=240,y=230)


Button(f2, text='Submit',width=20,bg='green',fg='white',command=submit).place(x=180,y=350)
Button(f2, text='Clear',width=20,bg='gray',fg='white',command=clear).place(x=180,y=380)
Button(f2, text='Home Page',width=20,bg='blue',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=440)
Button(f2, text='Exit',width=20,bg='red',fg='white',command=root.destroy).place(x=180,y=470)
#----------------------------------------
Label(f3, text="Name").pack(ipadx=500, ipady=500)
Label(f3, text="Coin Counter - View Data",width=20,font=("bold", 20)).place(x=90,y=53)
Button(f3, text='Bags Cheaked And Value',width=20,bg='darkcyan',fg='white',command=lambda:raise_frame(f5)).place(x=180,y=200)
Button(f3, text='Accuraccy Monitor',width=20,bg='darkcyan',fg='white',command=lambda:raise_frame(f4)).place(x=180,y=230)
Button(f3, text='Home Page',width=20,bg='blue',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=440)
Button(f3, text='Exit',width=20,bg='red',fg='white',command=root.destroy).place(x=180,y=470)


with open("CoinCount.txt") as f:
    contents = f.read()
    abenabagscheaked = contents.count("Abena")

with open ("CoinCount.txt", "r") as inputFile:
    data = inputFile.read()
abenapattern = re.compile(r'^(?=.*\bAbena\b)(?=.*\bYes\b).*$', flags=re.MULTILINE)
abenalines = re.findall(abenapattern, data)


if abenabagscheaked == 0:
    abenapercentagecorrect= 'N/A'
else:
    abenapercentagecorrect= int(len(abenalines))/int(abenabagscheaked)*100




Label(f4, text="Name").pack(ipadx=500, ipady=500)
label_2=Label(f4, text="Coin Counter - Accurecy Monitor",width=25,font=("bold", 20)).place(x=50,y=53)
Label(f4, text="Volunteer Name",width=12,font=("bold", 10)).place(x=10,y=95)
Label(f4, text="Total Enteries",width=10,font=("bold", 10)).place(x=145,y=95)
Label(f4, text="Total Correct",width=10,font=("bold", 10)).place(x=255,y=95)
Label(f4, text="Percentage Correct",width=15,font=("bold", 10)).place(x=360,y=95)
Label(f4, text="Abena",width=12,font=("bold", 10)).place(x=10,y=130)
Label(f4, text=str(abenabagscheaked),width=12,font=("bold", 10)).place(x=130,y=130)
Label(f4, text=str(len(abenalines)),width=12,font=("bold", 10)).place(x=240,y=130)
Label(f4, text=str(abenapercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=130)
Label(f4, text="Malcom",width=12,font=("bold", 10)).place(x=10,y=160)
Label(f4, text=str(malcombagscheaked),width=12,font=("bold", 10)).place(x=130,y=160)
Label(f4, text=str(len(malcomlines)),width=12,font=("bold", 10)).place(x=240,y=160)
Label(f4, text=str(malcompercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=160)
Label(f4, text="Jane",width=12,font=("bold", 10)).place(x=10,y=190)
Label(f4, text=str(janebagscheaked),width=12,font=("bold", 10)).place(x=130,y=190)
Label(f4, text=str(len(janelines)),width=12,font=("bold", 10)).place(x=240,y=190)
Label(f4, text=str(janepercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=190)
Label(f4, text="Andy",width=12,font=("bold", 10)).place(x=10,y=220)
Label(f4, text=str(andybagscheaked),width=12,font=("bold", 10)).place(x=130,y=220)
Label(f4, text=str(len(andylines)),width=12,font=("bold", 10)).place(x=240,y=220)
Label(f4, text=str(andypercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=220)
Label(f4, text="Sandip",width=12,font=("bold", 10)).place(x=10,y=250)
Label(f4, text=str(sandipbagscheaked),width=12,font=("bold", 10)).place(x=130,y=250)
Label(f4, text=str(len(sandiplines)),width=12,font=("bold", 10)).place(x=240,y=250)
Label(f4, text=str(sandippercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=250)
Label(f4, text="Liz",width=12,font=("bold", 10)).place(x=10,y=280)
Label(f4, text=str(lizbagscheaked),width=12,font=("bold", 10)).place(x=130,y=280)
Label(f4, text=str(len(lizlines)),width=12,font=("bold", 10)).place(x=240,y=280)
Label(f4, text=str(lizpercentagecorrect),width=12,font=("bold", 10)).place(x=350,y=280)
ttk.Separator(f4, orient=VERTICAL).place(x=130 ,y=100, height=300)
ttk.Separator(f4, orient=VERTICAL).place(x=240 ,y=100, height=300)
ttk.Separator(f4, orient=VERTICAL).place(x=350 ,y=100, height=300)
ttk.Separator(f4, orient=HORIZONTAL).place(x=25 ,y=120, width=450)
Button(f4, text='Reload Data',width=20,bg='SeaGreen3',fg='white', command=reload(root)).place(x=180,y=410)
Button(f4, text='Home Page',width=20,bg='blue',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=440)
Button(f4, text='Back',width=20,bg='light sea green',fg='white',command=lambda:raise_frame(f3)).place(x=20,y=470)
Button(f4, text='Exit',width=20,bg='red',fg='white',command=root.destroy).place(x=180,y=470)

with open("CoinCount.txt") as f:
    contents = f.read()
    bagscheaked = contents.count("Yes")

label_2=Label(f5, text="Coin Counter - Bags and Value",width=25,font=("bold", 20)).place(x=50,y=53)
Label(f5, text="Bags Cheaked: " + str(bagscheaked),width=20,font=("bold", 10)).place(x=170,y=150)
Label(f5, text="Total Value",width=20,font=("bold", 10)).place(x=170,y=180)
Button(f5, text='Reload Data',width=20,bg='SeaGreen3',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=410)
Button(f5, text='Home Page',width=20,bg='blue',fg='white', command=lambda:raise_frame(f1)).place(x=180,y=440)   
Button(f5, text='Back',width=20,bg='light sea green',fg='white',command=lambda:raise_frame(f3)).place(x=20,y=470)
Button(f5, text='Exit',width=20,bg='red',fg='white',command=root.destroy).place(x=180,y=470)

raise_frame(f1)
root.mainloop()




