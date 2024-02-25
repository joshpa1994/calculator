import tkinter as tk
import tkinter.messagebox
from tkinter.constants import GROOVE
from tkinter.constants import FLAT
import math

window = tk.TK()
window.title('Scientific Calculator')
frame = tk.Frame(master=window, bg=" powder blue ", padx=10)
frame.pack()
entry = tk.entry(master=frame, relief=GROOVE, borderwidth=4, widht=40)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


def myinput(number):
    entry.insert(tk.end, number)


def equal():
    try:
        z = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, z)
    except:
        tkinter.messagebox.showinfo("error", "syntax error")


def clear():
    entry.delete(0, tk.END)


def sqrt():
    try:
        z = str(math.sqrt(float(entry.get)))
        entry.delete(0, tk.END)
        entry.insert(0, z)
    except:
        tkinter.messagebox.showinfo(" value error", "check your entered value")


def sin_func():
    try:
        ans=float(entry.get())
        ans=math.sin(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
            tkinter.messagebox.showinfo(" value error", "check your entered value")


def cos_func():
    try:
        ans=float(entry.get())
        ans=math.cos(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
            tkinter.messagebox.showinfo(" value error", "check your entered value")



def sin_func():
    try:
        ans=float(entry.get())
        ans=math.tan(math.radians(ans))
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))
    except Exception:
            tkinter.messagebox.showinfo(" value error", "check your entered value")





