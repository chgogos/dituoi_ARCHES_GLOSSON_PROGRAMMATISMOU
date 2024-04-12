import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

class Contact:
    def __init__(self, owner_name, owner_lastname, owner_phone):
        self.name = owner_name.strip()
        self.lastname = owner_lastname.strip()
        self.phone = owner_phone.strip()

    def __eq__(self, oth_phone):
        return self.phone == oth_phone

    def __str__(self):
        return f"{self.name},{self.lastname},{self.phone}"


class Phonebook:
    file_db = os.path.join("", "data.csv")

    def __init__(self):
        self.contacts = []
        if not os.path.exists(Phonebook.file_db):
            return
        with open(Phonebook.file_db, "r") as RF:
            for i, line in enumerate(RF):
                if i == 0:
                    continue
                owner_name, owner_lastname, owner_phone = line.split(",")
                owner_name = owner_name.replace('"', "")
                owner_lastname = owner_lastname.replace('"', "")
                owner_phone = owner_phone.replace('"', "")
                self.contacts.append(Contact(owner_name, owner_lastname, owner_phone))

    def insert(self, new_name, new_lastname, new_phone):
        if new_phone in self.contacts:
            return False
        self.contacts.append(Contact(new_name, new_lastname, new_phone))
        return True

    def update_contact(
        self, old_phone, new_name=None, new_lastname=None, new_phone=None
    ):
        i = self.contacts.index(old_phone)
        if new_name != None:
            self.contacts[i].name = new_name
        if new_lastname != None:
            self.contacts[i].lastname = new_lastname
        if new_phone != None:
            self.contacts[i].phone = new_phone

    def contacts_exist(self, phone):
        return phone in self.contacts

    def delete(self, phone_entry):
        self.contacts.remove(self.contacts[self.contacts.index(phone_entry)])

    def save(self):
        with open(Phonebook.file_db, "w") as WF:
            for col in ["NAME", "LASTNAME", "PHONE"]:
                WF.write(f"{col},")
            WF.write("\n")
            for contact in self.contacts:
                WF.write(f"{str(contact)}\n")

    def load_dummy(self):
        with open(os.path.join("", "dummy.csv"), "r") as RF:
            for i, line in enumerate(RF):
                if i == 0:
                    continue
                name, lastname, phone = line.split(",")
                self.contacts.append(Contact(name, lastname, phone))


class App(tk.Tk):
    def insertFrame(self):
        self.insFrame = tk.Frame(self)
        self.insFrame.columnconfigure(3)
        self.insFrame.rowconfigure(4)
        fg = "#120d33"
        name_label = tk.Label(
            self.insFrame, text="CONTACT NAME", justify="center", font="calibri 14 bold"
        )
        lastname_label = tk.Label(
            self.insFrame,
            text="CONTACT LASTNAME",
            justify="center",
            font="calibri 14 bold",
        )
        phone_label = tk.Label(
            self.insFrame,
            text="CONTACT PHONE",
            justify="center",
            font="calibri 14 bold",
        )

        self.name = tk.Entry(
            self.insFrame,
            text="Contact Name",
            justify="center",
            fg=fg,
            font="Calibri 12 bold",
            width=20,
        )
        self.lastname = tk.Entry(
            self.insFrame,
            text="Contact Lastname",
            justify="center",
            font="Calibri 12 bold",
            fg=fg,
            width=20,
        )
        self.phone = tk.Entry(
            self.insFrame,
            text="Contact Phone",
            justify="center",
            font="Calibri 12 bold",
            fg=fg,
            width=20,
        )

        px = 140
        name_label.grid(row=0, column=0, padx=(px, 10), pady=(2, 10))
        self.name.grid(row=0, column=1, pady=(2, 10))

        lastname_label.grid(row=1, column=0, padx=(px, 10), pady=10)
        self.lastname.grid(row=1, column=1, pady=(1, 10))

        phone_label.grid(row=2, column=0, padx=(px, 10), pady=10)
        self.phone.grid(row=2, column=1, pady=(1, 10))

        b1 = tk.Button(
            self.insFrame,
            text="INSERT",
            foreground="#f7f9fa",
            background="#691f70",
            font="Calibri 12 bold",
            width=15,
            command=self.insert_contact,
        )
        b2 = tk.Button(
            self.insFrame,
            text="CLEAR",
            foreground="#f7f9fa",
            background="#691f70",
            font="Calibri 12 bold",
            width=15,
            command=self.clear_contact,
        )
        b1.grid(row=3, column=0, padx=(px, 10), pady=(3, 40))
        b2.grid(row=3, column=1, padx=(4, 10), pady=(3, 40))

    def updateFrame(self):
        self.updFrame = tk.Frame(self)
        self.insFrame.columnconfigure(3)
        self.insFrame.rowconfigure(4)

        name_label = tk.Label(
            self.updFrame, text="CONTACT NAME", justify="center", font="calibri 14 bold"
        )
        lastname_label = tk.Label(
            self.updFrame,
            text="CONTACT LASTNAME",
            justify="center",
            font="calibri 14 bold",
        )
        phone_label = tk.Label(
            self.updFrame,
            text="CONTACT PHONE",
            justify="center",
            font="calibri 14 bold",
        )

        self.uname = tk.Entry(
            self.updFrame,
            text="Contact Name",
            justify="center",
            font="Calibri 12 bold",
            width=20,
        )
        self.ulastname = tk.Entry(
            self.updFrame,
            text="Contact Lastname",
            justify="center",
            font="Calibri 12 bold",
            width=20,
        )
        self.uphone = tk.Entry(
            self.updFrame,
            text="Contact Phone",
            justify="center",
            font="Calibri 12 bold",
            width=20,
        )

        px = 140
        name_label.grid(row=0, column=0, padx=(px, 10), pady=(2, 10))
        self.uname.grid(row=0, column=1, pady=(2, 10))

        lastname_label.grid(row=1, column=0, padx=(px, 10), pady=10)
        self.ulastname.grid(row=1, column=1, pady=(1, 10))

        phone_label.grid(row=2, column=0, padx=(px, 10), pady=10)
        self.uphone.grid(row=2, column=1, pady=(1, 10))

        b1 = tk.Button(
            self.updFrame,
            text="UPDATE",
            foreground="#f7f9fa",
            background="#691f70",
            font="Calibri 12 bold",
            width=15,
            command=self.update_contact,
        )
        b2 = tk.Button(
            self.updFrame,
            text="CLEAR",
            foreground="#f7f9fa",
            background="#691f70",
            font="Calibri 12 bold",
            width=15,
            command=self.clear_contact,
        )
        b1.grid(row=3, column=0, padx=(px, 10), pady=(3, 5))
        b2.grid(row=3, column=1, padx=(4, 10), pady=(3, 5))

    def deleteFrame(self):
        self.delFrame = tk.Frame(self)

        descLabel = tk.Label(
            self.delFrame,
            background="#6e206b",
            fg="white",
            font="calibri 14 bold",
            justify="center",
            text="Select a record from the table and then press DEL",
        )
        descLabel.grid(row=2, column=1, columnspan=3, padx=140, pady=(50, 0))

    def selectionFrame(self):
        selectorFrame = tk.Frame(self)
        self.selected_var = tk.IntVar()

        b1 = tk.Radiobutton(
            selectorFrame,
            text="",
            font="calibri 20 bold",
            fg="white",
            selectcolor="white",
            variable=self.selected_var,
            value=1,
            command=self.change_frame,
        )

        b2 = tk.Radiobutton(
            selectorFrame,
            text="",
            font="calibri 20 bold",
            fg="white",
            selectcolor="white",
            variable=self.selected_var,
            value=2,
            command=self.change_frame,
        )

        b3 = tk.Radiobutton(
            selectorFrame,
            text="",
            font="calibri 20 bold",
            fg="white",
            selectcolor="white",
            variable=self.selected_var,
            value=3,
            command=self.change_frame,
        )

        b1.grid(row=1, column=0, padx=(20, 0), pady=(0, 40))
        b2.grid(row=1, column=1, padx=(1, 1), pady=(0, 40))
        b3.grid(row=1, column=2, padx=(1, 20), pady=(0, 40))

        self.change_frame()

        selectorFrame.grid(row=1, column=1)

    def create_table(self, srow=0):
        table_frame = tk.Frame(self)
        table_scroll1 = tk.Scrollbar(table_frame)
        table_scroll1.pack(side=tk.RIGHT, fill=tk.Y)

        table_scroll = tk.Scrollbar(table_frame, orient="horizontal")
        table_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.contacts_book = ttk.Treeview(
            table_frame,
            yscrollcommand=table_scroll1.set,
            xscrollcommand=table_scroll.set,
        )

        table_scroll.config(command=self.contacts_book.xview)
        table_scroll1.config(command=self.contacts_book.yview)

        self.contacts_book["columns"] = (
            "contact_name",
            "contact_lastname",
            "contact_phone",
        )

        # format our column
        self.contacts_book.column("#0", width=0, stretch=tk.NO)
        self.contacts_book.column(
            "contact_name", anchor=tk.CENTER, width=int(self.width * 0.9 / 3)
        )
        self.contacts_book.column(
            "contact_lastname", anchor=tk.CENTER, width=int(self.width * 0.9 / 3)
        )
        self.contacts_book.column(
            "contact_phone", anchor=tk.CENTER, width=int(self.width * 0.9 / 3)
        )

        # Create Headings
        self.contacts_book.heading("#0", text="", anchor=tk.CENTER)
        self.contacts_book.heading(
            "contact_name", text="CONTACT NAME", anchor=tk.CENTER
        )
        self.contacts_book.heading(
            "contact_lastname", text="CONTACT LASTNAME", anchor=tk.CENTER
        )
        self.contacts_book.heading(
            "contact_phone", text="CONTACT PHONE", anchor=tk.CENTER
        )

        style = ttk.Style(self.contacts_book)
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading",
            background="black",
            foreground="white",
            font="Calibri 13 bold",
        )

        self.contacts_book.pack(padx=(30, 0))

        for contact in self.phonebook.contacts:
            self.contacts_book.insert(
                parent="",
                index="end",
                text="",
                values=(contact.name, contact.lastname, contact.phone),
            )

        table_frame.grid(row=srow, column=0, columnspan=3)

        self.contacts_book.bind("<Double-1>", self.doubleclickevent)
        self.contacts_book.bind("<Delete>", self.deleteev)

    def renew_table(self):
        for item in self.contacts_book.get_children():
            self.contacts_book.delete(item)

        for contact in self.phonebook.contacts:
            self.contacts_book.insert(
                parent="",
                index="end",
                values=(contact.name, contact.lastname, contact.phone),
            )

    def __init__(self):
        self.phonebook = Phonebook()
        # self.phonebook.load_dummy()
        self.phone_to_be_updated = None
        super().__init__()
        self.geometry("700x700")
        self.title("Contacts Book")
        self.columnconfigure(3)
        self.update()
        self.resizable(False, False)
        self.width, self.height = self.winfo_width(), self.winfo_height()
        self.insertFrame()
        self.updateFrame()
        self.deleteFrame()

        self.frames = {1: self.insFrame, 2: self.updFrame, 3: self.delFrame}
        for _, f in self.frames.items():
            f.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.selectionFrame()
        self.create_table(srow=3)

    def __del__(self):
        self.phonebook.save()

    def change_frame(self):
        current_frame = self.selected_var.get()
        if current_frame == 0:
            current_frame = 1
        frame = self.frames[current_frame]
        frame.tkraise()

    def insert_contact(self):
        if (
            len(self.name.get()) == 0
            or len(self.lastname.get()) == 0
            or len(self.phone.get()) == 0
        ):
            showerror(
                title="Error on blank filling", message="Please fill all the blanks"
            )
            return

        if len(self.phone.get()) == 0:
            showerror(
                title="Phone invalid format",
                message=f"Phone {self.phone.get()} is not in valid",
            )
            return
        if self.phonebook.contacts_exist(self.phone.get()):
            showinfo(
                title="Phone exists in Phonebbok",
                message=f"{str(self.phonebook.contacts[self.phonebook.contacts.index(self.phone.get())])}",
            )
            return

        self.phonebook.insert(self.name.get(), self.lastname.get(), self.phone.get())

        self.contacts_book.insert(
            parent="",
            index="end",
            text="",
            values=(self.name.get(), self.lastname.get(), self.phone.get()),
        )
        self.renew_table()

    def update_contact(self):
        if self.phone_to_be_updated == None:
            showerror(
                title="Error on Selection",
                message="You did not select a phone to update",
            )
            return
        self.phonebook.update_contact(
            self.phone_to_be_updated,
            self.uname.get(),
            self.ulastname.get(),
            self.uphone.get(),
        )
        self.renew_table()

    def clear_contact(self):
        if self.selected_var.get() == 1 or self.selected_var.get() == 0:
            self.name.delete(0, "end")
            self.lastname.delete(0, "end")
            self.phone.delete(0, "end")
        elif self.selected_var.get() == 2:
            self.uname.delete(0, "end")
            self.ulastname.delete(0, "end")
            self.uphone.delete(0, "end")

    def doubleclickevent(self, event):
        item = self.contacts_book.identify("item", event.x, event.y)
        if self.selected_var.get() == 2:
            name, lastname, phone = (
                self.contacts_book.item(item, "values")[0],
                self.contacts_book.item(item, "values")[1],
                self.contacts_book.item(item, "values")[2],
            )
            self.phone_to_be_updated = phone
            self.uname.delete(0, "end")
            self.uname.insert(0, name)

            self.ulastname.delete(0, "end")
            self.ulastname.insert(0, lastname)

            self.uphone.delete(0, "end")
            self.uphone.insert(0, phone)
        else:
            self.phone_to_be_updated = None

    def deleteev(self, event):
        curItem = self.contacts_book.focus()
        phone = str(self.contacts_book.item(curItem)["values"][2])
        self.phonebook.delete(phone)
        self.renew_table()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    del app
