# import module
from tkinter import *

# creating window

root  = Tk()

# label
theLabel = Label(root, text= "Hello")
# to print label on window
theLabel.pack()

# keep showing window until user hits close icon
root.mainloop()