from tkinter import *  # Import all classes and functions from tkinter
import tkinter as ttk  # Import tkinter with alias ttk
import ttkbootstrap as ttk  # Import ttkbootstrap with alias ttk

# Initialize the main window using ttkbootstrap
window = ttk.Window()
window.title('Progress Bar')  # Set the title of the window
window.geometry('800x500')  # Set the size of the window

# Create an IntVar to hold the value of the scale
scale_int = ttk.IntVar(value=10)

# Create a horizontal scale (slider) widget
scale = ttk.Scale(window, 
    command=lambda value: print(scale_int.get()),  # Callback function to print the current scale value
    orient='horizontal',  # Orientation of the scale
    from_=0,  # Minimum value of the scale
    to=30,  # Maximum value of the scale
    length=300,  # Length of the scale in pixels
    variable=scale_int  # Associate the IntVar with the scale to reflect its value
    )
scale.pack()  # Add the scale to the window

# Create a vertical progress bar widget
progress_bar = ttk.Progressbar(window,
    variable=scale_int,  # Link the progress bar value to the scale's IntVar
    length=300,  # Length of the progress bar in pixels
    maximum=20,  # Maximum value of the progress bar
    orient='vertical',  # Orientation of the progress bar
    mode='determinate'  # Set the mode to determinate
)
progress_bar.pack()  # Add the progress bar to the window

# Start the Tkinter event loop
window.mainloop()