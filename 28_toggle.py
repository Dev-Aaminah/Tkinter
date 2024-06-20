import tkinter as ttk  # Import tkinter with alias ttk
from tkinter import *  # Import all classes and functions from tkinter
import ttkbootstrap as ttk  # Import ttkbootstrap for theming

# Initialize the main window
root = Tk()
root.title('Toggle In Tkinter')  # Set the title of the window
root.geometry('750x450')  # Set the size of the window

# Function to toggle the background color of label1
def toggle_effect():
    label1.config(background='sky blue')

# Create label1 with a pink background and pack it
label1 = ttk.Label(root, background='pink')
label1.pack(expand=True, fill='both')

# Create a button on label1 to toggle the background color
btn = ttk.Button(label1, text='Click', command=toggle_effect).pack(expand=True)

# Define default color for label2
defaultColor = 'sky blue'

# Function to toggle the background color of label2
def toggleForContClrChange():
    global defaultColor
    
    if defaultColor == 'sky blue':
        label2.config(background='pink')
        defaultColor = 'pink'
    else:
        label2.config(background='sky blue')
        defaultColor = 'sky blue'

# Create label2 with the default background color and pack it
label2 = ttk.Label(root, background=defaultColor)
label2.pack(expand=True, fill='both')

# Create a button on label2 to toggle the background color
btn2 = ttk.Button(label2, text='Click', command=toggleForContClrChange)
btn2.pack(expand=True)

# Start the Tkinter event loop
root.mainloop()