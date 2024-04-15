import tkinter as tk


def increment():
    x = int(count_label["text"])
    x += 1
    count_label["text"] = str(x)


root = tk.Tk()
root.geometry("300x30")
root.title("Counter")
frame = tk.Frame(root)
frame.pack()
count_label = tk.Label(frame, text="0", width=10, background="white")
count_label.pack(side=tk.LEFT)
increment_button = tk.Button(frame, text="Count", width=10)
increment_button.pack(side=tk.RIGHT)
increment_button.config(command=increment)

root.eval("tk::PlaceWindow . center")
root.mainloop()
