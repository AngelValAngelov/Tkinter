from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Dialog box')

root.filename = filedialog.askopenfilename(initialdir="/Users/Angel/Desktop", title='Select a file', filetypes=(('pdf files', '*.pdf'), ('all files','*.*')))


root.mainloop()
