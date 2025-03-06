import random
import tkinter as tk
from tkinter.messagebox import showinfo

from utils import distance_percentage

# επιλογή τυχαίου χρώματος για το frame
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
a_color = f"#{r:02x}{g:02x}{b:02x}"

tries = 0
nearest_color = None
min_distance = None


def check_color():
    global tries, nearest_color, min_distance
    user_red = int(red_scale.get())
    user_green = int(green_scale.get())
    user_blue = int(blue_scale.get())
    user_color = f"#{user_red:02x}{user_green:02x}{user_blue:02x}"
    user_color_frame.config(bg=user_color)
    user_color_label["text"] = f"{(user_red, user_green, user_blue)}"
    p = distance_percentage((r, g, b), (user_red, user_green, user_blue))
    if nearest_color is None:
        nearest_color = (user_red, user_green, user_blue)
        min_distance = p
    else:
        if p < min_distance:
            nearest_color = (user_red, user_green, user_blue)
            min_distance = p
    tries += 1
    if min_distance < 0.1 and tries <= 5:
        showinfo(
            "Επιτυχία",
            msg="Το χρώμα που επιλέξατε είναι πολύ κοντά (< 10%) στο χρώμα που αναζητούταν!",
        )
    msg = f" προσπάθεια {tries}/5, καλύτερο σκορ {min_distance*100:.4}% {nearest_color}"
    count_lbl.config(text=msg)
    if tries == 5:
        guess_color_label["text"] = f"{(r,g,b)}"


root = tk.Tk()
root.title("Συνδυασμός βασικών χρωμάτων")
top_frame = tk.Frame(root)
top_frame.pack()
middle_frame = tk.Frame(root)
middle_frame.pack()
bottom_frame = tk.Frame(root)
bottom_frame.pack()

red_label = tk.Label(top_frame, text="Κόκκινο")
red_label.grid(row=0, column=0)
red_scale = tk.Scale(top_frame, from_=0, to=255, orient=tk.HORIZONTAL)
red_scale.grid(row=0, column=1)

green_label = tk.Label(top_frame, text="Πράσινο")
green_label.grid(row=1, column=0)
green_scale = tk.Scale(top_frame, from_=0, to=255, orient=tk.HORIZONTAL)
green_scale.grid(row=1, column=1)

blue_label = tk.Label(top_frame, text="Μπλε")
blue_label.grid(row=2, column=0)
blue_scale = tk.Scale(top_frame, from_=0, to=255, orient=tk.HORIZONTAL)
blue_scale.grid(row=2, column=1)

test_btn = tk.Button(middle_frame, text="Δοκιμή")
count_lbl = tk.Label(middle_frame, text="προσπάθεια 0/5, καλύτερο σκορ = κανένα")
test_btn.grid(row=0, column=0)
count_lbl.grid(row=0, column=1)
test_btn.config(command=check_color)

guess_color_frame = tk.Frame(bottom_frame, width=385, height=460, background=a_color)
guess_color_frame.grid(row=0, column=0)
guess_color_label = tk.Label(bottom_frame, text="Χρώμα στόχος")
guess_color_label.grid(row=1, column=0)
user_color_frame = tk.Frame(bottom_frame, width=385, height=460, background="white")
user_color_frame.grid(row=0, column=1)
user_color_label = tk.Label(bottom_frame, text="255, 255, 255")
user_color_label.grid(row=1, column=1)

root.eval("tk::PlaceWindow . center")
root.mainloop()
