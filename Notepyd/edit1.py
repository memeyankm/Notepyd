from tkinter import messagebox
import datetime

def cut():
        text.event_generate("<<Cut>>")

def copy():
        text.event_generate("<<Copy>>")

def paste():
        text.event_generate("<<Paste>>")

def delete():
        message = messagebox.askquestion('Notepad',"Do you want to Delete all")
        if message == "yes":
                text.delete('1.0','end')
        else:
               return "break"

def select_all():
        text.tag_add('sel','1.0','end')
        return 'break'

def time():
        d = datetime.now()
        text.insert('end',d)