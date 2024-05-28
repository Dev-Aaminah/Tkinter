from tkinter import *
import ttkbootstrap as ttk

window = ttk.Window(themename='journal')
window.geometry('1050x800+150+150')
window.title('Events in tkinter')

text_box = Text(window)
text_box.pack()

entry = Entry(window)
entry.pack()

# events
window.bind('<Alt-KeyPress-a>', lambda event: print('an event'))

btn = Button(window, text='Button')
btn.pack()

window.mainloop()