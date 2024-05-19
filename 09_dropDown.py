from tkinter import *

root = Tk()
main_menu = Menu(root)
root.config(menu=main_menu)

# file menu 
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu= file_menu)

# edit menu
edit_menu = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)

# add items in file menu
def doNothing():
    print("Did Nothing")
file_menu.add_command(label="New File", command=doNothing)
file_menu.add_command(label="New Project", command=doNothing)
file_menu.add_command(label="Save", command=doNothing)
file_menu.add_command(label="Exit", command=doNothing)


root.mainloop()