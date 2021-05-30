#imports
from tkinter import *

#createTheWindow
window = Tk()
#windowSize
window.geometry('480x360')

#titleLabel
window.title("Breadstix Tracker Python Additon")
lbl = Label(window, text="BreadStix Tracker", font=('Arial Bold', 18))
lbl.grid(column=0, row=0)

#nameField
nameLbl = Label(window, text="Please Enter Your Name", font=('Arial Bold', 12))
nameLbl.grid(column=0, row=2)
#input
userName = Entry(window, width=10)
userName.grid(column=1, row=2)
#action
def clicked():    
    res = "Welcome " + userName.get()
    nameLbl.configure(text= res)
    userName.grid_remove()



#buttons
btn = Button(window, text= "Enter", bg="lightGreen", command=clicked)
btn.grid(column=0,row=3)
btn = Button(window, text= "Cancel", bg="red")
btn.grid(column=1,row=3)

#buttonAction

#CloseWindow
window.mainloop()