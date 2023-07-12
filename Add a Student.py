from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c 
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from stu_profile')
rec = cu.fetchall()

tchr = Tk()
tchr.title('Add a Student')
tchr.geometry('700x500')
tchr.call('wm', 'iconphoto', tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(tchr, image = render).pack()

Adm_Nos = []
for i in rec:
    Adm_Nos.append(i[0])

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
    e= Ent5.get()
    f= Ent6.get()
    g= Ent7.get()
    h= Ent8.get()
    i= Ent9.get()
    if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0 or len(e) == 0 or len(f) == 0 or len(g) == 0 or len(h) == 0 or len(i) == 0 :
        messagebox.showinfo('Incomplete Input', 'All the fields are required!!!')
    elif len(a)<=5 and len(b)<=50 and len(c)<=50 and len(d)<=100 and len(e)<=100 and len(f)<=3 and len(g)<=7 and len(h)<=20 and len(i)<=8 and int(a) not in Adm_Nos:
        var = (a, b, c, d, e, f, g, h, i)
        sql = 'Insert into stu_profile value(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cu.execute(sql, var)
        db.commit()
        messagebox.showinfo('Submitted', 'Student has been successfully added')
        tchr.destroy()
        call(['python','Teacher Permission.py'])
    elif int(a) in Adm_Nos:
        messagebox.showinfo('Existing Entry', 'The Adm_No already exists ')
    elif len(a)>5:
        messagebox.showinfo('Invalid Input', 'The Adm No field is exceeding limit of 5!!!')
 
    elif len(b)>50:
        messagebox.showinfo('Invalid Input', 'The Student Name field is exceeding limit of 50!!!')
 
    elif len(c)>50:
        messagebox.showinfo('Invalid Input', 'The Father Name field is exceeding limit of 50!!!')
 
    elif len(d)>100:
        messagebox.showinfo('Invalid Input', 'The Address field is exceeding limit of 100!!!')
 
    elif len(e)>100:
        messagebox.showinfo('Invalid Input', 'The Email ID field is exceeding limit of 100!!!')
 
    elif len(f)>3:
        messagebox.showinfo('Invalid Input', 'The Class field is exceeding limit of 3!!!')
        Ent1.delete()
    elif len(g)>7:
        messagebox.showinfo('Invalid Input', 'The User Name field is exceeding limit of 7!!!')

    elif len(h)>20:
        messagebox.showinfo('Invalid Input', 'The Password field is exceeding limit of 20!!!')

    elif len(a)>8:
        messagebox.showinfo('Invalid Input', 'The Teacher Id field is exceeding limit of 8!!!')


    
load1=Image.open('Images\\16.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr, image = render1).place(x=200, y=10)


Label2 = Label(tchr, text = "Adm No.", font = ('Forte', 20), fg = 'blue')
Label2.place(x=180, y=80)
Label3 = Label(tchr, text = "Name", font = ('Forte', 20), fg = 'blue')
Label3.place(x=180, y=120)
Label4 = Label(tchr, text = "Father's Name", font = ('Forte', 20), fg = 'blue')
Label4.place(x=180, y=160)
Label5 = Label(tchr, text = "Address", font = ('Forte', 20), fg = 'blue')
Label5.place(x=180, y=200)
Label6 = Label(tchr, text = "Email Id", font = ('Forte', 20), fg = 'blue')
Label6.place(x=180, y=240)
Label7 = Label(tchr, text = "Class", font = ('Forte', 20), fg = 'blue')
Label7.place(x=180, y=280)
Label8 = Label(tchr, text = "User Name", font = ('Forte', 20), fg = 'blue')
Label8.place(x=180, y=320)
Label9 = Label(tchr, text = "Password", font = ('Forte', 20), fg = 'blue')
Label9.place(x=180, y=360)
Label10 = Label(tchr, text = "Teacher_ID", font = ('Forte', 20), fg = 'blue')
Label10.place(x=180, y=400)

Ent1 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent1.place(x=400, y=80)

Ent2 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent2.place(x=400, y=120)

Ent3 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent3.place(x=400, y=160)

Ent4 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent4.place(x=400, y=200)

Ent5 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent5.place(x=400, y=240)

Ent6 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent6.place(x=400, y=280)

Ent7 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent7.place(x=400, y=320)

Ent8 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent8.place(x=400, y=360)

Ent9 = Entry(tchr, font=('Elephant', 14), width = 20)
Ent9.place(x=400, y=400)

load2=Image.open('Images\\13.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(tchr, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = submit).place(x= 300, y=460)

def Back():
    tchr.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=560, y=0)

tchr.mainloop()
