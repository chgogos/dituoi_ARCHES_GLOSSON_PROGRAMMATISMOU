import sys

def main():
    if len(sys.argv) < 2:
        print("Παρακαλώ δώστε τουλάχιστον 2 ορίσματα")
        print("Χρήση: python program.py [sum|reverse] τιμή1 τιμή2 ...")
        return

    action = sys.argv[1] 

    if action == "sum":
        if len(sys.argv) < 3:
            print("Παρακαλώ δώστε τουλάχιστον έναν αριθμό για άθροισμα")
            return

        total = 0
        try:
            for num in sys.argv[2:]:
                total += float(num)
            print(f"Το άθροισμα είναι: {total}")
        except ValueError:
            print("Σφάλμα: Όλα τα ορίσματα πρέπει να είναι αριθμοί")

    elif action == "reverse":
        if len(sys.argv) < 3:
            print("Παρακαλώ δώστε κείμενο για αντιστροφή")
            return

        text = " ".join(sys.argv[2:])
        reversed_text = text[::-1]
        print(f"Αντεστραμμένο κείμενο: {reversed_text}")

    else:
        print(f"Άγνωστη εντολή: {action}")
        print("Διαθέσιμες εντολές: sum, reverse")


if __name__ == "__main__":
    main()
