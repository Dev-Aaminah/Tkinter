from tkinter import *  # Import all classes and functions from tkinter
from tkinter import ttk  # Import ttk from tkinter for advanced widgets
import ttkbootstrap as ttk  # Import ttkbootstrap for theming

# Initialize the main window using ttkbootstrap
root = ttk.Window()
root.title('Pack and Frame')  # Set the title of the window
root.geometry('450x550')  # Set the size of the window

# Create the top frame and add labels
top_frame = ttk.Frame(root)  # Create a frame to hold the top labels
# Add a label to the top frame, positioned to the left, filling the space and expanding
label1 = ttk.Label(top_frame, text='First label', background='red').pack(side='left', fill='both', expand=True)
# Add another label to the top frame, positioned to the right, filling the space and expanding
label2 = ttk.Label(top_frame, text='Second label', background='blue').pack(side='right', fill='both', expand=True)
top_frame.pack(fill='both', expand=True)  # Pack the top frame to fill available space and expand

# Add another label directly to the root window with padding
label3 = ttk.Label(root, text='Another label', background='green').pack(padx=100, pady=100)

# Create the bottom frame
bottom_frame = ttk.Frame(root)  # Create a frame to hold the bottom widgets

# Create an inner frame within the bottom frame
frame_btm = ttk.Frame(bottom_frame)  # Create a frame inside the bottom frame to group some widgets

# Add buttons and labels to the inner frame
btn00 = ttk.Button(frame_btm, text='A Button')  # Create a button inside the inner frame
btn00.pack(side='left', fill='both', expand=True)  # Pack the button, positioned to the left, filling the space and expanding

# Add a label inside the inner frame, positioned to the left, filling the space and expanding
label4 = ttk.Label(frame_btm, text='Last of the labels', background='orange')
label4.pack(side='left', fill='both', expand=True)

# Add another button inside the inner frame, with a white background
btn01 = Button(frame_btm, text='A Button', background='white')
btn01.pack(side='left', fill='both', expand=True)

# Pack the inner frame within the bottom frame, positioned to the left, with padding
frame_btm.pack(side='left', expand=True, fill='both', padx=10, pady=10)

# Add buttons directly to the bottom frame, with padding and expansion to fill available space
btn1 = Button(bottom_frame, text='Button1').pack(expand=True, fill='both', padx=5, pady=10)
btn2 = Button(bottom_frame, text='Button1').pack(expand=True, fill='both', padx=5, pady=10)
btn3 = Button(bottom_frame, text='Button1').pack(expand=True, fill='both', padx=5, pady=10)

# Pack the bottom frame within the root window to fill available space and expand
bottom_frame.pack(expand=True, fill='both')

# Start the Tkinter event loop to wait for user interaction
root.mainloop()