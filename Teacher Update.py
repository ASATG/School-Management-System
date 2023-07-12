from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from tchr_profile')
rec = cu.fetchall()

tchr = Tk()
tchr.title('Update Teacher')
tchr.geometry('700x500')
tchr.call('wm', 'iconphoto',tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr, image = render).pack()

tchr_var = open('tchr_var.txt', 'r')
e = tchr_var.readline()
tchr_var.close()

def Home():
    tchr.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

def submit():
    a= Ent1.get()
    b= Ent2.get()
    c= Ent3.get()
    d= Ent4.get()
    var= (a,b,c,d,e)
    sql = 'Update tchr_profile set Tchr_Name = %s, Password = %s, Phn_Number = %s, Address = %s where Teacher_Id=%s'
    cu.execute(sql, var)
    db.commit()
    messagebox.showinfo('Updated', 'Your Info has been successfully updated')
    tchr.destroy()
    call(['python','Teacher Permission.py'])


load1=Image.open('Images\\18.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr, image = render1).place(x=200, y=10)

Label2 = Label(tchr, text = "Teacher's Name", font = ('Forte', 20), fg = 'blue')
Label2.place(x=180, y=80)
Label3 = Label(tchr, text = "Password", font = ('Forte', 20), fg = 'blue')
Label3.place(x=180, y=160)
Label8 = Label(tchr, text = "Phone Number", font = ('Forte', 20), fg = 'blue')
Label8.place(x=180, y=240)
Label9 = Label(tchr, text = "Address", font = ('Forte', 20), fg = 'blue')
Label9.place(x=180, y=320)

Ent1 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent1.place(x=400, y=80)

Ent2 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent2.place(x=400, y=160)

Ent3 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent3.place(x=400, y=240)

Ent4 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent4.place(x=400, y=320)

load2=Image.open('Images\\13.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(tchr, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = submit).place(x= 300, y=440)

for i in rec:
    if i[0] == e:
        Ent1.insert(0,i[2])
        Ent2.insert(0,i[1])
        Ent3.insert(0,i[6])
        Ent4.insert(0,i[7])

        
def Back():
    tchr.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=560, y=0)


tchr.mainloop()
