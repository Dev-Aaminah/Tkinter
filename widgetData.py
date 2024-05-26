import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
    # get the content of entry
    entry_text = entry.get()
    
    # update the label
    label['text'] = entry_text
    
    # disable entry
    entry['state'] = 'disabled'

def enable():
    label['text'] = 'Label'
    entry['state'] = 'enabled'
    
window = ttk.Window(themename='vapor')
window.geometry('500x350')
window.title('Getting and Setting Widgets')

# label
label = ttk.Label(master=window, text='Label')
label.pack()

# entry
entry = ttk.Entry(master=window)
entry.pack()

# button
button = ttk.Button(master=window, text='Click', command= button_func)
button.pack()

# btn
btn = ttk.Button(master=window, text='BUTTON', command=enable)
btn.pack()

window.mainloop()