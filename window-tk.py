#!/usr/bin/env python3
import text
from tkinter import *


def on_button():
    label.config(text=text.get())


tk = Tk()
tk.title("window-tk.py")

label = Label(tk, text="empty")
label.pack(side=TOP)
widget = Button(tk, text="Button", command=on_button)
widget.pack(side=BOTTOM)
tk.mainloop()
