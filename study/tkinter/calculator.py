from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
ans = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
ans.grid(row=1, column=0, columnspan=4, padx=10, pady=5)


def button_click(press):
    c_ans = str(ans.get())
    c_e = str(e.get())

    if str(press) in '+-/*':
        e.delete(0, END)
        e.insert(0, c_ans + press)
    elif press == 'c':
        ans.delete(0, END)
        e.delete(0, END)
    elif press == '=':
        equ = c_e + c_ans
        e.delete(0, END)
        ans.delete(0, END)
        e.insert(0, equ + '=')
        ans.insert(0, eval(equ))
    else:
        ans.delete(0, END)
        if c_e != '' and c_e[-1] in '+-/*':
            ans.insert(0, str(press))
        else:
            ans.insert(0, c_ans + str(press))


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=20, command=lambda: button_click('+'))
button_sub = Button(root, text='-', padx=40, pady=20, command=lambda: button_click('-'))
button_mult = Button(root, text='*', padx=40, pady=20, command=lambda: button_click('*'))
button_div = Button(root, text='/', padx=40, pady=20, command=lambda: button_click('/'))

button_equal = Button(root, text='=', padx=39, pady=20, command=lambda: button_click('='))
button_clear = Button(root, text='C', padx=39, pady=20, command=lambda: button_click('c'))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)

button_add.grid(row=5, column=3)
button_sub.grid(row=4, column=3)
button_mult.grid(row=3, column=3)
button_div.grid(row=2, column=3)

button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=1)

root.mainloop()
