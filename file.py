from tkinter import *

root = Tk()
root.title("Advanced Calculator")

e = Entry(root, width=35, borderwidth=5, font=("Arial", 16))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

first_number = None
operation = None

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def set_operation(op):
    global first_number, operation
    try:
        first_number = float(e.get())
        operation = op
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def button_equal():
    global first_number, operation
    try:
        second_number = float(e.get())
        e.delete(0, END)

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                e.insert(0, "Divide Error")
                return
            result = first_number / second_number
        else:
            e.insert(0, "Error")
            return

        e.insert(0, result)

    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Buttons
buttons = [
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('0', 4, 0)
]

for (text, row, col) in buttons:
    Button(root, text=text, padx=40, pady=20,
           command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Operations
Button(root, text="+", padx=39, pady=20, command=lambda: set_operation("+")).grid(row=5, column=0)
Button(root, text="-", padx=41, pady=20, command=lambda: set_operation("-")).grid(row=5, column=1)
Button(root, text="*", padx=40, pady=20, command=lambda: set_operation("*")).grid(row=5, column=2)
Button(root, text="/", padx=41, pady=20, command=lambda: set_operation("/")).grid(row=5, column=3)

# Equal & Clear
Button(root, text="=", padx=39, pady=20, command=button_equal).grid(row=4, column=2)
Button(root, text="Clear", padx=79, pady=20, command=button_clear).grid(row=4, column=1, columnspan=2)

root.mainloop()