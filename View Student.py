from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from stu_profile')
rec =  cu.fetchall()

tchr_var = open('tchr_var.txt', 'r')
d = tchr_var.readline()
tchr_var.close()

tchr = Tk()
tchr.title('Your Students')
tchr.geometry('1200x500')
tchr.call('wm', 'iconphoto',tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
load2 = load.resize((1200,500), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load2)
img=Label(tchr, image = render).pack()
load1=Image.open('Images\\15.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(tchr, image = render1, bg = '#EEEEEE').place(x=400, y=10)

def Home():
    tchr.destroy()
    call(['python','Main Page.py'])

bttn = Button(tchr, text = 'Click to Home Page', command = Home, bd = 0, fg = 'blue',highlightthickness = 0)
bttn.place(x=0, y=0)

style = ttk.Style()
style.theme_use('default')
style.configure('Treeview', background = '#F1F1F1' ,foreground = 'Navy Blue', rowheight = 25, fieldbackround = '#F1F1F1')
style.map('Treeview', background = [('selected', 'yellow')])

table = ttk.Treeview(tchr)


table['columns']=('Adm_No', 'Student Name', 'Fathers Name', 'Address', 'Email Id', 'Class', 'User Name', 'Password', 'Teacher ID')


table.column('#0', width = 0, stretch = NO)
table.column('Adm_No', width = 60)
table.column('Student Name', width = 100)
table.column('Fathers Name', width = 120)
table.column('Address', width = 160)
table.column('Email Id', width = 160)
table.column('Class', width = 70)
table.column('User Name', width = 70)
table.column('Password', width = 70)
table.column('Teacher ID', width = 70)




table.heading('Adm_No', text = 'Adm_No')
table.heading('Student Name', text = 'Student Name')
table.heading('Fathers Name', text = 'Fathers Name')
table.heading('Address', text = 'Address')
table.heading('Email Id', text = 'Email Id')
table.heading('Class', text = 'Class')
table.heading('User Name', text = 'User Name')
table.heading('Password', text = 'Password')
table.heading('Teacher ID', text = 'Teacher ID')

def Back():
    tchr.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=1050, y=0)

count = 0
for i in rec:
    if i[8] == d:
        table.insert(parent = '', index = 'end', iid = count, text = '', values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        count+=1
        
table.place(x= 300, y=100)


tchr.mainloop()




