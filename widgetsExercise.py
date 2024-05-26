import tkinter as tk
import ttkbootstrap as ttk

# def print_something():
#     print('hello')

window = ttk.Window(themename='journal')
window.title('Widgets Exercise')
window.geometry('450x300')

entry = ttk.Entry().pack()

label = ttk.Label(master=window, text='My Label', font='times 24 bold').pack()

# button = ttk.Button(master=window, text='Button', command=print_something).pack()

# another way to print 'hello' in command line
button = ttk.Button(master=window, text='Button', command=lambda: print('hello')).pack()
window.mainloop()