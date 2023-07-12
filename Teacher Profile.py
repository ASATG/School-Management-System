from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from tchr_profile')
rec = cu.fetchall()

tchr_var = open('tchr_var.txt', 'r')
d = tchr_var.readline()
tchr_var.close()



for i in rec:
    global a
    global b
    global e
    global f
    global g
    global h
    global k
    global j
    if i[0] == d:
        a = i[0]
        b = i[1]
        e = i[2]
        f = i[3]
        g = i[4]
        h = i[5]
        k = i[6]
        j = i[7]
        

tchr_view = Tk()
tchr_view.title('Profile Page')
tchr_view.geometry('700x500')
tchr_view.call('wm', 'iconphoto', tchr_view._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr_view, image = render).pack()
load1=Image.open('Images\\14.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr_view, image = render1).place(x=200, y=10)

def Home():
    tchr_view.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr_view, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

Label2 = Label(tchr_view, text = "Teacher's Id", font = ('Forte', 20), fg = 'blue')
Label2.place(x=180, y=80)
Label3 = Label(tchr_view, text = "Password", font = ('Forte', 20), fg = 'blue')
Label3.place(x=180, y=120)
Label4 = Label(tchr_view, text = "Teacher's Name", font = ('Forte', 20), fg = 'blue')
Label4.place(x=180, y=160)
Label5 = Label(tchr_view, text = "Class Teaching", font = ('Forte', 20), fg = 'blue')
Label5.place(x=180, y=200)
Label6 = Label(tchr_view, text = "Qualification", font = ('Forte', 20), fg = 'blue')
Label6.place(x=180, y=240)
Label7 = Label(tchr_view, text = "Subject Teaching", font = ('Forte', 20), fg = 'blue')
Label7.place(x=180, y=280)
Label8 = Label(tchr_view, text = "Phone Number", font = ('Forte', 20), fg = 'blue')
Label8.place(x=180, y=320)
Label9 = Label(tchr_view, text = "Address", font = ('Forte', 20), fg = 'blue')
Label9.place(x=180, y=360)

Label12 = Label(tchr_view, text = a, font = ('Forte', 20), fg = 'blue')
Label12.place(x=400, y=80)
Label13 = Label(tchr_view, text = b, font = ('Forte', 20), fg = 'blue')
Label13.place(x=400, y=120)
Label14 = Label(tchr_view, text = e, font = ('Forte', 20), fg = 'blue')
Label14.place(x=400, y=160)
Label15 = Label(tchr_view, text = f, font = ('Forte', 20), fg = 'blue')
Label15.place(x=400, y=200)
Label16 = Label(tchr_view, text = g, font = ('Forte', 20), fg = 'blue')
Label16.place(x=400, y=240)
Label17 = Label(tchr_view, text = h, font = ('Forte', 20), fg = 'blue')
Label17.place(x=400, y=280)
Label18 = Label(tchr_view, text = k, font = ('Forte', 20), fg = 'blue')
Label18.place(x=400, y=320)
Label19 = Label(tchr_view, text = j, font = ('Forte', 20), fg = 'blue')
Label19.place(x=400, y=360)

def Back():
    tchr_view.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr_view, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=560, y=0)

tchr_view.mainloop()
