import tkinter as tk

root = tk.Tk()
celsius_var = tk.StringVar()
celsius_var.set("0.0")
fahr_var = tk.StringVar()
fahr_var.set("32.0")


def celcius_callback(*args):
    if root.focus_get() != celsius_entry:
        return
    try:
        celcius_temperature = celsius_var.get()
        c = float(celcius_temperature)
        f = c * (9 / 5) + 32
        celsius_entry.config(background="white")
        fahr_var.set(f"{f:.1f}")
    except ValueError:
        celsius_entry.config(background="pink")


def fahr_callback(*args):
    if root.focus_get() != fahr_entry:
        return
    try:
        fahr_temperature = fahr_var.get()
        f = float(fahr_temperature)
        c = (f - 32) * 5 / 9
        fahr_entry.config(background="white")
        celsius_var.set(f"{c:.1f}")
    except ValueError:
        fahr_entry.config(background="pink")


root.geometry("350x30")
root.title("TempConv")

celsius_var.trace_add("write", celcius_callback)
fahr_var.trace_add("write", fahr_callback)
celsius_entry = tk.Entry(root, width=10, textvariable=celsius_var)
celsius_entry.grid(row=0, column=0)

label1 = tk.Label(root, text="Celsius = ")
label1.grid(row=0, column=1)
fahr_entry = tk.Entry(root, width=10, textvariable=fahr_var)
fahr_entry.grid(row=0, column=2)
label2 = tk.Label(root, text="Fahrenheit")
label2.grid(row=0, column=3)

root.eval("tk::PlaceWindow . center")
root.mainloop()
