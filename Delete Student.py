from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from stu_profile')
rec = cu.fetchall()
cu.execute('select * from stu_profile')
rec = cu.fetchall()

Adm_Nos = []
for i in rec:
    Adm_Nos.append(i[0])

def confirm():
    a = Ent1.get()
    if int(a) not in Adm_Nos:
        messagebox.showwarning('Invalid Input','No such Student Exists')
    else:
        var = (a,)
        sql = 'delete from stu_profile where Adm_No = %s'
        cu.execute(sql, var)
        db.commit()
        messagebox.showinfo('Deleted','Student has been deleted')
        tchr.destroy()
        call(['python','Teacher Permission.py'])

tchr = Tk()
tchr.title('Student Removal')
tchr.geometry('700x500')
tchr.call('wm', 'iconphoto',tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr, image = render).pack()
load1=Image.open('Images\\19.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr, image = render1).place(x=100, y=30)

def Home():
    tchr.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

Label2 = Label(tchr, text = 'Enter Adm No of the Student ', fg = 'red', font= ('Bernard MT Condensed', 30)).place(x=200, y= 150)
Label2 = Label(tchr, text = 'To be Deleted :', fg = 'red', font= ('Bernard MT Condensed', 30)).place(x=300, y= 200)

Ent1 = Entry(tchr, font = ('Helvitica', 25), width = 20)
Ent1.place(x=220, y=300)


def Back():
    tchr.destroy()
    call(['python','Teacher Permission.py'])

Btn2 = Button(tchr, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Btn2.place(x=560, y=0)

load2=Image.open('Images\\7.png')
render2 = ImageTk.PhotoImage(load2)
btn1= Button(tchr, image = render2, bg = '#919191' , bd = 0, highlightthickness = 0, command = confirm).place(x=290, y=440)
tchr.mainloop()
