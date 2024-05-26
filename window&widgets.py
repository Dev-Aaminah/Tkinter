# import tkinter as ttk
import tkinter as tk
import ttkbootstrap as ttk

def btn_func():
    print('pressed')

window = tk.Tk()
window.title('Window & Widgets')
window.geometry('1200x600+120+120')

# ttk widgets / ttk label
label = ttk.Label(master=window, text='This is a test')
label.pack()

# tk widget / tk textbox
# multiline textbox
textbox = tk.Text(master=window)
textbox.pack()



# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window , text='Button', command= btn_func)
button.pack()

window.mainloop()