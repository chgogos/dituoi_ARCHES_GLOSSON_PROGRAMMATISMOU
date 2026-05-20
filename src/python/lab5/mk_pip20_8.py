import tkinter as tk

class CounterApp:
    def __init__(self):
        self.count = 0

        self.window = tk.Tk()
        self.count_btn = tk.Button(
            master=self.window,
            text=str(self.count),
            command=self.increment_count
        )
        self.count_btn.pack()

    def increment_count(self):
        self.count += 1
        self.count_btn.config(text=str(self.count))

    def run(self):
        self.window.mainloop()

counter = CounterApp()
counter.run()