from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()


tchr_add = Tk()
tchr_add.title('Adding a Teacher')
tchr_add.geometry('700x500')
tchr_add.call('wm', 'iconphoto', tchr_add._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr_add, image = render ).pack()

load1=Image.open('Images\\12.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr_add, image = render1, bg = '#EFEFEF').place(x=120, y=10)

def Home():
    tchr_add.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr_add, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

def submit():
    a= Ent1.get()
    b= Ent2.get()
    c= Ent3.get()
    d= Ent4.get()
    e= Ent5.get()
    f= Ent6.get()
    g= Ent7.get()
    h= Ent8.get()
    if a == '' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='':
        messagebox.showerror('warning', 'All fields are required')
    elif len(a)<=8 and len(b)<=20 and len(c)<=50 and len(d)<=50 and len(e)<=20 and len(f)<=100 and len(g)<=10 and len(h)<=100:
        var = (a, b, c, d, e, f, g, h)
        sql = 'Insert into tchr_profile value(%s,%s,%s,%s,%s,%s,%s,%s)'
        cu.execute(sql, var)
        db.commit()
        messagebox.showinfo('Submitted', 'Teacher has been successfully added')  
        tchr_add.destroy()
        call(['python','Teacher Permission.py'])
    elif len(a)>8:
        messagebox.showinfo('Invalid Input', 'The Teacher ID field is exceeding limit of 8!!!')
    elif len(b)>20:
        messagebox.showinfo('Invalid Input', 'The Password field is exceeding limit of 20!!!')

    elif len(c)>50:
        messagebox.showinfo('Invalid Input', 'The Teacher Name field is exceeding limit of 50!!!')

    elif len(d)>50:
        messagebox.showinfo('Invalid Input', 'The Class Teaching field is exceeding limit of 50!!!')

    elif len(e)>20:
        messagebox.showinfo('Invalid Input', 'The Qualification field is exceeding limit of 20!!!')

    elif len(f)>100:
        messagebox.showinfo('Invalid Input', 'The Subject Teaching is exceeding limit of 100!!!')

    elif len(g)>10:
        messagebox.showinfo('Invalid Input', 'The Phone Number field is exceeding limit of 10!!!')

    elif len(h)>100:
        messagebox.showinfo('Invalid Input', 'The Address field is exceeding limit of 100!!!')

Label2 = Label(tchr_add, text = "Teacher's Id", font = ('Forte', 20), fg = 'blue')
Label2.place(x=180, y=80)
Label3 = Label(tchr_add, text = "Password", font = ('Forte', 20), fg = 'blue')
Label3.place(x=180, y=120)
Label4 = Label(tchr_add, text = "Teacher's Name", font = ('Forte', 20), fg = 'blue')
Label4.place(x=180, y=160)
Label5 = Label(tchr_add, text = "Class Teaching", font = ('Forte', 20), fg = 'blue')
Label5.place(x=180, y=200)
Label6 = Label(tchr_add, text = "Qualification", font = ('Forte', 20), fg = 'blue')
Label6.place(x=180, y=240)
Label7 = Label(tchr_add, text = "Subject Teaching", font = ('Forte', 20), fg = 'blue')
Label7.place(x=180, y=280)
Label8 = Label(tchr_add, text = "Phone Number", font = ('Forte', 20), fg = 'blue')
Label8.place(x=180, y=320)
Label9 = Label(tchr_add, text = "Address", font = ('Forte', 20), fg = 'blue')
Label9.place(x=180, y=360)


Ent1 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent1.place(x=400, y=80)

Ent2 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent2.place(x=400, y=120)

Ent3 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent3.place(x=400, y=160)

Ent4 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent4.place(x=400, y=200)

Ent5 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent5.place(x=400, y=240)

Ent6 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent6.place(x=400, y=280)

Ent7 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent7.place(x=400, y=320)

Ent8 = Entry(tchr_add, font=('Elephant', 14), width = 20)
Ent8.place(x=400, y=360)

load2=Image.open('Images\\13.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(tchr_add, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = submit).place(x= 300, y=440)


def Back():
    tchr_add.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr_add, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=560, y=0)

tchr_add.mainloop()



