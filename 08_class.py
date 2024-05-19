from tkinter import *



class myBtn:
    def __init__(self, master):
        self.printBtn = Button(master, text="Click" , command=self.printMsg)
        self.printBtn.pack(side=LEFT)
        
        self.quitBtn = Button(master, text="Quit", command=master.quit)
        self.quitBtn.pack(side=RIGHT)
        
    def printMsg(self):
        print("Printing Message")

root = Tk()
b = myBtn(root)
root.mainloop()