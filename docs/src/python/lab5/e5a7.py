# Λύση από τον φοιτητή Μπακογιάννη Θωμά
# του Τμήματος Πληροφορικής και Τηλεπικοινωνιών
# του Πανεπιστημίου Ιωαννίνων τον Απρίλιο του 2024

import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up main window
        self.title("Book Flight")
        self.geometry("300x150")
        for x in range(4):
            self.rowconfigure(x, weight=1)
        self.columnconfigure(0, weight=1)

        # Set up combo box
        options = ["one-way flight", "return flight"]
        self.flight_options = ttk.Combobox(self, values=options, state="readonly")
        self.flight_options.set("one-way flight")
        self.flight_options.bind("<<ComboboxSelected>>", self.on_combobox_select)
        self.flight_options.grid(row=0, sticky="nesw", padx=3, pady=3)

        # Set up start date entry
        self.entry_val1 = tk.StringVar()
        self.entry_val1.trace_add("write", self.validate_date)
        self.start_date = tk.Entry(self, textvariable=self.entry_val1)
        self.start_date.grid(row=1, sticky="nesw", padx=3, pady=3)

        # Set up return date entry
        self.entry_val2 = tk.StringVar()
        self.entry_val2.trace_add("write", self.validate_date)
        self.return_date = tk.Entry(self, textvariable=self.entry_val2)
        self.return_date["state"] = "disabled"
        self.return_date.grid(row=2, sticky="nesw", padx=3, pady=3)

        # Set up book button
        self.book_button = ttk.Button(
            self, text="Book", command=self.display_message, state="disabled"
        )
        self.book_button.grid(row=3, sticky="nesw", padx=3, pady=3)

    def check_box1(self):
        try:
            datetime.strptime(self.start_date.get(), "%d.%m.%Y")
            self.start_date["bg"] = "white"
            self.book_button["state"] = "normal"
            return True
        except ValueError:
            self.start_date["bg"] = "red"
            return False

    def check_box2(self):
        try:
            datetime.strptime(self.return_date.get(), "%d.%m.%Y")
            self.return_date["bg"] = "white"
            return True
        except ValueError:
            self.return_date["bg"] = "red"
            return False

    def on_combobox_select(self, event):
        # Extra checks for boxes
        if self.flight_options.get() == "one-way flight":
            self.return_date["state"] = "disabled"
            if self.check_box1():
                self.book_button["state"] = "normal"
            else:
                self.book_button["state"] = "disabled"
        else:
            self.return_date["state"] = "normal"
            if self.check_box1() and self.check_box2():
                self.book_button["state"] = "normal"
            else:
                self.book_button["state"] = "disabled"

    def validate_date(self, *args):
        focused_widget = self.focus_get()

        # Validate date entries
        if focused_widget in [self.start_date, self.return_date]:
            if not focused_widget.get():
                self.book_button["state"] = "disabled"
            else:
                try:
                    datetime.strptime(focused_widget.get(), "%d.%m.%Y")
                    focused_widget["bg"] = "white"
                    self.book_button["state"] = "normal"
                except ValueError:
                    focused_widget["bg"] = "red"
                    self.book_button["state"] = "disabled"

        # Compare dates if return flight is selected
        if self.flight_options.get() == "return flight":
            self.compare_dates()

    def compare_dates(self):
        date_str1 = self.start_date.get()
        date_str2 = self.return_date.get()

        # Compare start and return dates
        try:
            date1 = datetime.strptime(date_str1, "%d.%m.%Y")
            date2 = datetime.strptime(date_str2, "%d.%m.%Y")
            if date2 < date1:
                self.book_button["state"] = "disabled"
            else:
                self.book_button["state"] = "normal"
        except ValueError:
            self.book_button["state"] = "disabled"

    def display_message(self):
        # Display booking information
        if self.flight_options.get() == "one-way flight":
            messagebox.showinfo(
                "Booking information",
                f"You have booked a one-way flight for {self.start_date.get()}",
            )
        else:
            messagebox.showinfo(
                "Booking information",
                f"You have booked a return flight departing on {self.start_date.get()} and returning on {self.return_date.get()}",
            )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
