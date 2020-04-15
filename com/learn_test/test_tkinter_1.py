import tkinter as tk


window = tk.Tk()
bt1 = tk.Button()
bt1.pack()
def click_but1():
    print('haha')
bt1.config(text='open',command=click_but1)

window.mainloop()