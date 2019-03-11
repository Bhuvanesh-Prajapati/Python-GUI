from tkinter import *

# basic window for the calculator
cal = Tk()
cal.title("Calculator")
operator = ""
input_text = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=input_text, bd=15, insertwidth=5,
                   bg='light grey', justify='right').grid(columnspan=4)

# =======================Functions========================= #

# function to update the input field whenever an input is given
def btn_click(item):
    global operator
    operator = operator + str(item)
    input_text.set(operator)


# function to clear the input field
def btn_clear():
    global operator
    operator = ""
    input_text.set("")

# function to calculate the operator
def btn_equal():
    global operator
    result = str(eval(operator))  # 'eval' directly evalutes the operator
    input_text.set(result)
    operator = ""

# first row
clear = Button(cal, text="CLEAR", fg="black", padx=16, bd=8, font=('arial', 10, 'bold'), bg='light grey',
               command=btn_clear).grid(row=1, column=0)

# second row
seven = Button(cal, text="7", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(7)).grid(row=2, column=0)
eight = Button(cal, text="8", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(8)).grid(row=2, column=1)
nine = Button(cal, text="9", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(9)).grid(row=2, column=2)
multiply = Button(cal, text="*", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click("*")).grid(row=2, column=3)

# third row
four = Button(cal, text="4", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(4)).grid(row=3, column=0)
five = Button(cal, text="5", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(5)).grid(row=3, column=1)
six = Button(cal, text="6", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(6)).grid(row=3, column=2)
minus = Button(cal, text="-", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click("-")).grid(row=3, column=3)

# forth row
one = Button(cal, text="1", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(1)).grid(row=4, column=0)
two = Button(cal, text="2", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(2)).grid(row=4, column=1)
three = Button(cal, text="3", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(3)).grid(row=4, column=2)
plus = Button(cal, text="+", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click("+")).grid(row=4, column=3)

# fifth row
zero = Button(cal, text="0", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(0)).grid(row=5, column=0)
point = Button(cal, text=".", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click(".")).grid(row=5, column=1)
division = Button(cal, text="/", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_click("/")).grid(row=5, column=2)
equals = Button(cal, text="=", padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), bg='light grey',
               command=lambda: btn_equal()).grid(row=5, column=3)

cal.mainloop()
