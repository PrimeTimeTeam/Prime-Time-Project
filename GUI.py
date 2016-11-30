# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
import tkMessageBox
import Tkinter as tk
from index import*
from Database import Database
import subprocess as sub

user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+ "
count = 0
def centerWindow():
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))                         #takes in variables for centering
    root.title("Prime Time")

def dbConfig():

    gui_db = Database(user, password, host, database)
    gui_db.connect()
    windowDB = tk.Toplevel(root)
    flushdbButton = Button(windowDB, text="flush database",command=gui_db.flush)

    secondButton = Button(windowDB, text=" Print database", command=printPrimes)
    flushdbButton.pack()
    secondButton.pack()

    windowDB.update_idletasks()



def primeCheck(event):
    
    gui_db = Database(user, password, host, database)
    gui_db.connect()
    
    if re.search('[a-zA-Z]', entry1.get()) or set(' [~!=@#$%^`&*()_+{}":;\']+$').intersection(entry1.get()):
        tkMessageBox.showwarning("INVALID ENTRY", "Please enter only digits")
        return
    if brain(int(entry1.get())):
        SBtime = gui_db.SBtimeReturn(entry1.get())
        FBtime = gui_db.FBtimeReturn(entry1.get())
        sbt = str(SBtime)
        fbt = str(FBtime)
        Pbutton.config(bg='Green')
        fbTime.config(text= "SBtime: " + sbt + " seconds")
        sbTime.config(text= "FBtime: " + fbt + " seconds")
        root.after(1000, lambda: Pbutton.config(bg='grey'))
        
    else:
        NPbutton.config(bg='Red')
        root.after(1000, lambda: NPbutton.config(bg='grey'))
        fbTime.config(text='0.0000000')
        sbTime.config(text='0.0000000')
def printPrimes():
    #]windowPrint = tk.Toplevel(root)
    lst = ['a', 'b', 'c', 'd']
    gui_db = Database(user, password, host, database)
    gui_db.connect()
    x=1

    t = Text(root)
    while gui_db.primeReturn(x):
        t.insert(END, str(gui_db.primeReturn(x)) + ", ")
        x=x+1
    t.pack()





#main portion of GUI
root = Tk()  # Creates object root that has properties for the window. Access via .instr
centerWindow()
# configuration portion

sbTime = Label(root, text="Slowbrain Time",font="Times 12")
fbTime = Label(root, text="Fastbrain Time", font="Times 12")
fbTime.grid(row=1, column =1)
sbTime.grid(row=1, column =0)
entry1 = Entry(root)
mesgLabel = Label(root, text="Enter Value to Check: ", font="Times 12")
Pbutton = Label(root, text="Prime", fg='Black', bg='grey', font="Times 20")
NPbutton = Label(root, text="Not-Prime", fg='black', bg='grey', font="Times 20")
loginWindow = Button(root, command=dbConfig, text= "Enter Admin Mode", fg='black', bg='grey')



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
