# Λύση από τον φοιτητή Μπακογιάννη Θωμά
# του Τμήματος Πληροφορικής και Τηλεπικοινωνιών
# του Πανεπιστημίου Ιωαννίνων τον Απρίλιο του 2024

import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up mainwindow
        self.title("Timer")
        self.geometry("300x150")
        for x in range(4):
            self.grid_rowconfigure(x, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.et_label = ttk.Label(self, text="Elapsed Time:")
        self.et_label.grid(row=0, column=0)

        self.et_time = ttk.Label(self, text="0")
        self.et_time.grid(row=1, column=0)

        self.progress_bar = ttk.Progressbar(
            self, orient="horizontal", length=200, mode="determinate"
        )
        self.progress_bar.grid(row=0, column=1, padx=3, pady=10)

        self.d_label = ttk.Label(self, text="Duration:")
        self.d_label.grid(row=2, column=0)

        self.d_time = 0
        self.d_slider = ttk.Scale(
            self, from_=0, to=100, orient="horizontal", command=self.update_time
        )
        self.d_slider.grid(row=2, column=1, sticky="nswe", padx=10)

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset)
        self.reset_button.grid(
            row=3, column=0, columnspan=2, sticky="nswe", padx=10, pady=10
        )

        self.timer()

    def update_time(self, value):
        self.d_time = float(value)

    def timer(self):
        # Update the elapsed time label
        elapsed_time = int(self.et_time["text"]) + 1
        self.et_time["text"] = str(elapsed_time)

        diff = self.d_time - elapsed_time

        # Update the progress bar
        if not elapsed_time >= self.d_time:
            if diff >= 0:
                self.progress_bar["value"] = (
                    ((self.d_time - diff) / self.d_time) * 100 if self.d_time else 0
                )
            else:
                self.progress_bar["value"] = 0

            # Call the timer function again after 1 second
            self.after(1000, self.timer)

    def reset(self):
        self.et_time["text"] = "0"
        self.progress_bar["value"] = 0
        self.timer()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
