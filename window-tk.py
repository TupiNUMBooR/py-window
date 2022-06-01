#!/usr/bin/env python3
import text
from tkinter import *

tk = Tk()
tk.title("window-tk.py")
label = Label(tk, text="empty")
label.pack()
Button(tk, text="Button", command=lambda: label.config(text=text.get())).pack()
tk.mainloop()
