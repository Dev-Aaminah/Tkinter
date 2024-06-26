import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
        # widgets
        self.menu = Menu(self)
        
        # run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight= 1)
        
        self.create_widgets()
        
    def create_widgets(self):
        btn1 = ttk.Button(self, text='Button1')
        btn2 = ttk.Button(self, text='Button2')
        btn3 = ttk.Button(self, text='Button3')

        # menu slider
        menu_slider1 = ttk.Scale(self, orient='vertical')
        menu_slider2 = ttk.Scale(self, orient='vertical')

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text='check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text='check 2')
            
        entry = ttk.Entry(self)
        
        # create grid
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.columnconfigure((0,1,2,3,4), weight=1, uniform='a')
            
        # place the widgets
        btn1.grid(row=0, column=0, sticky='nswe', columnspan=2)
        btn2.grid(row=0, column=2, sticky='nswe')
        btn3.grid(row=1, column=0, sticky='nswe', columnspan=3)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)
        
        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)
        
        # entry layout
        entry.place(relx=0.5, rely= 0.95, relwidth=0.9, anchor='center')
        
App('Class based app',(600,600))