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
tchr.title('Teacher Login')
tchr.geometry('700x500')
tchr.call('wm', 'iconphoto',tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr, image = render).pack()

def Home():
    tchr.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

usernames = []
for i in rec:
    usernames.append(i[0])

passwords = []
for i in rec:
    passwords.append(i[1])
    

def tchr_per():
    a = Ent1.get()
    b = Ent2.get()
    for i in rec:
        if i[0] == a and i[1] == b:
            c = Ent1.get()
            tchr.destroy()
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
                   messagebox.showinfo('Invalid Selection', 'Something needs to be selected') 
                    
                    
            var = IntVar()

            load1=Image.open('Images\\10.png')
            render1 = ImageTk.PhotoImage(load1)
            Label1= Label(tchr_per, image = render1, bg = '#EFEFEF').place(x=100, y=10)


            if c == 'ASA_0000' or c == 'Vin_0001':
                RB1 = Radiobutton(tchr_per, text = 'View you Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 1).place(x=250, y=80)
                RB2 = Radiobutton(tchr_per, text = 'View your Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 2).place(x=250, y= 120)
                RB3 = Radiobutton(tchr_per, text = 'Edit Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 3).place(x=250, y= 160)
                RB4 = Radiobutton(tchr_per, text = 'Edit you profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 4).place(x=250, y= 200)
                RB5 = Radiobutton(tchr_per, text = 'Add a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 5).place(x=250, y= 240)
                RB6 = Radiobutton(tchr_per, text = 'Remove a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 6).place(x=250, y= 280)
                RB7 = Radiobutton(tchr_per, text = 'Add a Teacher', font= ('Broad Way', 20), fg = 'green', variable = var, value = 7).place(x=250, y= 320)
                RB8 = Radiobutton(tchr_per, text = 'View all Teacher', font= ('Broad Way', 20), fg = 'green', variable = var, value = 8).place(x=250, y= 360)
                RB9 = Radiobutton(tchr_per, text = 'View all Students', font= ('Broad Way', 20), fg = 'green', variable = var, value = 9).place(x=250, y= 400)
            else:
                RB1 = Radiobutton(tchr_per, text = 'View you Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 1).place(x=250, y=90)
                RB2 = Radiobutton(tchr_per, text = 'View your Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 2).place(x=250, y= 150)
                RB3 = Radiobutton(tchr_per, text = 'Edit Student Profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 3).place(x=250, y= 210)
                RB4 = Radiobutton(tchr_per, text = 'Edit you profile', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 4).place(x=250, y= 270)
                RB5 = Radiobutton(tchr_per, text = 'Add a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 5).place(x=250, y= 330)
                RB6 = Radiobutton(tchr_per, text = 'Remove a student', font= ('Broad Way', 20), fg = 'blue', variable = var, value = 6).place(x=250, y= 390)
                    
                    
                    

            load2=Image.open('Images\\11.png')
            render2 = ImageTk.PhotoImage(load2)
            btn = Button(tchr_per, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = next_page)
            btn.place(x= 300, y=460 )

            tchr_per.mainloop()

        elif a == '' or b == '':
            messagebox.showwarning('Empty Field', 'All fields are required')

        elif a not in usernames or b not in passwords:
            messagebox.showwarning('Invalid Input', 'Something didn\'t match')




load1=Image.open('Images\\5.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr, image = render1).place(x=120, y=10)
Label2 = Label(tchr, text = 'Enter your ID: ', fg = 'Blue', font= ('Bernard MT Condensed', 30)).place(x=200, y= 100)
Ent1 = Entry(tchr, font = ('Helvitica', 25), width = 20)
Ent1.place(x=200, y=180)
Label3 = Label(tchr, text = 'Enter your Password: ', fg = 'Blue', font= ('Bernard MT Condensed', 30)).place(x=200, y= 260)
Ent2 = Entry(tchr, font = ('Helvitica', 25), width = 20)
Ent2.place(x=200, y=340)
load2=Image.open('Images\\7.png')
render2 = ImageTk.PhotoImage(load2)
btn1= Button(tchr, image = render2, bg = '#919191' , bd = 0, highlightthickness = 0, command = tchr_per).place(x=290, y=440)
tchr.mainloop()
