import tkinter as tk

def click(btn_text):
    current = input.get()
    input.delete(0, tk.END)
    input.insert(0, current + btn_text)

def clear():
    input.delete(0, tk.END)

def calculate():
    try:
        result = eval(input.get())
        input.delete(0, tk.END)
        input.insert(0, str(result))
    except:
        input.delete(0, tk.END)
        input.insert(0, "Error")

m = tk.Tk()
m.title("Simple Calculator")
m.geometry("250x300")

input = tk.input(m, width=20, font=("Forte", 18), bd=5, justify="right")
input.pack(pady=10)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "C", "=", "+")
]

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
