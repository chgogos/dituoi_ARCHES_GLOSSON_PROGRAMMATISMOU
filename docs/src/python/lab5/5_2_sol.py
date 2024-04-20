# Λύση από τον φοιτητή Ράντο Κωνσταντίνο
# του Τμήματος Πηροφορικής και Τηλεπικοινωνιών
# του Πανεπιστημίου Ιωαννίνων τον Απρίλιο του 2024

import csv
import tkinter as tk
from tkinter import messagebox, ttk


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Διαχείριση Επαφών")
        self.contacts = self.load_contacts()
        self.deleted_contacts = []
        self.create_widgets()
        self.root.eval("tk::PlaceWindow . center")

    def create_widgets(self):
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            tree_frame, columns=("lastname", "firstname", "phone"), show="headings"
        )
        self.tree.heading("lastname", text="Επώνυμο")
        self.tree.heading("firstname", text="Όνομα")
        self.tree.heading("phone", text="Τηλέφωνο")
        self.tree.column("lastname", width=120)
        self.tree.column("firstname", width=120)
        self.tree.column("phone", width=120)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            tree_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Button(btn_frame, text="Προσθήκη Επαφής", command=self.add_contact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(btn_frame, text="Επεξεργασία Επαφής", command=self.edit_contact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(btn_frame, text="Διαγραφή Επαφής", command=self.delete_contact).pack(
            side=tk.TOP, fill=tk.X
        )
        tk.Button(
            btn_frame, text="Ανάκτηση Επαφής", command=self.show_retrieve_dialog
        ).pack(side=tk.TOP, fill=tk.X)
        tk.Button(btn_frame, text="Αποθήκευση Επαφών", command=self.save_contacts).pack(
            side=tk.TOP, fill=tk.X
        )

        self.display_contacts()

    def load_contacts(self):
        try:
            with open("contacts.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                return [tuple(contact) for contact in reader]
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open("contacts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)
        messagebox.showinfo("Επιτυχία!", "Οι επαφές αποθηκεύτηκαν στο αρχείο.")

    def add_contact(self):
        self.create_dialog("Νέα Επαφή")

    def edit_contact(self):
        try:
            selected_item = self.tree.selection()[0]
            contact = self.tree.item(selected_item, "values")
            self.create_dialog("Επεξεργασία Επαφής", contact)
        except IndexError:
            messagebox.showerror("Σφάλμα!", "Δεν έχει επιλεγεί καμία επαφή")

    def create_dialog(self, title, contact=None):
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry(
            "+{}+{}".format(self.root.winfo_x() + 50, self.root.winfo_y() + 50)
        )
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.focus_set()

        tk.Label(dialog, text="Επώνυμο:").pack()
        last_name_entry = tk.Entry(dialog)
        last_name_entry.pack(fill=tk.X)
        last_name_entry.insert(0, contact[0] if contact else "")

        tk.Label(dialog, text="Όνομα:").pack()
        first_name_entry = tk.Entry(dialog)
        first_name_entry.pack(fill=tk.X)
        first_name_entry.insert(0, contact[1] if contact else "")

        tk.Label(dialog, text="Τηλέφωνο:").pack()
        phone_number_entry = tk.Entry(dialog)
        phone_number_entry.pack(fill=tk.X)
        phone_number_entry.insert(0, contact[2] if contact else "")

        def save_contact():
            last_name = last_name_entry.get()
            first_name = first_name_entry.get()
            phone_number = phone_number_entry.get()
            if last_name and first_name and phone_number:
                new_contact = (last_name, first_name, phone_number)
                if contact:
                    idx = self.contacts.index(contact)
                    self.contacts[idx] = new_contact
                else:
                    self.contacts.append(new_contact)
                self.display_contacts()
                dialog.destroy()
            else:
                messagebox.showerror(
                    "Σφάλμα!",
                    "Παρακαλώ εισάγετε όλες τις λεπτομέρειες της επαφής",
                    parent=dialog,
                )

        tk.Button(dialog, text="Αποθήκευση", command=save_contact).pack()

    def display_contacts(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for contact in self.contacts:
            self.tree.insert("", tk.END, values=contact)

    def delete_contact(self):
        try:
            selected_item = self.tree.selection()[0]
            contact = self.tree.item(selected_item, "values")
            self.deleted_contacts.append(contact)
            self.contacts.remove(contact)
            self.tree.delete(selected_item)
        except IndexError:
            messagebox.showerror("Σφάλμα!", "Δεν έχει επιλεγεί καμία επαφή")

    def show_retrieve_dialog(self):
        if not self.deleted_contacts:
            messagebox.showinfo(
                "Πληροφορία", "Δεν υπάρχουν διαγραμμένες επαφές για ανάκτηση"
            )
            return

        retrieve_window = tk.Toplevel(self.root)
        retrieve_window.title("Ανάκτηση Επαφής")
        retrieve_window.geometry("300x300+450+450")

        list_frame = tk.Frame(retrieve_window)
        list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(list_frame)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.configure(yscrollcommand=scrollbar.set)

        for idx, contact in enumerate(self.deleted_contacts):
            listbox.insert(tk.END, f"{idx+1}. {contact[0]} {contact[1]} - {contact[2]}")

        def retrieve_selected_contact():
            selected_idx = listbox.curselection()
            if selected_idx:
                selected_contact = self.deleted_contacts.pop(selected_idx[0])
                self.contacts.append(selected_contact)
                self.display_contacts()
                retrieve_window.destroy()
            else:
                messagebox.showerror("Προσοχή!", "Δεν έχετε επιλέξει καμία επαφή")

        retrieve_button = tk.Button(
            retrieve_window,
            text="Ανάκτηση Επιλεγμένης Επαφής",
            command=retrieve_selected_contact,
        )
        retrieve_button.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
