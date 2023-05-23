from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('New frame')

frame = LabelFrame(root, text='This is mmy new frame', padx=50, pady=50)
frame.pack(padx=10, pady=10)

button_1 = Button(frame, text='Button 1')
button_2 = Button(frame, text='Button 2')

button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)

root.mainloop()

