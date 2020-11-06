from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Hello Everyone!")
myLabel2 = Label(root, text= "I am Vedant Nichal.")
myLabel3 = Label(root, text= "                       ")

#Showing it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()
