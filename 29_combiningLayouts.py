from tkinter import *
import tkinter as ttk
import ttkbootstrap as ttk

root = Tk()
root.title('Combined Layouts')
root.geometry('650x450')
root.minsize(600, 600)

# Create instances of Frame
menu_frame = ttk.Frame(root)
main_frame = ttk.Frame(root)

btn1 = ttk.Button(menu_frame, text='Button1')
btn2 = ttk.Button(menu_frame, text='Button2')
btn3 = ttk.Button(menu_frame, text='Button3')

# menu slider
menu_slider1 = ttk.Scale(menu_frame, orient='vertical')
menu_slider2 = ttk.Scale(menu_frame, orient='vertical')

# menu layout
menu_frame.columnconfigure((0,1,2), weight=1)
menu_frame.rowconfigure((0,1,2,3,4),weight=1)

btn1.grid(row=0, column=0, sticky='nswe', columnspan=2)
btn2.grid(row=0, column=2, sticky='nswe', columnspan=2)
btn3.grid(row=1, column=0, sticky='nswe', columnspan=2)

menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)

# Place the frames using the place geometry manager
menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)


root.mainloop()