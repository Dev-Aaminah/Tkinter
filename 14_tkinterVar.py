import tkinter as tk 
import ttkbootstrap as ttk

window = ttk.Window(themename='journal')
window.title('Tkinter Variable')
window.geometry('350x200')

def btn_pressed():    
    string_var.set('')

# tkinter variable
string_var = tk.StringVar()

# label
label = ttk.Label(master=window, text='label' , textvariable=string_var)
label.pack()

# entry
entry = ttk.Entry(master=window , textvariable=string_var)
entry.pack()

btn = ttk.Button(master=window, text='Button', command=btn_pressed)
btn.pack()

window.mainloop()