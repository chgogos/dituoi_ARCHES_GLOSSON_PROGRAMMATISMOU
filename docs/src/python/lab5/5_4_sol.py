import sys
import tkinter as tk
from tkinter import messagebox


class Complex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    # Υπερφόρτωση τελεστών για πράξεις μιγαδικών αριθμών
    def __add__(self, other_complex: "Complex"):
        real_new = self.real + other_complex.real
        imag_new = self.imag + other_complex.imag
        return Complex(real_new, imag_new)

    def __sub__(self, other_complex: "Complex"):
        real_new = self.real - other_complex.real
        imag_new = self.imag - other_complex.imag
        return Complex(real_new, imag_new)

    def __mul__(self, other_complex: "Complex"):
        real_new = self.real * other_complex.real - self.imag * other_complex.imag
        imag_new = self.imag * other_complex.real + self.real * other_complex.imag
        return Complex(real_new, imag_new)

    def __truediv__(self, other_complex: "Complex"):
        temp_real = self.real * other_complex.real + self.imag * other_complex.imag
        temp_imag = other_complex.real * self.imag - self.real * other_complex.imag
        denum = other_complex.real**2 + other_complex.imag**2
        real_new = temp_real / denum
        imag_new = temp_imag / denum
        return Complex(real_new, imag_new)

    def __str__(self):
        return f"({self.real}, {self.imag}i)"


class ViewGui(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # 1η γραμμή -> Εισαγωγή πρώτου μιγαδικού αριθμού
        self.real1_label = tk.Label(self, text="Real 1: ")
        self.real1_label.grid(row=0, column=0)
        self.real1_var = tk.DoubleVar()
        self.real1_entry = tk.Entry(self, textvariable=self.real1_var, justify="right")
        self.real1_entry.grid(row=0, column=1)
        self.imag1_label = tk.Label(self, text="Imaginary 1: ")
        self.imag1_label.grid(row=0, column=2)
        self.imag1_var = tk.DoubleVar()
        self.imag1_entry = tk.Entry(self, textvariable=self.imag1_var, justify="right")
        self.imag1_entry.grid(row=0, column=3)

        # 2η γραμμή -> Εισαγωγή δεύτερου μιγαδικού αριθμού
        self.real2_label = tk.Label(self, text="Real 2: ")
        self.real2_label.grid(row=1, column=0)
        self.real2_var = tk.DoubleVar()
        self.real2_entry = tk.Entry(self, textvariable=self.real2_var, justify="right")
        self.real2_entry.grid(row=1, column=1)
        self.imag2_label = tk.Label(self, text="Imaginary 2: ")
        self.imag2_label.grid(row=1, column=2)
        self.imag2_var = tk.DoubleVar()
        self.imag2_entry = tk.Entry(self, textvariable=self.imag2_var, justify="right")
        self.imag2_entry.grid(row=1, column=3)

        # 3η γραμμή -> Κουμπιά εκτέλεσης πράξεων μιγαδικών αριθμών
        self.add_button = tk.Button(self, text="Add", command=self.add_clicked)
        self.add_button.grid(row=2, column=0, sticky=tk.W)
        self.substract_button = tk.Button(
            self, text="Substract", command=self.substract_clicked
        )
        self.substract_button.grid(row=2, column=1, sticky=tk.W)
        self.multiply_button = tk.Button(
            self, text="Multiply", command=self.multiply_clicked
        )
        self.multiply_button.grid(row=2, column=2, sticky=tk.W)
        self.divide_button = tk.Button(self, text="Divide", command=self.divide_clicked)
        self.divide_button.grid(row=2, column=3, sticky=tk.W)

        # 4η γραμμή -> Εμφάνιση αποτελέσματος πράξης μιγαδικών αριθμών
        self.real_result_label = tk.Label(self, text="")
        self.real_result_label.grid(row=3, column=0)
        self.imag_result_label = tk.Label(self, text="")
        self.imag_result_label.grid(row=3, column=1)

        self.controller = None

    # Συνάρτηση ορισμού controller
    def set_controller(self, controller):
        self.controller = controller

    # Συνάρτηση χειρισμού εισαγωγών
    def handle_input_event(self):
        self.complex1 = Complex(
            float(self.real1_entry.get()), float(self.imag1_entry.get())
        )
        self.complex2 = Complex(
            float(self.real2_entry.get()), float(self.imag2_entry.get())
        )

    # Συνάρτηση ενημέρωσης label αποτελέσματος μιγαδικού αριθμού
    def show_result(self, complex_result: Complex):
        # Μορφοποίηση αποτελέσματος για εμφάνιση 2 δεκαδικών ψηφίων
        complex_result.real = "{:.3f}".format(complex_result.real)
        complex_result.imag = "{:.3f}".format(complex_result.imag)
        # Ανανέωση label για εμφάνιση αποτελέσματος
        self.real_result_label["text"] = "Real Result: {}".format(
            str(complex_result.real)
        )
        self.imag_result_label["text"] = "Imaginary Result: {}".format(
            str(complex_result.imag)
        )

    # Συναρτήσεις χειρισμού event πράξεων μιγαδικών αριθμών
    def add_clicked(self):
        self.handle_input_event()
        if self.controller:
            self.controller.add(self.complex1, self.complex2)

    def substract_clicked(self):
        self.handle_input_event()
        if self.controller:
            self.controller.substract(self.complex1, self.complex2)

    def multiply_clicked(self):
        self.handle_input_event()
        if self.controller:
            self.controller.multiply(self.complex1, self.complex2)

    def divide_clicked(self):
        self.handle_input_event()
        if self.controller:
            self.controller.divide(self.complex1, self.complex2)


class ViewTui:
    def __init__(self):
        print("~" * 82)
        print("~" * 30 + "  Complex Calculator  " + "~" * 30)
        print("~" * 82 + "\n")

        print("Choose operation::")
        self.operation_selection = int(
            input("1.Addition  2.Substraction  3.Multiplication  4.Division \n5.Quit\n")
        )

        self.controller = Controller(Complex(1, 2), self)

        if self.operation_selection == 1:
            # check which function needs to be called
            self.add_clicked()
        elif self.operation_selection == 2:
            self.substract_clicked()
        elif self.operation_selection == 3:
            self.multiply_clicked()
        elif self.operation_selection == 4:
            self.divide_clicked()
        elif self.operation_selection == 5:
            print("Quitting ...")
        else:
            print("Wrong Input!!!")

    # Συνάρτηση χειρισμού εισαγωγής μιγαδικών αριθμών
    def handle_input_event(self):
        print("Input of 1st complex number:")
        print("Give real part of 1st complex number: ")
        self.real1 = float(input())
        print("Give imaginary part of 1st complex number: ")
        self.imag1 = float(input())

        print("Input of 2nd complex number:")
        print("Give real part of 2nd complex number: ")
        self.real2 = float(input())
        print("Give imaginary part of 2nd complex number: ")
        self.imag2 = float(input())

    def handle_modelling_stage(self):
        self.complex1 = Complex(self.real1, self.imag1)
        self.complex2 = Complex(self.real2, self.imag2)

    def show_result(self, complex_result: Complex):
        print(
            "Real Result: {:.3f}, Imaginary Result: {:.3f}".format(
                complex_result.real, complex_result.imag
            )
        )

    # Συναρτήσεις χειρισμού event πράξεων μιγαδικών αριθμών
    def add_clicked(self):
        self.handle_input_event()
        self.handle_modelling_stage()
        self.controller.add(self.complex1, self.complex2)

    def substract_clicked(self):
        self.handle_input_event()
        self.handle_modelling_stage()
        self.controller.substract(self.complex1, self.complex2)

    def multiply_clicked(self):
        self.handle_input_event()
        self.handle_modelling_stage()

        self.controller.multiply(self.complex1, self.complex2)

    def divide_clicked(self):
        self.handle_input_event()
        self.handle_modelling_stage()

        self.controller.divide(self.complex1, self.complex2)


class Controller:
    def __init__(self, model: Complex = None, view=None):
        self.model = model
        self.view = view

    # Συναρτήσεις εκτέλεσης πράξεων μιγαδικών αριθμών
    def add(self, complex1: Complex, complex2: Complex):
        self.model = complex1
        complex_result = self.model + complex2
        self.view.show_result(complex_result)

    def substract(self, complex1: Complex, complex2: Complex):
        self.model = complex1
        complex_result = self.model - complex2
        self.view.show_result(complex_result)

    def multiply(self, complex1: Complex, complex2: Complex):
        self.model = complex1
        complex_result = self.model * complex2
        self.view.show_result(complex_result)

    def divide(self, complex1: Complex, complex2: Complex):
        self.model = complex1

        # try catch, για GUI διεπαφή
        if sys.argv[1].upper() == "GUI":
            try:
                complex_result = self.model / complex2
                self.view.show_result(complex_result)
            except ZeroDivisionError:
                messagebox.showwarning(
                    title="Division Error",
                    message=" Can't divide by zero!!! \n Please input valid numbers!",
                )

        # try catch, για TUI διεπαφή
        if sys.argv[1].upper() == "TUI":
            try:
                complex_result = self.model / complex2
                self.view.show_result(complex_result)
            except ZeroDivisionError:
                print(" Can't divide by zero!!! \n Please input valid numbers!")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Complex Calculator")
        # Δημιουργία μοντέλου
        model = Complex(1, 2)
        # Δημιουργία γραφικού περιβάλλοντος και τοποθέτηση στην οθόνη
        view_gui = ViewGui(self)
        view_gui.grid(row=0, column=0, padx=10, pady=10)
        # Δημιουργία controller
        controller_gui = Controller(model, view_gui)
        # Ορισμός του controller στο γραφικό περιβάλλον
        view_gui.set_controller(controller_gui)


if __name__ == "__main__":
    # try catch block, για αποφυγή IndexError exception, αν ο χρήστης δεν εισάγει τύπο διεπαφής
    try:
        if sys.argv[1].upper() == "GUI":
            app = App()
            app.mainloop()
        elif sys.argv[1].upper() == "TUI":
            while True:
                view = ViewTui()
                if view.operation_selection == 5:
                    break

        # Δημιουργία exception αν ο χρήστης εισάγει λάθος τύπο διεπαφής
        if sys.argv[1].upper() not in ["GUI", "TUI"]:
            raise Exception("Wrong interface command line parameter")
    except IndexError:
        print("Input interface type, as command line parameter")
