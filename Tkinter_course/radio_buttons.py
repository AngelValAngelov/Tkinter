import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio buttons')

r = IntVar()
r.set('2')

TOPPINGS = {
    'Pepperoni': 'Pepperoni',
    'Cheese': 'Cheese',
    'Mushrooms': 'Mushrooms',
    'Onion': 'Onion',
}

pizza = StringVar()
pizza.set('Pepperoni')

for text, topping in TOPPINGS.items():
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text='Click here', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
