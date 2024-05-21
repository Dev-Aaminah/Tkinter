from tkinter import *

root = Tk()

label1 = Label(root, text="Hello Sir").place(x=600,y=450)
label2 = Label(root, text="Hello Miss")
label2.place(x=600,y=400)

root.geometry("1200x850+120+120")
root.mainloop()