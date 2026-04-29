import tkinter as tk

window = tk.Tk()

hello_label = tk.Label(master=window, text="Hello!")
hello_label.pack()
hello_label.config(text="Hi!")

window.mainloop()