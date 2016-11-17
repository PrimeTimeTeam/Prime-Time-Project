# Project Name: Prime-Time-Project
# File: GUI.py
# NOTE: this is our graphical user interface
#import index
from Tkinter import *  # Importing the Tkinter (tool box) library
                        #might need be "tkinter"
def Pfunction():
    pass  # some code here hitting yes, pass just means no code is running here

    return


def Nfunction():
    pass  # just pass this function for now
    return

#------------
root = Tk()  # Creats object root that has properties for the window. Access via .instr

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

#above for functionallity

root.mainloop()  # Execute the main event handler




