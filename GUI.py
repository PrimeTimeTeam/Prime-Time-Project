# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
import tkMessageBox
import Tkinter as tk
from index_GUI_test import*

symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+ "
count = 0
def centerWindow():
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))                         #takes in variables for centering
def dbConfig():
    #make new window, allow for flushing db
    windowDB = tk.Toplevel(root)
    flushdbButton = Button(windowDB, text="flush database")
    secondButton = Button(windowDB, text=" do something else") #add ,command = DB.flush()
    flushdbButton.pack()
    secondButton.pack()

def loginButton():
    windowLog = tk.Toplevel(root)
    usernameEntry = Entry(windowLog)
    usernameLabel = Label(windowLog, text= "Username:")
    passwordEntry = Entry(windowLog, show= "*")
    passwordLabel = Label(windowLog, text= "Password:")
    loginButton = Button(windowLog, text="Login")
    usernameEntry.grid(row=0, column=1)
    passwordEntry.grid(row=1, column=1)
    usernameLabel.grid(row=0, column=0)
    passwordLabel.grid(row=1, column=0)
    loginButton.grid(row=2, column=1)




def primeCheck(event):
    if re.search('[a-zA-Z]', entry1.get()) or set(' [~!=@#$%^`&*()_+{}":;\']+$').intersection(entry1.get()):
        tkMessageBox.showwarning("INVALID ENTRY", "Please enter only digits")
        return
    if brain(int(entry1.get())):
        Pbutton.config(bg='Green')
        root.after(1000, lambda: Pbutton.config(bg='grey'))

    else:
        NPbutton.config(bg='Red')
        root.after(1000, lambda: NPbutton.config(bg='grey'))


def sbTime():
     pass   # placeholder string


def fbTime():
    return "test"  # placeholder string



#main portion of GUI
root = Tk()  # Creates object root that has properties for the window. Access via .instr
centerWindow()
# configuration portion

SBtime = Label(root, text="Slowbrain Time",font="Times 12")
FBtime = Label(root, text="Fastbrain Time",font="Times 12")
FBtime.grid(row=1, column =1)
SBtime.grid(row=1, column =0)
entry1 = Entry(root)
mesgLabel = Label(root, text="Enter Value to Check: ", font="Times 12")
Pbutton = Label(root, text="Prime", fg='Black', bg='grey', font="Times 20")
NPbutton = Label(root, text="Not-Prime", fg='black', bg='grey', font="Times 20")
loginWindow = Button(root, command=loginButton, text= "Enter Admin Mode", fg='black', bg='grey')



#MUST SEPERATE CONFIG. this allows for 'plabel' and 'pbutton' to still point at the button object.
#adding <object>.grid results in an output of 'none' rather than *self . this causes problems when attempting
#to point to the variable.
#ex. plabel (points to obj) = Label() <objct>
#   plabel(DOESNOT POINT) = Label(____).grid() <- grid output is none, not Self
entry1.grid(row=2, column=1)

mesgLabel.grid(row=2,column=0)
Pbutton.grid(row=0,  column=0)
NPbutton.grid(row=0, column=1)
entry1.bind('<Return>', primeCheck)
loginWindow.grid(row=2, column=2)


root.mainloop()  # Execute the main event handler
