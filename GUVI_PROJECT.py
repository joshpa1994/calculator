import tkinter as tk
import tkinter.messagebox
from tkinter.constants import GROOVE
from tkinter.constants import FLAT
import math

window = tk.Tk()
window.title('Scientific Calculator')
frame = tk.Frame(master=window, bg="powder blue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=GROOVE, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def my_input(number):
    entry.insert(tk.END, number)


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except Exception:
        tkinter.messagebox.showinfo("error", "enter correct value")


def clear():
    entry.delete(0, tk.END)


def sqrt():
    try:
        y = str(math.sqrt(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except Exception:
        tkinter.messagebox.showinfo("error", "enter correct value")


def sin():
    try:
        ans = float(entry.get())
        ans = math.sin(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showinfo("value error", "enter correct value")


def cos():
    try:
        ans = float(entry.get())
        ans = math.cos(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showinfo("value error", "enter correct value")


def tan():
    try:
        ans = float(entry.get())
        ans = math.tan(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showinfo("value error", "enter correct value")


def fact():
    try:
        ans = float(entry.get())
        ans = math.factorial((ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showinfo("value error", "enter correct value")


button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(1))
button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(2))
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(3))
button_3.grid(row=1, column=2, pady=2)

button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(4))
button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(5))
button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(6))
button_6.grid(row=2, column=2, pady=2)

button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(7))
button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(8))
button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(9))
button_9.grid(row=3, column=2, pady=2)

button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, relief=FLAT, command=lambda: my_input(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text='+', padx=15,
                       pady=5, width=3, relief=GROOVE, command=lambda: my_input('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(master=frame, text='-', padx=15,
                            pady=5, width=3, relief=GROOVE, command=lambda: my_input('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_div = tk.Button(master=frame, text='/', padx=15,
                       pady=5, width=3, relief=GROOVE, command=lambda: my_input('/'))
button_div.grid(row=6, column=0, pady=2)

button_multiply = tk.Button(master=frame, text='*', padx=15,
                            pady=5, width=3, relief=GROOVE, command=lambda: my_input('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_sqrt = tk.Button(master=frame, text='sqrt', padx=15,
                        pady=5, width=3, relief=GROOVE, command=sqrt)
button_sqrt.grid(row=4, column=0, pady=2)

button_equal = tk.Button(master=frame, text='=', padx=15,
                         pady=5, width=3, relief=GROOVE, command=equal)
button_equal.grid(row=8, column=1, pady=2)

button_clear = tk.Button(master=frame, text='C', padx=30,
                         pady=5, width=3, relief=GROOVE, command=clear)
button_clear.grid(row=7, column=2, pady=2)

button_sin = tk.Button(master=frame, text='sin', padx=15,
                       pady=5, width=3, relief=GROOVE, command=sin)
button_sin.grid(row=6, column=1, pady=2)

button_cos = tk.Button(master=frame, text='cos', padx=15,
                       pady=5, width=3, relief=GROOVE, command=cos)
button_cos.grid(row=6, column=2, pady=2)

button_tan = tk.Button(master=frame, text='tan', padx=15,
                       pady=5, width=3, relief=GROOVE, command=tan)
button_tan.grid(row=7, column=0, pady=2)

button_fact = tk.Button(master=frame, text='x!', padx=15,
                        pady=4, width=3, relief=GROOVE, command=fact)
button_fact.grid(row=4, column=2, pady=2)

window.mainloop()
