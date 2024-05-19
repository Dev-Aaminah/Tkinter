from tkinter import *

root = Tk()

# def callme(event): defines a function named callme that takes one argument, event.
def callme(event):
    print("Called")


# btn.bind("<Button-1>", callme) binds the left mouse button click event (<Button-1>) to the callme function.
btn = Button(root, text="Click Me")
# <Button-1> refers to the left mouse button click event in Tkinter.
btn.bind("<Button-1>", callme)
btn.pack()

root.mainloop()