from logging import root
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("GS SCREENSHOT ")
root["bg"] = "black"
root.geometry("500x500")
root.resizable(0,0)



def screenshot():
    name = int(round(time.time()*1000))
    name = 'image'+ '{}.png' .format(name)
    time.sleep(5)
    image = pyautogui.screenshot(name)
    
    root.deiconify()


screenshot()



def delay():
    root.withdraw()
    root.after(3000,screenshot())

btn1 = Button(root,text = "Take Screenshot",command = delay(),font=("Arial",15,"bold"),fg = "green",bg = "black",height = 4,width = 20 )
btn1.place(x=100,y=30)
root.mainloop()
btn2 = Button(root,text="QUIT HERE",command = quit() ,font=("Arial",15,"bold"),fg = "green",bg = "black",height = 4,width = 20 ).place(x=95,y=80)




#screen shot api by pyautogui 
#by Gourav sarkar