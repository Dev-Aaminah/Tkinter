from tkinter import *  # Import all classes and functions from tkinter
import tkinter as ttk  # Import tkinter with alias ttk
import ttkbootstrap  # Import ttkbootstrap for theming

# Initialize the main window
root = Tk()
root.geometry('550x450')  # Set the size of the window

# Create labels with specified background colors and text
label1 = Label(root, background='sea green', text='Label1', width=50)
label2 = Label(root, background='pink', text='Label2', width=50)

# Pack the labels into the window
label1.pack()  # Pack label1 with default options
label2.pack(fill='x')  # Pack label2 to fill the horizontal space

# Start the Tkinter event loop
root.mainloop()