#imports
from tkinter import *

#createTheWindow
window = Tk()
#windowSize
window.geometry('480x360')

#titleLabel
window.title("Breadstix Tracker Python Additon")
lbl = Label(window, text="BreadStix", font=('Arial Bold', 24))
lbl.grid(column=0, row=0)

#inputFields
txt = Entry(window, width=10)
txt.grid(column=1, row=1)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)



#buttons
btn = Button(window, text= "Enter", bg="lightGreen")
btn.grid(column=3,row=2)
btn = Button(window, text= "Cancel", bg="red")
btn.grid(column=4,row=2)

#buttonAction

#CloseWindow
window.mainloop()