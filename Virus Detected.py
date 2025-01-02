#import nessecary librarites
from tkinter import *
from tkinter import messagebox

#setup the window
root=Tk()
root.geometry("200x200")

#fuction for display warning massages
#this will be called once the button clicked
#massagebox.showarning ("window Name",Text will be displayed)
def msg():
    messagebox.showwarning("Alert","Stop! Virus found.")

#adding button  widget to window
button=Button(root,text="Scan for Virus",command=msg)
button.place(x=40,y=80)


root.mainloop()


