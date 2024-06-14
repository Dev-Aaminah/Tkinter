from tkinter import *  # Import all classes and functions from tkinter
import tkinter as ttk  # Import tkinter with alias ttk
import ttkbootstrap as ttk  # Import ttkbootstrap with alias ttk

# Initialize the main window using ttkbootstrap
root = ttk.Window()
root.title('Tab Widget')  # Set the title of the window
root.geometry('750x450')  # Set the size of the window

# Create a notebook widget to hold tabs
notebook = ttk.Notebook(root)

# Create the first tab
tab1 = ttk.Frame(notebook)
label = ttk.Label(tab1, text='Text inside tab1').pack()  # Add a label to the first tab
btn = ttk.Button(tab1, text='Button').pack()  # Add a button to the first tab

# Create the second tab
tab2 = ttk.Frame(notebook)
entry = ttk.Entry(tab2).pack()  # Add an entry widget to the second tab
btn1 = ttk.Button(tab2, text='Click Me').pack()  # Add a button to the second tab

# Create the third tab (exercise)
new_tab = ttk.Frame(notebook)
new_label = ttk.Label(new_tab, text='Text inside tab3').pack()  # Add a label to the third tab
btn00 = ttk.Button(new_tab, text='Click').pack()  # Add a button to the third tab
btn01 = ttk.Button(new_tab, text='Submit').pack()  # Add another button to the third tab

# Add tabs to the notebook
notebook.add(tab1, text='Tab 1')  # Add the first tab to the notebook
notebook.add(tab2, text='Tab 2')  # Add the second tab to the notebook
notebook.add(new_tab, text='Tab 3')  # Add the third tab to the notebook

# Pack the notebook to make it visible
notebook.pack()

# Start the Tkinter event loop
root.mainloop()