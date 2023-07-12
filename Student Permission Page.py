from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()

stu_per = Tk()
stu_per.title('Student Permission Page')
stu_per.geometry('700x500')
stu_per.call('wm', 'iconphoto', stu_per._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(stu_per, image = render ).pack()
load1=Image.open('Images\\22.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(stu_per, image = render1, bg = '#EFEFEF').place(x=80, y=10)



def Home():
    stu_per.destroy()
    call(['python','Main Page.py'])

bttn = Button(stu_per, text = 'Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)


def next_page():
    a = var.get()
    stu_var = open('stu_var.txt', 'r')
    e = stu_var.readline()
    stu_var.close()
    if a == 1:
        stu_per.destroy()
        call(['python','student profile.py'])

    elif a == 2:
        stu_per.destroy()
        call(['python','Student Update.py'])

    else:
        messagebox.showinfo('Unselected', 'Something need to be selected')

var = IntVar()

stu_var = open('stu_var.txt', 'r')
e = stu_var.readline()
stu_var.close()

RB1 = Radiobutton(stu_per, text = 'View you Profile', font= ('Broad Way', 30), fg = 'red', variable = var, value = 1).place(x=250, y=100)
RB2 = Radiobutton(stu_per, text = 'Edit you profile', font= ('Broad Way', 30), fg = 'red', variable = var, value = 2).place(x=250, y= 250)
                
load2=Image.open('Images\\23.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(stu_per, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = next_page)
btn.place(x= 300, y=460 )

stu_per.mainloop()
