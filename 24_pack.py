from tkinter import *  # Import all classes and functions from tkinter
import tkinter as ttk  # Import tkinter with alias ttk
import ttkbootstrap  # Import ttkbootstrap

# Initialize the main window using ttkbootstrap
root = ttk.Tk()
root.title('Pack Method in Tkinter')  # Set the title of the window
root.geometry('750x450')  # Set the size of the window

# Create labels with different background colors
label1 = Label(root, text='First Label', background='red')
label2 = Label(root, text='Second Label', background='green')
label3 = Label(root, text='Third Label', background='blue')

# Create a button with a pink background
btn = Button(root, text='Button', background='pink')

# Layout management using the pack method
label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)  # Place label1 at the top with padding
label2.pack(side='left', expand=True, fill='both')  # Place label2 on the left
label3.pack(side='top', expand=True, fill='both')  # Place label3 at the top
btn.pack(side='top', expand=True, fill='both')  # Place the button at the top

# Start the Tkinter event loop
root.mainloop()
