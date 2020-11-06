from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=4, bg="Red", fg="White")
e.pack()
e.get()
e.insert(0, "Enter Your Name!")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name!", command=myClick, bg="Blue", fg="White")
myButton.pack()

root.mainloop()
