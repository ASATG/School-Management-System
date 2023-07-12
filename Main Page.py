from tkinter import *
from PIL import Image,ImageTk
from subprocess import call

def tchr_login():
    root.destroy()
    call(['python','teacher login.py'])
    
def stu_login():
    root.destroy()
    call(['python','student login.py'])

root = Tk()
root.title('Login Page')
root.geometry('700x500')
root.resizable(False, False)
root.call('wm', 'iconphoto', root._w,PhotoImage(file='AV.png'))
load=Image.open('Images\\89633.jpg')
render = ImageTk.PhotoImage(load)
img=Label(root, image = render ).pack()
load1=Image.open('Images\\2.png')
render1 = ImageTk.PhotoImage(load1)
Label1= Label(root, image = render1, bg = '#EFEFEF').place(x=100, y=10)  
Label2= Label(root, text = 'If you are a Teacher', fg = 'Blue', font= ('Bernard MT Condensed', 40)).place(x=200, y= 100)
load2=Image.open('Images\\4.png')
render2 = ImageTk.PhotoImage(load2)
btn1= Button(root, image = render2, bg = '#EFEFEF' , bd = 0, highlightthickness = 0, command = tchr_login)
btn1.place(x=330, y=190)
Label3= Label(root, text = 'If you are a Student', fg = 'Red', font= ('Bernard MT Condensed', 40)).place(x=200, y= 250)
load3=Image.open('Images\\6.png')
render3 = ImageTk.PhotoImage(load3)
btn2= Button(root, image = render3, bg = '#EFEFEF' , bd = 0, highlightthickness = 0, command = stu_login).place(x=330, y=340)
root.mainloop()
