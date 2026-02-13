import hashlib

text = "ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ"
d = 7  # Ο αριθμός των μηδενικών που πρέπει να έχει η hash τιμή στο τέλος

# Επαναληπτική διαδικασία για τον έλεγχο ακεραίων μέχρι να βρεθεί ο επιθυμητός αριθμός
x = 0
while True:
    x += 1
    new_text = text + str(x)
    new_hash = hashlib.sha256(new_text.encode()).hexdigest()
    if new_hash[-d:] == "0" * d:
        break

print("Ο επιθυμητός ακέραιος αριθμός είναι:", x)
print("Το νέο κείμενο είναι:", new_text)
print("Η hash τιμή του νέου κειμένου είναι:", new_hash)
