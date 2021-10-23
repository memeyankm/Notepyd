from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import format1
import edit1
import file1
import help1
import right_click1

def new_window():
    root = tk.Tk() # tkinter root to initialize the app
    root.geometry('1600x900') # launch size of the app 
    root.minsize(400,300) # size when the app is minimized
    root.title('Notepyd') # title of app
    root.iconbitmap('Notepyd/notepyd.ico') # icon of the app
    
    text = ScrolledText(root, height=1000, undo=True) # text window with basic typing features 
    text.pack(fill=tk.BOTH)

    menubar = Menu(root) # menu ribbon

    text = ScrolledText(root, width=1000, height=1000)
    text.place(x=0, y=0)

    file = Menu(menubar, tearoff=0) # file menu with file management features
    file.add_command(label="New", command=file1.new)
    file.add_command(label="New window", command=new_window)
    file.add_command(label="Open", command=file1.Open)
    file.add_command(label="Save", command=file1.save)
    file.add_command(label="Save as", command=file1.save_as)
    file.add_separator()
    file.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))
    
    edit = Menu(menubar, tearoff=0) # edit menu with editing features
    edit.add_command(label="Undo",accelerator="Ctrl+Z", command=text.edit_undo)
    edit.add_command(label="Redo",accelerator="Ctrl+Y", command=text.edit_redo)
    edit.add_separator()
    edit.add_command(label="Cut",accelerator="Ctrl+X", command=edit1.cut)
    edit.add_command(label="Copy",accelerator="Ctrl+C", command=edit1.copy)
    edit.add_command(label="Paste",accelerator="Ctrl+V", command=edit1.paste)
    edit.add_command(label="Delete",accelerator="Del", command=edit1.delete)
    edit.add_command(label="Select All",accelerator="Ctrl+A", command=edit1.select_all)
    edit.add_command(label="Time/Date",accelerator="F5", command=edit1.time)
    menubar.add_cascade(label="Edit",menu=edit)

    Format = Menu(menubar, tearoff=0) # format menu with text formatting features
    Format.add_command(label="Word Wrap", command=format1.wrap)
    Format.add_command(label="Font...", command=format1.fonts)
    menubar.add_cascade(label="Format", menu=Format)

    m = Menu(root, tearoff = 0) # right click commands
    m.add_command(label ="Select All", accelerator="Ctrl+A", command=edit1.select_all) 
    m.add_command(label ="Cut", accelerator="Ctrl+X", command=edit1.cut) 
    m.add_command(label ="Copy", accelerator="Ctrl+C", command=edit1.copy) 
    m.add_command(label ="Paste", accelerator="Ctrl+V", command=edit1.paste) 
    m.add_command(label ="Delete", accelerator="Del", command=edit1.delete) 
    m.add_separator() 
    m.add_command(label ="Undo", accelerator="Ctrl+Z", command=text.edit_undo)
    m.add_command(label ="Redo", accelerator="Ctrl+Z", command=text.edit_redo) 
    root.bind("<Button-3>", right_click1.do_popup) 

    Help = Menu(menubar, tearoff = 0) # help menu
    Help.add_command(label="View Help", command=help1.view_help) # guides to the readme
    Help.add_command(label="Send FeedBack", command=help1.send_feedback) # giudes to my twitter
    Help.add_command(label="About Notepyd", command= help1.about) # guides to my github
    menubar.add_cascade(label="Help", menu=Help)

    root.config(menu=menubar)

    root.mainloop()

new_window()
