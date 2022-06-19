#!/usr/bin/env python3
import text
from tkinter import *


def on_button():
    # https://www.pythontutorial.net/tkinter/tkinter-photoimage/
    # https://placekitten.com/640/240
    tk.im = PhotoImage(file="./240.png")
    l_im.config(image=tk.im)
    l_txt.config(text=text.get())


tk = Tk()
tk.title("window-tk.py")
l_txt = Label(tk, text="empty")
l_txt.pack()
l_im = Label(tk)
l_im.pack()
Button(tk, text="Button", command=on_button).pack()

tk.mainloop()
