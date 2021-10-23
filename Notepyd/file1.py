from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def new():
        text.delete('1.0','end')

def Open():
        root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        file = open(root.filename)
        text.insert('end',file.read())

def save():
        root.filename = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        root.filename.write('Untitled')

def save_as():
        root.filename = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if root.filename is None:
                return
        file_save =  str(text.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()

def exit():
        message = messagebox.askquestion('Notepad',"Do you want to save changes")
        if message == "yes":
                save_as()
        else:
                root.destroy()
