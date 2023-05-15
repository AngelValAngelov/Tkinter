from tkinter import *

root = Tk()
root.title('new windows')


def open():
    top = Toplevel()
    top.title('Second window')
    Label(top, text='Hello world').pack()
    Button(top, text='Close window', command=top.destroy).pack()


button = Button(root, text='Open second window', command=open).pack()

mainloop()
