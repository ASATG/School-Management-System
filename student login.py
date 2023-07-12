from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from stu_profile')
rec = cu.fetchall()

stu = Tk()
stu.title('Student Login')
stu.geometry('700x500')
stu.call('wm', 'iconphoto', stu._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(stu, image = render).pack()
load1=Image.open('Images\\9.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(stu, image = render1).place(x=120, y=10)

def stu_per():
    a = Ent1.get()
    b = Ent2.get()
    for i in rec:
        if i[6] == a and i[7] == b:
            c = Ent1.get()
            stu_var = open('stu_var.txt','w')
            stu_var.write(c)
            stu_var.close()
            stu.destroy()
            stu_per = Tk()
            stu_per.title('Student Permission Page')
            stu_per.geometry('700x500')
            stu_per.call('wm', 'iconphoto', stu_per._w,PhotoImage(file='Images\\AV.png'))
            load=Image.open('Images\\89633.jpg')
            render = ImageTk.PhotoImage(load)
            img=Label(stu_per, image = render ).pack()

            def Home():
                stu_per.destroy()
                call(['python','Main Page.py'])

            bttn = Button(stu_per, text = 'Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
            bttn.place(x=0, y=0)

            def next_page():
                a = var.get()
                if a == 1:
                    stu_per.destroy()
                    call(['python','student profile.py'])

                elif a == 2:
                    stu_per.destroy()
                    call(['python','Student Update.py'])
                    
                    
            var = IntVar()

            load1=Image.open('Images\\22.png')
            render1 = ImageTk.PhotoImage(load1)
            Label1= Label(stu_per, image = render1, bg = '#EFEFEF').place(x=80, y=10)


            RB1 = Radiobutton(stu_per, text = 'View you Profile', font= ('Broad Way', 30), fg = 'red', variable = var, value = 1).place(x=250, y=100)
            RB2 = Radiobutton(stu_per, text = 'Edit you profile', font= ('Broad Way', 30), fg = 'red', variable = var, value = 2).place(x=250, y= 250)
                
                    
                    

            load2=Image.open('Images\\23.png')
            render2 = ImageTk.PhotoImage(load2)
            btn = Button(stu_per, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = next_page)
            btn.place(x= 300, y=460 )

            stu_per.mainloop()
        else:
            messagebox.showwarning('Invalid Input','Either the username or the password is incorrect!!!')




Label2 = Label(stu, text = 'Enter your ID: ', fg = 'Red', font= ('Bernard MT Condensed', 30)).place(x=200, y= 100)
Ent1 = Entry(stu, font = ('Helvitica', 25), width = 20)
Ent1.place(x=200, y=180)
Label3 = Label(stu, text = 'Enter your Password: ', fg = 'Red', font= ('Bernard MT Condensed', 30)).place(x=200, y= 260)
Ent2 = Entry(stu, font = ('Helvitica', 25), width = 20, bg = '#EFEFEF')
Ent2.place(x=200, y=340)
load2=Image.open('Images\\8.png')
render2 = ImageTk.PhotoImage(load2)
btn1= Button(stu, image = render2, bg = '#919191' , bd = 0, highlightthickness = 0, command = stu_per).place(x=290, y=440)
stu.mainloop()
