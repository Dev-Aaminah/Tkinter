from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500, bg="blue")
canvas.pack()

line = canvas.create_line(0,0,200,500)
line1 = canvas.create_line(200,500,0,200, fill="red")


root.geometry("1550x830+0+0")
root.mainloop()