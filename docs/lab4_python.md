# Εργαστήριο 4 στην Python

Θέματα που εξετάζονται στο εργαστήριο: αντικειμενοστραφής προγραμματισμός με την Python[^1], οι μέθοδοι ```__init__```, ```__str__```, ```__repr__```, υπερφόρτωση τελεστών[^2], κληρονομικότητα. 

[^1]: [Notebook με παραδείγματα αντικειμενοστραφούς προγραμματισμού](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/11-classes.ipynb)

[^2]: [Notebook με παραδείγματα υπεφόρτωσης τελεστών](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/34-operator_overloading.ipynb)

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση E4A1** - Δημιουργήστε μια κλάση Car με μέλη δεδομένων τη μάρκα (brand), το μοντέλο (model) και το έτος κατασκευής (year). Υλοποιήστε τη μέθοδο κατασκευής \_\_init\_\_ και τη μέθοδο \_\_str\_\_ που θα εμφανίζει πληροφορίες για κάθε αντικείμενο τύπου Car. Διαβάστε τα ακόλουθα δεδομένα και δημιουργήστε στιγμιότυπα αντικειμένων Car. Ταξινομήστε τα αντικείμενα πρώτα με βάση το έτος κατασκευής, και μετά με βάση τη μάρκα. Εμφανίστε τα ταξινομημένα αντικείμενα.

```
cars = """
#year,brand,model
1969,Dodge,Charger
1963,Corvette, Stingray
1974,Porsche,914
1969,Chevrolet,Camaro Z28
1967,Toyota,2000GT
1971,Ford,Thunderbird
1991,Dodge,Viper
1966,Lamborghini,Miura
1962,Ferrari,250 GTO
1954,Mercedes,300SL Gullwing"""
```

??? note "Λύση άσκησης E4A1"
    ```{.py title="4_1_sol.py" linenums="1"}
    --8<-- "src/python/lab4/4_1_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 4_1_sol.py
    Brand: Mercedes, model: 300SL Gullwing, year: 1954
    Brand: Ferrari, model: 250 GTO, year: 1962
    Brand: Corvette, model:  Stingray, year: 1963
    Brand: Lamborghini, model: Miura, year: 1966
    Brand: Toyota, model: 2000GT, year: 1967
    Brand: Chevrolet, model: Camaro Z28, year: 1969
    Brand: Dodge, model: Charger, year: 1969
    Brand: Ford, model: Thunderbird, year: 1971
    Brand: Porsche, model: 914, year: 1974
    Brand: Dodge, model: Viper, year: 1991
    ```

**Άσκηση E4A2** - Δίνεται ο ακόλουθος κώδικας που ορίζει την κλάση Juice και υπερφορτώνει τον τελεστή +.

```Python
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, other):
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
result = a + b
print(result)
```

* Προσθέστε το επιπλέον πεδίο τιμή (price).
* Όταν εφαρμόζεται ο τελεστής πρόσθεσης ο νέος χυμός να έχει τιμή ίση με το άθροισμα τιμών των δύο χυμών.
* Προσθέστε τη μέθοδο pour() που να δέχεται ως παράμετρο μια τιμή από το 0% μέχρι το 100% και να επιστρέφει ένα νέο αντικείμενο Juice με το χυμό που προκύπτει αν ληφθεί το αντίστοιχο ποσοστό περιεχομένου από το καλών αντικείμενο.


??? note "Λύση άσκησης E4A2"
    ```{.py title="4_2_sol.py" linenums="1"}
    --8<-- "src/python/lab4/4_2_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    Orange (1.50L) 3.50 €
    Apple (2.00L) 3.00 €
    Orange&Apple (3.50L) 6.50 €
    Pouring 40.0% from Orange&Apple (3.50L) 6.50 €
    Orange&Apple (2.10L) 3.90 €
    Orange&Apple (1.40L) 2.60 €
    ```

**Άσκηση E4A3** - Δημιουργήστε μια κλάση Stack που να ορίζει μια στοίβα. Η στοίβα να υποστηρίζει τις λειτουργίες ώθηση (push), απώθηση (pop), εκκαθάριση περιεχομένων στοίβας (clear) και εμφάνιση περιεχομένων στοίβας (με τη χρήση του \_\_str\_\_). Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template4_3.py" linenums="1"}
--8<-- "src/python/lab4/template4_3.py"
```

??? note "Λύση άσκησης E4A3"
    ```{.py title="template4_3_sol.py" linenums="1"}
    --8<-- "src/python/lab4/template4_3_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

**Άσκηση E4A4** - Κατασκευάστε την κλάση Document που να αναπαριστά ένα έγγραφο που να περιέχει τη λίστα συντακτών του (authors) και την ημερομηνία δημιουργίας του (creation_date). Η κλάση Document να διαθέτει τη μέθοδο add_author για την προσθήκη συντακτών στο έγγραφο. Από την κλάση Document κληρονομήστε σε δύο άλλες κλάσεις, την υποκλάση Book και την υποκλάση Email. Για την υποκλάση Book ορίστε το επιπλέον πεδίο title (τίτλος βιβλίου). Για την υποκλάση Email ορίστε τα επιπλέον πεδία sender (αποστολέας), subject (θέμα), recipients (λίστα παραληπτών). Η υποκλάση Recipient να διαθέτει τη μέθοδο add_recipient για την προσθήλη παραληπτών. Για όλες τις κλάσεις ορίστε κατάλληλους κατασκευαστές και τη συνάρτηση \_\_str\_\_.
Τροποποιήστε το ακόλουθο template κώδικα: 

```{.py title="template4_4.py" linenums="1"}
--8<-- "src/python/lab4/template4_4.py"
```

έτσι ώστε η έξοδος να είναι η ακόλουθη: 

```
Document created at 2022-03-24 09:30:00 authors=Nikos
Document created at 2022-03-24 10:20:00 authors=Petros, Maria
Document created at 2021-01-01 00:00:00 authors=Socrates, Descartes, Nietschie title=Philosophy 101 type=BOOK
Document created at 2022-03-26 10:30:00 authors=Panayiotis sender=Panayiotis subject=Important notice recipients=Maria type=EMAIL
Document created at 2022-03-21 22:45:00 authors=Marianthi, Vasilis sender=Marianthi subject=SPAM recipients=Maria, Christos, Vasilis, Sofia type=EMAIL
```

* Συμπληρώστε τον κώδικα στη main έτσι ώστε η λίστα εγγράφων να εμφανίζεται ταξινομημένη σε αύξουσα σειρά ημερομηνίας και ώρας δημιουργίας. 

??? note "Λύση άσκησης E4A4"
    ```{.py title="template4_4_sol.py" linenums="1"}
    --8<-- "src/python/lab4/template4_4_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    Document created at 2022-03-24 09:30:00 authors=Nikos
    Document created at 2022-03-24 10:20:00 authors=Petros, Maria
    Document created at 2021-01-01 00:00:00 authors=Socrates, Descartes, Nietschie title=Philosophy 101 type=BOOK
    Document created at 2022-03-26 10:30:00 authors=Panayiotis sender=Panayiotis subject=Important notice recipients=Maria type=EMAIL
    Document created at 2022-03-21 22:45:00 authors=Marianthi, Vasilis sender=Marianthi subject=SPAM recipients=Maria, Christos, Vasilis, Sofia type=EMAIL
    ################################################################################
    Document created at 2021-01-01 00:00:00 authors=Socrates, Descartes, Nietschie title=Philosophy 101 type=BOOK
    Document created at 2022-03-21 22:45:00 authors=Marianthi, Vasilis sender=Marianthi subject=SPAM recipients=Maria, Christos, Vasilis, Sofia type=EMAIL
    Document created at 2022-03-24 09:30:00 authors=Nikos
    Document created at 2022-03-24 10:20:00 authors=Petros, Maria
    Document created at 2022-03-26 10:30:00 authors=Panayiotis sender=Panayiotis subject=Important notice recipients=Maria type=EMAIL
    ```
