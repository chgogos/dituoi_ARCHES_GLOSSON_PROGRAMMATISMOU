import tkinter as tk

window = tk.Tk()

message_label = tk.Label(master=window, text="")
message_label.pack()


def display_message():
    message_label.config(text="Hello!")


hello_button = tk.Button(master=window, text="Say Hello!", command=display_message)
hello_button.pack()

window.mainloop()
