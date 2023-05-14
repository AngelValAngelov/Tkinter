from tkinter import *

root = Tk()
root.title('Checkboxes')
root.geometry('400x400')

var = StringVar()


def show():
    Label(root, text=var.get()).pack()


c = Checkbutton(root, text='Are you agree?', variable=var, onvalue='Yes', offvalue='No')
c.deselect()
c.pack()

myButton = Button(root, text='Show selection', command=show).pack()

mainloop()
