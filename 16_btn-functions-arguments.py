from tkinter import *
import ttkbootstrap as ttk

# Create the main window
window = ttk.Window()
window.title('Buttons, Functions & Arguments')
window.geometry('450x300+650+350')

def btn_func():
    print(entry.get())

# text variable
entry_string = StringVar(value='Hello')

entry = Entry(window, textvariable=entry_string)
entry.pack()

btn = Button(window, text='Button' , command=lambda: btn_func(entry_string))
btn.pack()

# Start the main loop
window.mainloop()
