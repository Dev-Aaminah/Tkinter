from tkinter import *
import ttkbootstrap as ttk

window = ttk.Window()

btn = ttk.Button(window, text='Press')
btn.pack()

check = ttk.Checkbutton(window, 
    text='Check It'
    )
check.pack()

# basically radio buttons are checked by default. 
# To make them unchecked we need to give value to more than one of them.
radio_btn = ttk.Radiobutton(
    window, 
    text='Radio Button', 
    state='normal',
    value= 0
    )
radio_btn.pack()

radio_btn1 = ttk.Radiobutton(
    window, 
    text='Radio Button', 
    state='normal',
    value= 1
    )

radio_btn1.pack()

window.mainloop()