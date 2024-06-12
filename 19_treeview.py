from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk
from random import choice

window = ttk.Window()
window.geometry('1200x800')
window.title('Tree in tkinter')

# data
first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jessica"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# treeView
table = ttk.Treeview(window, columns=('first', 'last', 'email'))
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[0]}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)
    
    
# events in table
table.bind('<<TreeviewSelect>>' , lambda event: print(table.selection()))
 

def deleteItems(_):
    print('Delete')
    for i in table.selection():
        table.delete(i)
    
table.bind('<Delete>', deleteItems)
 
# items in table
window.mainloop()