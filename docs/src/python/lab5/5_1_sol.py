import tkinter as tk
from tkinter import ttk  # themed widgets
from tkinter.messagebox import showwarning

root = tk.Tk()
root.title("Λίστα εργασιών")
tasks = tk.Variable(value=[])


def add_task():
    task = entry_task.get()
    if task == "":
        showwarning(title="Σφάλμα!", message="Θα πρέπει να εισάγετε μια εργασία")
    elif task in tasks.get():
        showwarning(title="Σφάλμα!", message="H εργασία ήδη υπάρχει στη λίστα")
    else:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        showwarning(title="Σφάλμα!", message="Θα πρέπει να επιλέξετε μια εργασία")


# Δημιουργία GUI
# Frame για το listbox και το scrollbar
frame_tasks = ttk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, listvariable=tasks)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = ttk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# σύνδεση listbox με scrollbar
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = ttk.Entry(root, width=50)
entry_task.pack(fill="x", expand=True)

button_add_task = ttk.Button(root, text="Νέα εργασία", width=45)
button_add_task["command"] = add_task
button_add_task.pack(fill="x", expand=True)

button_delete_task = ttk.Button(
    root, text="Διαγραφή εργασίας", width=45, command=delete_task
)
button_delete_task.pack(fill="x", expand=True)


root.mainloop()
