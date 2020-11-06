from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Vedant's Text Editor!")
root.geometry("1000x600")


# Create New file Func.
def new_file():
    my_text.delete("1.0", END)
    root.title("New File! - Vedant's Text Editor!")
    status_bar.config(text="New File    ")


# Create Open file Func.
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open File", filetypes=(
        ("TEXT FILES", "*.txt"), ("HTML FILES", "*.html"), ("PYTHON FILES", "*.py"), ("ALL FILES", "*.*")))
    name = text_file
    status_bar.config(text=f"{name}     ")
    root.title(f'{name} - Vedant\'s Text Editor!')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


# Create Save As Func.
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save Your File", filetypes=(("TEXT FILES", "*.txt"), ("HTML FILES", "*.html"), ("PYTHON FILES", "*.py"), ("ALL FILES", "*.*")))

    if text_file:
        name = text_file
        root.title(f'{name} - Vedant\'s Text Editor!')
        status_bar.config(text=f"{name}     ")

        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scroll Bar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="Yellow",
               selectforeground="Black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar to Bottom of App
status_bar = Label(root, text='Ready    ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
