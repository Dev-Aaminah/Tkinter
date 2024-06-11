from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from random import choice

window = ttk.Window()
window.geometry('1200x800')
window.title('Tree in tkinter')

# data
first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jessica"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# treeView
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Sur Name')
table.heading('email', text='Email')
table.pack(fill= 'both', expand=True)

# values into a table
# table.insert(parent='', index=0, values=('John', 'Doe', 'J.doe@gmail.com'))

for i in range(100):
    first=choice(first_names)
    last=choice(last_names)
    email= f'{first}{last}@gmail.com'
    table.insert(parent='', index=0, values= (first, last, email))


window.mainloop()