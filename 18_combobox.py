from tkinter import *
import ttkbootstrap as ttk

window = ttk.Window(themename='journal')
window.geometry('1050x800+150+150')
window.title('Events in tkinter')

# combobox
combo_list = ('Face wash', 'shampoo', 'toothpaste')
# for default option
default_item = StringVar(value=combo_list[0])
combo = ttk.Combobox(window, textvariable=default_item)
combo['values'] = combo_list
combo.pack()

# spinbox
spin = Spinbox(window, from_=0, to = 20)
spin.pack()



window.mainloop()