from tkinter import *


root = Tk()
root.title("Vedant's GUI9")
root.iconbitmap("A:/Users/anvit/Downloads/download.ico")


v = IntVar()
v.set("1")


def click(value):
    label = Label(root, text=value)
    label.pack()


Radiobutton(root, text="Option 1", variable=v, value=1, command=lambda: click(v.get())).pack()
Radiobutton(root, text="Option 2", variable=v, value=2, command=lambda: click(v.get())).pack()

label = Label(root, text=v.get())
label.pack()

button = Button(root, text="Click me!!", command=lambda: click(v.get()))
button.pack()


root.mainloop()
