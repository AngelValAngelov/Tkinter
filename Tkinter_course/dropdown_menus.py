from tkinter import *

root = Tk()
root.title('Dropdown menus')
root.geometry('400x400')


def show():
    Label(root, text=clicked.get()).pack()


options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='My selection: ', command=show).pack()

mainloop()
