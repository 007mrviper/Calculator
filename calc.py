from tkinter import *
from decimal import  Decimal

root = Tk()
root.title('Calculator')

input_ = Entry(root, width=40, borderwidth=5)
input_.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(num):
    current = input_.get()
    input_.delete(0, END)
    input_.insert(0, str(current) + str(num))

def add():
    current = input_.get()
    global initial
    initial = Decimal(current)
    input_.delete(0, END)
    global mode
    mode = 'add'

def sub():
    current = input_.get()
    global initial
    initial = Decimal(current)
    input_.delete(0, END)
    global mode
    mode = 'sub'

def mul():
    current = input_.get()
    global initial
    initial = Decimal(current)
    input_.delete(0, END)
    global mode
    mode = 'mul'

def divide():
    current = input_.get()
    global initial
    initial = Decimal(current)
    input_.delete(0, END)
    global mode
    mode = 'div'

def remove():
    input_.delete(0, END)

def new():
    pass

def square():
    # current = input_.get()
    global Square, mode
    Square = Decimal(input_.get())
    mode = 'square'

def Ans():
    final = input_.get()
    if mode == 'add':
        result = initial + Decimal(final)
        input_.delete(0, END)
        input_.insert(0, result)

    if mode == 'sub':
        result = initial - Decimal(final)
        input_.delete(0, END)
        input_.insert(0, result)

    if mode == 'mul':
        result = initial * Decimal(final)
        input_.delete(0, END)
        input_.insert(0, result)

    if mode == 'div':
        result = initial / Decimal(final)
        input_.delete(0, END)
        input_.insert(0, result)

    if mode == 'square':
        result = Square * Square
        input_.delete(0, END)
        input_.insert(0, result)

button1 = Button(root, text="1", padx=25, pady=12, command=lambda: click(1))
button2 = Button(root, text="2", padx=25, pady=12, command=lambda: click(2))
button3 = Button(root, text="3", padx=25, pady=12, command=lambda: click(3))
button4 = Button(root, text="4", padx=25, pady=12, command=lambda: click(4))
button5 = Button(root, text="5", padx=25, pady=12, command=lambda: click(5))
button6 = Button(root, text="6", padx=25, pady=12, command=lambda: click(6))
button7 = Button(root, text="7", padx=25, pady=12, command=lambda: click(7))
button8 = Button(root, text="8", padx=25, pady=12, command=lambda: click(8))
button9 = Button(root, text="9", padx=25, pady=12, command=lambda: click(9))
button0 = Button(root, text="0", padx=25, pady=12, command=lambda: click(0))

delete = Button(root, text="Del", padx=18, pady=12, bg='#ed1c54', fg='white',command=lambda: click())
Sub = Button(root, text="-", padx=25, pady=12, command=sub)
Mul = Button(root, text="x", padx=25, pady=12, command=mul)
Div = Button(root, text="/", padx=25, pady=12, command=divide)
Add = Button(root, text="+", padx=25, pady=12, command=add)

clear = Button(root, text="C", padx=25, pady=12, command=remove).grid(row=4, column=2)
ans = Button(root, text="=", padx=130, pady=12, bg='#98d979',command=Ans).grid(row=6, column=0,columnspan=4)

dot = Button(root, text=".", padx=26.47, pady=12, command=lambda: click('.')).grid(row=4, column=0)
percent = Button(root, text="%", padx=25, pady=12, command=new).grid(row=5, column=1)
Root = Button(root, text="√", padx=25, pady=12, command=new).grid(row=5, column=2)
sq = Button(root, text="x^2", padx=18, pady=12, command=square).grid(row=5, column=0)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)

delete.grid(row=1,column=3)
Sub.grid(row=2, column=3)
Mul.grid(row=3, column=3)
Div.grid(row=4, column=3)
Add.grid(row=5, column=3)

root.mainloop()
