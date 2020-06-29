from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ding Dong Program")

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.grid(row=0, column=0, padx=10, pady=10)

r = IntVar()
r.set('1')


def clicked():
    status = Label(root, text="Option " + str(r.get()) + " Selected",
                   bd=1, relief=SUNKEN,
                   padx=5, pady=5,
                   anchor=E
                   )
    status.grid(row=1, column=0, sticky=W + E)


def popup():
    response = messagebox.askyesno("This is my popup", "hello world")
    if response == 1:
        Label(frame, text="Yes").pack()
    else:
        Label(frame, text="No").pack()



# Elements
Radiobutton(frame, text="Option 1", variable=r, value=1, command=clicked).pack()
Radiobutton(frame, text="Option 2", variable=r, value=2, command=clicked).pack()

b = Button(frame, text="Popup", command=popup)


# Display elements
clicked()
b.pack()


root.mainloop()
