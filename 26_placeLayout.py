import tkinter as tk  # Import the tkinter library and alias it as tk
from tkinter import ttk  # Import ttk from tkinter for advanced widgets

# Initialize the main window
root = tk.Tk()
root.title('Pack Layout')  # Set the title of the window
root.geometry('450x650')  # Set the size of the window

# Create widgets
label1 = ttk.Label(root, text='Label 1', background='red')  # Create a label with red background
label2 = ttk.Label(root, text='Label 2', background='blue')  # Create a label with blue background
label3 = ttk.Label(root, text='Label 3', background='green')  # Create a label with green background
btn = ttk.Button(root, text='Button')  # Create a button

# Place the widgets using the place geometry manager
label1.place(x=300, y=100, width=100, height=200)  # Place label1 at coordinates (300, 100) with specified width and height
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)  # Place label2 relative to the size of the window
label3.place(x=80, y=60, width=160, height=300)  # Place label3 at coordinates (80, 60) with specified width and height
btn.place(relx=1, rely=1, anchor='se')  # Place the button at the bottom-right corner of the window

# Start the Tkinter event loop
root.mainloop()