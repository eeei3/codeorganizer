from tkinter import *
from tkinter import filedialog
from breakdown import Breakdown

def filebrowser():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Python scripts",
                                                      "*.py*"),
                                                     ("all files",
                                                      "*.*")))
    fileselected.set(filename)

def wrapper():
    path = fileselected.get()
    Breakdown.find(path)


root = Tk()

fileselected = StringVar(root)
fileselected.set("None")

filelabel = Entry(root, textvariable=fileselected, state='disabled')
filelabel.pack()

filebutton = Button(root, text="Search", command=filebrowser)
filebutton.pack()

startbutton = Button(root, text="Breakdown", command=wrapper)
startbutton.pack()

root.title("Either you want to save time or your code sucks")
root.minsize(600, 600)
root.mainloop()
