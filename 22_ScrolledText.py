import tkinter as tk
from tkinter import ttk
import ttkbootstrap
from tkinter import scrolledtext

Window = tk.Tk()
Window.title('Scrolled Text')
Window.geometry('800x550')

scrolled_text = scrolledtext.ScrolledText(Window,
    width=50,
    height=10)
scrolled_text.pack()


Window.mainloop()