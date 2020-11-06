from tkinter import *

root = Tk()
root.title("Vedant's GUI8")
root.iconbitmap("A:/Users/anvit/Downloads/download.ico")

frame = LabelFrame(root, text="This is my frame!", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Click me!!")
b2 = Button(frame, text="Click here!!")

b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
