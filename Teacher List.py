from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as c
db = c.connect(host = 'localhost', user = 'root', passwd = 'Aayush@123', database = 'school_management_system')
cu = db.cursor()
cu.execute('select * from tchr_profile')
rec =  cu.fetchall()


tchr = Tk()
tchr.title('List of All teachers')
tchr.geometry('1200x500')
tchr.call('wm', 'iconphoto',tchr._w,PhotoImage(file='Images\\AV.png'))
load=Image.open('Images\\89633.jpg')
load2 = load.resize((1200,500), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load2)
img=Label(tchr, image = render).pack()
load1=Image.open('Images\\20.png')
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


table['columns']=('Teacher Id', 'Password', 'Teacher Name', 'Class Teaching', 'Qualification', 'Subject Teaching', 'Phone Number', 'Address')



table.column('#0', width = 0, stretch = NO)
table.column('Teacher Id', width = 60)
table.column('Password', width = 100)
table.column('Teacher Name', width = 120)
table.column('Class Teaching', width = 80)
table.column('Qualification', width = 80)
table.column('Subject Teaching', width = 100)
table.column('Phone Number', width = 120)
table.column('Address', width = 140)





table.heading('Teacher Id', text = 'Teacher Id')
table.heading('Password', text = 'Password')
table.heading('Teacher Name', text = 'Teacher Name')
table.heading('Class Teaching', text = 'Class Teaching')
table.heading('Qualification', text = 'Qualification')
table.heading('Subject Teaching', text = 'Subject Teaching')
table.heading('Phone Number', text = 'Phone Number')
table.heading('Address', text = 'Address')

def Back():
    tchr.destroy()
    call(['python','Teacher Permission.py'])

Button = Button(tchr, text = 'Click to Permission Page',command = Back, bd = 0,fg = 'blue' ,highlightthickness = 0)
Button.place(x=1050, y=0)

count = 0
for i in rec:
    table.insert(parent = '', index = 'end', iid = count, text = '', values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    count+=1


table.place(x= 300, y=100)

tchr.mainloop()
