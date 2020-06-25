from tkinter import *

root = Tk()


def myClick():
    text = "Hello " + name.get() + " ur gay."
    myLabel = Label(root, text=text)
    myLabel.grid(row=1, column=0)


name = Entry(root, width=20)
name.insert(0, "Enter your name")

myButton = Button(root, text="Enter", padx=50, pady=50, command=myClick)

name.grid(row=0, column=0)
myButton.grid(row=0, column=1)

root.mainloop()
