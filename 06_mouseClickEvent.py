from tkinter import *

root = Tk()
root.geometry("800x600")


def leftClick(event):
    print("Left Clicked")
def rightClick(event):
    print("Right Clicked")
def middleClick(event):
    print("Button Clicked")

frame = Frame(root, width=300, height=300, bg="teal")
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", rightClick)
frame.bind("<Button-3>", middleClick)
frame.pack()


root.mainloop()