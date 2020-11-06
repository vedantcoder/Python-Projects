from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="This button works!!")
    myLabel.pack()

myButton = Button(root, text="Click Here !!!", command=myClick, bg="Blue", fg="White")
myButton.pack()

root.mainloop()

