# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
                        #might need be "tkinter"

class LoginWindow(Frame):
    def _init_(self,master):
        self._init_(self,master)
        self.title('Login Window')
        self.label1= Label(self, text= "Username")
        self.label2= Label(self, text= "Password")
        self.enter1 = Entry(self)
        self.enter2 = Entry(self, show= "*")            #this maskes password on entry 2
        #grid config row, col, stick

        self.label1.grid(row=0, sticky=W)
        self.label2.grid(row=1,sticky=W)
        self.enter1.grid(row=0,column=2)
        self.enter2.grid(row=1,column =2)



        self.pack()

def Pfunction():
    pass  # some code here hitting yes, pass just means no code is running here

    return


def Nfunction():
    pass  # just pass this function for now
    return

#------------
root = Tk()  # Creats object root that has properties for the window. Access via .instr
lw = LoginWindow(root)


# configuration portion
root.font = ('Verdana', '20', 'bold')   #changes the font for ALL text belonging to root
root.title('PrimeTime Software')
Ybutton = Button(root, text="Prime", command=Pfunction(), fg='blue',bg='green',cursor= 'arrow' ).pack()  # currently packed just to populate the message box
Nbutton = Button(root, text="Not-Prime", command=Nfunction(), fg='black', bg='red',cursor= 'arrow').pack()  # need to link to fun
timer1 = Label(root, text = "placeholder text, ref FB timer")
timer1.pack()
timer2 = Label(root, text = "placeholder text, ref SB timer")
timer2.pack()
number = Entry(root)
number.pack()
number.insert(0,'value for prime')

root.mainloop()
#above for functionallity

#root.mainloop()  # Execute the main event handler

#login class
