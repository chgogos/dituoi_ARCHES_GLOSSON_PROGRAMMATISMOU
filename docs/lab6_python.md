# Εργαστήριο 6 στην Python

Θέματα που εξετάζονται στο εργαστήριο: συναρτησιακός προγραμματισμός με την Python[^6][^8], λάμδα συναρτήσεις[^1][^7] (lambda functions), συναρτήσεις υψηλότερης τάξης (higher order functions), μερικές συναρτήσεις[^5] (partial functions), γεννήτριες[^2] (generator functions και generator expressions) και οκνηρή αποτίμηση (lazy evaluation), iterators[^3], list comprehensions, βιβλιοθήκες itertools[^4] και functools[^5].

**Άσκηση Ε6Α1 (λάμδα συναρτήσεις και συναρτήσεις υψηλότερης τάξης)** - Δίνεται η ακόλουθη λίστα από πλειάδες που αναπαριστούν παραγγελίες ενός ηλεκτρονικού καταστήματος:

```sh
orders = [
    ("A101", "laptop", 1200, 1),
    ("A102", "mouse", 25, 2),
    ("A103", "keyboard", 75, 1),
    ("A104", "monitor", 300, 2),
    ("A105", "laptop", 1100, 1),
    ("A106", "mouse", 20, 3),
    ("A107", "monitor", 280, 1)
]
```

Κάθε πλειάδα έχει τη μορφή: (order_id, product, price_per_unit, quantity).

Να γράψετε πρόγραμμα που χωρίς χρήση for-loops και αξιοποιώντας lambda συναρτήσεις και higher-order functions (συναρτήσεις map, filter, sorted και από το functools η συνάρτηση reduce) να εκτελεί τα ακόλουθα:

- Υπολογισμός συνολικής αξίας κάθε παραγγελίας. Δηλαδή, δημιουργήστε μια νέα λίστα όπου κάθε στοιχείο θα έχει τη μορφή: (order_id, product, total_value), όπου total_value = price_per_unit * quantity
- Φιλτράρισμα παραγγελιών με συνολική αξία πάνω από 100 ευρώ
- Ομαδοποίηση order_id ανά προϊόν
- Ταξινομήστε τα προϊόντα κατά συνολική αξία σε φθίνουσα σειρά
- Εύρεση προϊόντος με τα μεγαλύτερα συνολικά έσοδα από όλες τις παραγγελίες

??? note "Λύση άσκησης E6A1"
    ```{.py title="e6a1.py" linenums="1"}
    --8<-- "src/python/lab6/e6a1.py"
    ```

**Άσκηση Ε6Α2 (μερική αποτίμηση συναρτήσεων)** - Δίνεται η παρακάτω συνάρτηση που υπολογίζει την τελική αξία μιας παραγγελίας, λαμβάνοντας υπόψη την τιμή μονάδας price, την ποσότητα quantity, την έκπτωση discount και τον φόρο tax:

```py
def calculate_price(price, quantity, discount, tax):
    return price * quantity * (1 - discount) * (1 + tax)
```

Να γράψετε πρόγραμμα που να χρησιμοποιεί partial function evaluation ώστε:

- Να δημιουργεί μια νέα συνάρτηση calculate_with_tax, στην οποία ο φόρος να είναι σταθερός στο 24%.
- Να δημιουργεί μια νέα συνάρτηση calculate_with_discount, στην οποία η έκπτωση να είναι σταθερή στο 10%.
- Να δημιουργεί μια νέα συνάρτηση calculate_standard_order, στην οποία τόσο ο φόρος όσο και η έκπτωση να είναι σταθερά στο 24% και 10% αντίστοιχα.
- Να καλεί τις νέες συναρτήσεις για διαφορετικές τιμές προϊόντων και ποσοτήτων και να εμφανίζει τα αποτελέσματα με κατάλληλα μηνύματα.

??? note "Λύση άσκησης E6A2"
    ```{.py title="e6a2.py" linenums="1"}
    --8<-- "src/python/lab6/e6a2.py"
    ```

**Άσκηση Ε6Α3 (γεννήτριες)** - Να γράψετε μια γεννήτρια συνάρτηση `running_totals(numbers)` η οποία δέχεται μια λίστα αριθμών και παράγει σταδιακά τα αθροίσματα των στοιχείων της λίστας. Για παράδειγμα, για τη λίστα `numbers = [4, 7, 2, 10]` η γεννήτρια θα πρέπει να παράγει τις τιμές `4, 11, 13, 23` σταδιακά με κάθε κλήση την εντολής `yield`.  Καλέστε την `yield` σε μια `for`.

??? note "Λύση άσκησης E6A3"
    ```{.py title="e6a3.py" linenums="1"}
    --8<-- "src/python/lab6/e6a3.py"
    ```

**Άσκηση Ε6Α4 (memoization)**
 Ο ακόλουθος κώδικας υπολογίζει αναδρομικά τον n-οστό όρο της ακολουθίας [Fibonacci (0,1,1,2,3,5,8,13,...)](https://en.wikipedia.org/wiki/Fibonacci_sequence).

```{.py title="e6a4a.py" linenums="1"}
--8<-- "src/python/lab6/e6a4a.py"
```

 Ωστόσο, καθυστερεί υπερβολικά για τιμές του n από 40 και πάνω. Εντοπίστε την τιμή του n για την οποία ο χρόνος υπολογισμού του n-οστού όρου είναι περισσότερο από 10 δευτερόλεπτα.

??? note "Άσκηση E6A4 (α΄ μέρος)"
    ```{.py title="e6a4b.py" linenums="1"}
    --8<-- "src/python/lab6/e6a4b.py"
    ```

 Στη συνέχεια προτείνετε λύση με το functools @cache που να λύνει το θέμα της ταχύτητας υπολογισμού.

??? note "Άσκηση E6A4 (β΄ μέρος)"
    ```{.py title="e6a4c.py" linenums="1"}
    --8<-- "src/python/lab6/e6a4c.py"
    ```

**Άσκηση Ε6Α5 itertools**
Να υλοποιήσετε τις παρακάτω συναρτήσεις, ώστε να περνάνε τα unittests, χρησιμοποιώντας τις συναρτήσεις του module itertools: count, combinations, product, accumulate, cycle, islice.

```{.py title="e6a5.py" linenums="1"}
--8<-- "src/python/lab6/e6a5.py"
```

??? note "Άσκηση E6A5"
    ```{.py title="e6a5sol.py" linenums="1"}
    --8<-- "src/python/lab6/e6a5sol.py"
    ```

**Άσκηση Ε6Α5 (all και any)**
Δίνεται μια λίστα από φοιτητές, όπου κάθε φοιτητής αναπαρίσταται από ένα tuple της μορφής (name, passed) όπου name είναι το όνομα του φοιτητή και το passed που είναι True αν ο φοιτητής πέρασε ένα μάθημα διαφορετικά είναι False. Δίνεται ο ακόλουθος κώδικας που ελέγχει α) αν όλοι οι φοιτητές έχουν περάσει το μάθημα και β) αν υπάρχει τουλάχιστον ένας φοιτητής που δεν πέρασε το μάθημα.

```{.py title="e6a6.py" linenums="1"}
--8<-- "src/python/lab6/e6a6.py"
```

Υλοποιήστε την ίδια λειτουργικότητα χρησιμοποιώντας τις συναρτήσεις all() και any().

??? note "Άσκηση E6A6"
    ```{.py title="e6a6sol.py" linenums="1"}
    --8<-- "src/python/lab6/e6a6sol.py"
    ```


[^1]: [Notebook με παραδείγματα λάμδα συναρτήσεων](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/10-lambdas.ipynb)
[^2]: [Notebook με παραδείγματα generators](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/23-generators.ipynb)
[^3]: [Notebook με παραδείγματα iterators](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/24-iterators.ipynb)
[^4]: [Notebook με παραδείγματα από το itertools](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/25-itertools.ipynb)
[^5]: [Notebook με παραδείγματα από το functools](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/40-functools.ipynb)
[^6]: [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
[^7]: [calmcode.io - lambdas](https://calmcode.io/course/lambda/introduction) 
[^8]: [Python advanced](https://marko-knoebl.github.io/slides/python-advanced-collection-en.html)