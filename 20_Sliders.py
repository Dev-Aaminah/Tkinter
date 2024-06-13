import tkinter as tk
from tkinter import ttk

# Initialize the main window
window = tk.Tk()
window.title('Sliders')  # Set the title of the window
window.geometry('1000x700')  # Set the size of the window

# Create an IntVar to hold the value of the slider
scale_int = tk.IntVar(value=15)

# Create a vertical slider (Scale) widget
slider = ttk.Scale(window,
                   command=lambda value: print(scale_int.get()),  # Callback function to print the current slider value
                   from_=0,  # Minimum value of the slider
                   to=30,  # Maximum value of the slider
                   length=300,  # Length of the slider in pixels
                   orient='vertical',  # Orientation of the slider
                   variable=scale_int)  # Associate the IntVar with the slider to reflect its value
slider.pack()  # Add the slider to the window

# Start the Tkinter event loop
window.mainloop()