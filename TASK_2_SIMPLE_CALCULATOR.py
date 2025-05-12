#This is a simple calculator GUI application in Python.

import tkinter as tk
#Tkinter is a standard GUI toolkit in Python.


def click(btn_text):# Function to handle button clicks
    current = input.get()
    input.delete(0, tk.END)
    input.insert(0, current + btn_text)

def clear():# Function to clear the input field
    input.delete(0, tk.END)

def calculate():# Function to evaluate the expression
    try:
        result = eval(input.get())
        input.delete(0, tk.END)
        input.insert(0, str(result))
    except:# Handle any errors in the expression
        input.delete(0, tk.END)
        input.insert(0, "Error")

m = tk.Tk()
m.title("Simple Calculator")
m.geometry("250x300")

input = tk.Entry(m, width=20, font=("Forte", 18), bd=5, justify="right")# Entry widget for input
input.pack(pady=10)

#Layout the buttons in a grid
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "C", "=", "+")
]

# Create buttons and add them to the window
for row in buttons:
    fraem = tk.Frame(m)
    fraem.pack()
    for b in row:
        action = (
            clear if b == "C"
            else calculate if b == "="
            else lambda b=b: click(b)
        )
        tk.Button(fraem, text=b, width=5, height=2, font=("Arial", 14), command=action).pack(side="left", padx=2, pady=2)

m.mainloop()
