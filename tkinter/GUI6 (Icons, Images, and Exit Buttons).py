from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Vedant's GUI6")
root.iconbitmap("A:/Users/anvit/Downloads/download.ico")


my_img = ImageTk.PhotoImage(Image.open("A:\\Users\\anvit\\Downloads\\Ganesh-Bhagwan-Ji-Photo-Wallpapers.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()
