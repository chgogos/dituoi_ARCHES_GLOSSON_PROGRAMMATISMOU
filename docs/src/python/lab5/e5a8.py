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

        self.d_time = 10
        self.elapsed_ms = 0
        self.timer_id = None
        self.d_slider = ttk.Scale(
            self, from_=0, to=100, orient="horizontal", command=self.slider_update
        )
        self.d_slider.set(10)
        self.d_slider.grid(row=2, column=1, sticky="nswe", padx=10)

        self.reset_button = ttk.Button(self, text="Reset", command=self.reset)
        self.reset_button.grid(
            row=3, column=0, columnspan=2, sticky="nswe", padx=10, pady=10
        )

        self.start_timer()

    def start_timer(self):
        self.update_timer()

    def update_timer(self):
        self.et_time["text"] = (
            "{:.1f}".format(self.elapsed_ms / 1000) + "s"
        )  # Display elapsed time with one decimal place

        diff = self.d_time - (self.elapsed_ms / 1000)

        if not (self.elapsed_ms / 1000) >= self.d_time:
            self.progress_bar["value"] = (
                ((self.d_time - diff) / self.d_time) * 100 if self.d_time else 0
            )
            # Update the timer every 1ms
            self.elapsed_ms += 1
            self.timer_id = self.after(1, self.update_timer)
        else:
            self.progress_bar["value"] = 100

    def reset(self):
        self.elapsed_ms = 0
        self.after_cancel(self.timer_id)
        self.start_timer()

    def slider_update(self, value):
        self.d_time = float(value)
        if self.d_time > self.elapsed_ms / 1000 and self.progress_bar["value"] == 100:
            self.start_timer()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
