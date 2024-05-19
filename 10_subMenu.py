from tkinter import *
root = Tk()

main_menu = Menu(root)
root.config(menu=main_menu)

# MENU
file1 = Menu(main_menu)
main_menu.add_cascade(label="Option 1", menu= file1)

file2 = Menu(main_menu)
main_menu.add_cascade(label="Option 2", menu= file2)

file3 = Menu(main_menu)
main_menu.add_cascade(label="Option 3", menu= file3)


# sub menu
fileSubMenu = Menu(file1)
fileSubMenu.add_cascade(label="New")
file1.add_cascade(label="1st", menu=fileSubMenu)


root.mainloop()