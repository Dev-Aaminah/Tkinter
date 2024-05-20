from tkinter import *
from tkinter import messagebox


root = Tk()

# success messagebox
def callMe():
    messagebox.showinfo("Success", "Installation Done")
btn = Button(root, text="Message", command=callMe).pack()


# error messagebox
def errorbox():
    messagebox.showerror("Access Denied", "Try Again!")
btn1 = Button(root, text="Click", command=errorbox).pack()


# show warning
def warning():
    messagebox.showwarning("Warning!", "Try Again!")
btn2 = Button(text="Warning", command=warning).pack()


# Ask Questions in message box
def askQuestion():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == 'yes':
        root.quit()
        
  
# Ask Questions Yes, No, Cancel in message box
def askQues():
    ask = messagebox.askyesnocancel("Stop", "Do you really want to exit?")
    if ask == True:
        root.quit()
btn4 = Button(root, text="Yes/No", command=askQues).pack()
  
    
btn3 = Button(text="Message", command=askQuestion).pack()

root.geometry("400x400+120+120")
root.mainloop()