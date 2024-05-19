from tkinter import *

# Create the main application window
root = Tk()
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to a fraction of the screen size
width = int(screen_width * 1)  # 100% of screen width
height = int(screen_height * 1)  # 100% of screen height

# Center the window on the screen
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# Set the geometry of the window
root.geometry(f'{width}x{height}+{x}+{y}')


# Fitting Widgets starts here
one = Label(root, text="one", background="teal", foreground="grey")
two = Label(root, text="two", background="pink", foreground="yellow")
three = Label(root, text="three", background="blue", foreground="purple")
one.pack(fill=X)
# fill=Y does not work without SIDE
two.pack(fill=Y)
# now it will work
three.pack(side=LEFT, fill=Y)


root.mainloop() 