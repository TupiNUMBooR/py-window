#!/usr/bin/env python3
import text
from tkinter import *
from PIL import ImageTk, Image
import pillow_avif

def on_button():
    # https://www.pythontutorial.net/tkinter/tkinter-photoimage/
    tk.im = ImageTk.PhotoImage(Image.open('240.avif'))
    # tk.im = PhotoImage(file="./240.jpg")
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
