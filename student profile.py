from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from stu_profile')
rec = cu.fetchall()

stu_var = open('stu_var.txt', 'r')
d = stu_var.readline()
stu_var.close()



stu_view = Tk()
stu_view.title('Profile Page')
stu_view.geometry('700x500')
stu_view.call('wm', 'iconphoto', stu_view._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(stu_view, image = render).pack()
load1=Image.open('Images\\24.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(stu_view, image = render1).place(x=200, y=10)

def Back():
    stu_view.destroy()
    call(['python','Student Permission Page.py'])

btn = Button(stu_view, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
btn.place(x=560, y=0)

for i in rec:
    global a
    global b
    global e
    global f
    global g
    global h
    global k
    global j
    global l
    if i[6] == d:
        a = i[0]
        b = i[1]
        e = i[2]
        f = i[3]
        g = i[4]
        h = i[5]
        k = i[6]
        j = i[7]
        l = i[8]

        Label12 = Label(stu_view, text = a, font = ('Forte', 20), fg = 'red')
        Label12.place(x=400, y=80)
        Label13 = Label(stu_view, text = b, font = ('Forte', 20), fg = 'red')
        Label13.place(x=400, y=120)
        Label14 = Label(stu_view, text = e, font = ('Forte', 20), fg = 'red')
        Label14.place(x=400, y=160)
        Label15 = Label(stu_view, text = f, font = ('Forte', 20), fg = 'red')
        Label15.place(x=400, y=200)
        Label16 = Label(stu_view, text = g, font = ('Forte', 20), fg = 'red')
        Label16.place(x=400, y=240)
        Label17 = Label(stu_view, text = h, font = ('Forte', 20), fg = 'red')
        Label17.place(x=400, y=280)
        Label18 = Label(stu_view, text = k, font = ('Forte', 20), fg = 'red')
        Label18.place(x=400, y=320)
        Label19 = Label(stu_view, text = j, font = ('Forte', 20), fg = 'red')
        Label19.place(x=400, y=360)
        Label19 = Label(stu_view, text = l, font = ('Forte', 20), fg = 'red')
        Label19.place(x=400, y=400)



        
def Home():
    stu_view.destroy()
    call(['python','Main Page.py'])

bttn = Button(stu_view, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

Label2 = Label(stu_view, text = "Adm. No.", font = ('Forte', 20), fg = 'red')
Label2.place(x=180, y=80)
Label3 = Label(stu_view, text = "Student Name", font = ('Forte', 20), fg = 'red')
Label3.place(x=180, y=120)
Label4 = Label(stu_view, text = "Fathers's Name", font = ('Forte', 20), fg = 'red')
Label4.place(x=180, y=160)
Label5 = Label(stu_view, text = "Address", font = ('Forte', 20), fg = 'red')
Label5.place(x=180, y=200)
Label6 = Label(stu_view, text = "Email Id", font = ('Forte', 20), fg = 'red')
Label6.place(x=180, y=240)
Label7 = Label(stu_view, text = "Class", font = ('Forte', 20), fg = 'red')
Label7.place(x=180, y=280)
Label8 = Label(stu_view, text = "User Name", font = ('Forte', 20), fg = 'red')
Label8.place(x=180, y=320)
Label9 = Label(stu_view, text = "Password", font = ('Forte', 20), fg = 'red')
Label9.place(x=180, y=360)
Label10 = Label(stu_view, text = "Teacher Id", font = ('Forte', 20), fg = 'red')
Label10.place(x=180, y=400)




stu_view.mainloop()
