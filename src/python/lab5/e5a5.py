import tkinter as tk


def increment():
    x = int(count_label["text"])
    x += 1
    count_label["text"] = str(x)


root = tk.Tk()
root.geometry("200x30")
root.title("Counter")
count_label = tk.Label(root, text="0", width=10, background="white")
count_label.pack(side=tk.LEFT)
increment_button = tk.Button(root, text="Count", width=10)
increment_button.pack(side=tk.RIGHT)
increment_button.config(command=increment)

root.eval("tk::PlaceWindow . center")
root.mainloop()
