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
stu.title('Student Edit')
stu.geometry('700x500')
stu.call('wm', 'iconphoto',stu._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(stu, image = render).pack()

stu_var = open('stu_var.txt', 'r')
e = stu_var.readline()
stu_var.close()

def Home():
    stu.destroy()
    call(['python','Main Page.py'])

bttn = Button(stu, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

def submit():
    a= Ent1.get()
    b= Ent2.get()
    c= Ent3.get()
    if a == '' or b=='' or c=='':
        messagebox.showerror('warning', 'All fields are required')

    elif len(a)>100:
        messagebox.showinfo('Invalid Input', 'The Email Id field is exceeding limit of 5!!!')
    elif len(b)>20:
        messagebox.showinfo('Invalid Input', 'The Password field is exceeding limit of 50!!!')

    elif len(c)>100:
        messagebox.showinfo('Invalid Input', 'The Address field is exceeding limit of 50!!!')

    else:
        var= (a,b,c,e)
        sql = 'Update stu_profile set Email_Id = %s, Password = %s, Address = %s where User_Name=%s'
        cu.execute(sql, var)
        db.commit()
        messagebox.showinfo('Updated', 'Your Info has been successfully updated')

            
load1=Image.open('Images\\25.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(stu, image = render1).place(x=200, y=10)

Label2 = Label(stu, text = "Email Id", font = ('Forte', 25), fg = 'blue')
Label2.place(x=180, y=100)
Label3 = Label(stu, text = "Password", font = ('Forte', 25), fg = 'blue')
Label3.place(x=180, y=200)
Label8 = Label(stu, text = "Address", font = ('Forte', 20), fg = 'blue')
Label8.place(x=180, y=300)


Ent1 = Entry(stu, font=('Elephant', 18), width = 17)
Ent1.place(x=350, y=100)

Ent2 = Entry(stu, font=('Elephant', 18), width = 17)
Ent2.place(x=350, y=200)

Ent3 = Entry(stu, font=('Elephant', 18), width = 17)
Ent3.place(x=350, y=300)

for i in rec:
    if i[6] == e:
        Ent1.insert(0, i[4])
        Ent2.insert(0, i[7])
        Ent3.insert(0, i[3])

def Back():
    stu.destroy()
    call(['python','Student Permission Page.py'])

btn = Button(stu, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
btn.place(x=560, y=0)

load2=Image.open('Images\\26.png')
render2 = ImageTk.PhotoImage(load2)
btn = Button(stu, image = render2,bd = 0, highlightthickness = 0, bg = '#8A8C8B', command = submit).place(x= 400, y=460)
load3=Image.open('Images\\4.png')

stu.mainloop()






    
