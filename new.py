from tkinter import*
from tkinter import messagebox
import pyspeedtest


def speed():
    gs = pyspeedtest.SpeedTest("www.google.com")
    a = (str(gs.download()) + " BYTES per Seconds")
    messagebox.showinfo("your downloading speed",a)

def uploadtest():
    sg = pyspeedtest.SpeedTest("www.google.com")
    b = (str(sg.upload()) + " BYTES per Seconds ")
    messagebox.showinfo("your uploading speed",b)

root =Tk()
root.title(" Check your Internet speed ")
root.geometry("650x750")
root['bg']= "green"


filename=PhotoImage(file="net-speed-1.png")
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

btn1=Button(root,text='Check the download speed',font=('San serif',20),bg='Yellow',height=1,width=30,command=speed)
btn1.place(x=105,y=90)

btn2=Button(root,text='Check the upload speed',font=('San serif',20),bg='Yellow',height=1,width=30,command=uploadtest)
btn2.place(x=105,y=170)

root.mainloop()



