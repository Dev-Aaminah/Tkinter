from tkinter import *

root = Tk()

frame = Frame(root, width= 1200 , height= 700)
# adding components
btn1 = Button(frame, text="Add")
btn1.pack(side=LEFT)
btn2 = Button(frame, text="Delete")
btn2.pack(side=TOP)
btn3 = Button(frame, text="Create ")
btn3.pack(side=RIGHT)

frame.pack()


frame1 = Frame(root)
btn = Button(frame1, text="Bye  ")
btn.pack()
frame1.pack(side=BOTTOM)


root.mainloop()