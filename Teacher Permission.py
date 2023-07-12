from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c

tchr_per = Tk()
tchr_per.title('Teacher Permission Page')
tchr_per.geometry('700x500')
tchr_per.call('wm', 'iconphoto', tchr_per._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr_per, image = render ).pack()

def Home():
    tchr_per.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr_per, text = 'Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

def next_page():
    a = var.get()
    tchr_var = open('tchr_var.txt','w')
    tchr_var.write(c)
    tchr_var.close()
    if a == 7:
        tchr_per.destroy()
        call(['python','Add a Teacher.py'])

    elif a == 1:
        tchr_per.destroy()
        call(['python','Teacher Profile.py'])

    elif a == 2:
        tchr_per.destroy()
        call(['python','View Student.py'])

    elif a == 3:
        tchr_per.destroy()
        call(['python','Student Edit.py'])

    elif a == 4:
        tchr_per.destroy()
        call(['python','Teacher Update.py'])


    elif a == 5:
        tchr_per.destroy()
        call(['python','Add a Student.py'])


    elif a == 6:
        tchr_per.destroy()
        call(['python','Delete Student.py'])


    elif a == 8:
        tchr_per.destroy()
        call(['python','Teacher List.py'])

    elif a == 9:
        tchr_per.destroy()
        call(['python','All Students.py'])

    else:
        messagebox.showinfo('Unselected', 'Something needs to be selected!!!')
    
        
        
var = IntVar()

load1=Image.open('Images\\10.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr_per, image = render1, bg = '#EFEFEF').place(x=100, y=10)

tchr_var = open('tchr_var.txt', 'r')
c = tchr_var.readline()
tchr_var.close() 

if c == 'ASA_0000' or c == 'Vin_0001':
    RB1 = Radiobutton(tchr_per, text = 'View your Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 1).place(x=250, y=80)
    RB2 = Radiobutton(tchr_per, text = 'View your Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 2).place(x=250, y= 120)
    RB3 = Radiobutton(tchr_per, text = 'Edit Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 3).place(x=250, y= 160)
    RB4 = Radiobutton(tchr_per, text = 'Edit your profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 4).place(x=250, y= 200)
    RB5 = Radiobutton(tchr_per, text = 'Add a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 5).place(x=250, y= 240)
    RB6 = Radiobutton(tchr_per, text = 'Remove a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 6).place(x=250, y= 280)
    RB7 = Radiobutton(tchr_per, text = 'Add a Teacher', font= ('Broad Way', 20), fg = 'green', variable = var, value = 7).place(x=250, y= 320)
    RB8 = Radiobutton(tchr_per, text = 'View all Teacher', font= ('Broad Way', 20), fg = 'green', variable = var, value = 8).place(x=250, y= 360)
    RB9 = Radiobutton(tchr_per, text = 'View all Students', font= ('Broad Way', 20), fg = 'green', variable = var, value = 9).place(x=250, y= 400)
else:
    RB1 = Radiobutton(tchr_per, text = 'View you Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 1).place(x=250, y=90)
    RB2 = Radiobutton(tchr_per, text = 'View your Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 2).place(x=250, y= 150)
    RB3 = Radiobutton(tchr_per, text = 'Edit Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 3).place(x=250, y= 210)
    RB4 = Radiobutton(tchr_per, text = 'Edit your profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 4).place(x=250, y= 270)
    RB5 = Radiobutton(tchr_per, text = 'Add a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 5).place(x=250, y= 330)
    RB6 = Radiobutton(tchr_per, text = 'Remove a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 6).place(x=250, y= 390)
        
        
        

load2=Image.open('Images\\11.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(tchr_per, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = next_page)
btn.place(x= 300, y=460 )

tchr_per.mainloop()
