import tkinter as tk  # Import tkinter as tk
from tkinter import ttk  # Import ttk from tkinter
import ttkbootstrap  # Import ttkbootstrap
from tkinter import scrolledtext  # Import scrolledtext from tkinter

# Initialize the main window using tkinter
Window = tk.Tk()
Window.title('Scrolled Text')  # Set the title of the window
Window.geometry('800x550')  # Set the size of the window

# Create and pack a scrolled text widget
scrolled_text = scrolledtext.ScrolledText(Window,
    width=50,  # Set the width of the scrolled text widget
    height=10)  # Set the height of the scrolled text widget
scrolled_text.pack()  # Add the scrolled text widget to the window

# Start the Tkinter event loop
Window.mainloop()