# Εργαστήριο 4 στην Python

Θέματα που εξετάζονται στο εργαστήριο: αντικειμενοστραφής προγραμματισμός με την Python[^1], οι μέθοδοι ```__init__```, ```__str__```, ```__repr__```, υπερφόρτωση τελεστών[^2], κληρονομικότητα, εξαιρέσεις[^3], ορίσματα γραμμής εντολών με το sys.argv και με το argparse, logging.

[^1]: [Notebook με παραδείγματα αντικειμενοστραφούς προγραμματισμού](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/11-classes.ipynb)

[^2]: [Notebook με παραδείγματα υπερφόρτωσης τελεστών](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/34-operator_overloading.ipynb)

[^3]: [Notebook με παραδείγματα εξαιρέσεων](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/07-exceptions.ipynb)

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση E4A1** - Δημιουργήστε μια κλάση ```Car``` με μέλη δεδομένων τη μάρκα (```brand```), το μοντέλο (```model```) και το έτος κατασκευής (```year```). Υλοποιήστε τη μέθοδο κατασκευής ```__init__``` και τη μέθοδο ```__str__``` που θα εμφανίζει πληροφορίες για κάθε αντικείμενο τύπου ```Car```. Διαβάστε τα ακόλουθα δεδομένα και δημιουργήστε στιγμιότυπα αντικειμένων ```Car```. Ταξινομήστε τα αντικείμενα πρώτα με βάση το έτος κατασκευής, και μετά με βάση τη μάρκα. Εμφανίστε τα ταξινομημένα αντικείμενα.

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
    ```console
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

**Άσκηση E4A2** - Δίνεται ο ακόλουθος κώδικας που ορίζει την κλάση ```Juice``` και υπερφορτώνει τον τελεστή ```+```.

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

* Προσθέστε το επιπλέον πεδίο τιμή (```price```).
* Όταν εφαρμόζεται ο τελεστής πρόσθεσης ο νέος χυμός να έχει τιμή ίση με το άθροισμα τιμών των δύο χυμών.
* Προσθέστε τη μέθοδο ```pour``` που να δέχεται ως παράμετρο μια τιμή από το 0% μέχρι το 100% και να επιστρέφει ένα νέο αντικείμενο ```Juice``` με το χυμό που προκύπτει αν ληφθεί το αντίστοιχο ποσοστό περιεχομένου από το καλών αντικείμενο.


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

**Άσκηση E4A3** - Δημιουργήστε μια κλάση ```Stack``` που να ορίζει μια στοίβα. Η στοίβα να υποστηρίζει τις λειτουργίες ώθηση (```push```), απώθηση (```pop```), εκκαθάριση περιεχομένων στοίβας (```clear```) και εμφάνιση περιεχομένων στοίβας (με τη χρήση του ```__str__```). Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template4_3.py" linenums="1"}
--8<-- "src/python/lab4/template4_3.py"
```

??? note "Λύση άσκησης E4A3"
    ```{.py title="template4_3_sol.py" linenums="1"}
    --8<-- "src/python/lab4/template4_3_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```console
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

**Άσκηση E4A4** - Κατασκευάστε την κλάση ```Document``` που να αναπαριστά ένα έγγραφο που να περιέχει τη λίστα συντακτών του (```authors```) και την ημερομηνία δημιουργίας του (```creation_date```). Η κλάση Document να διαθέτει τη μέθοδο add_author για την προσθήκη συντακτών στο έγγραφο. Από την κλάση ```Document``` κληρονομήστε σε δύο άλλες κλάσεις, την υποκλάση ```Book``` και την υποκλάση ```Email```. Για την υποκλάση ```Book``` ορίστε το επιπλέον πεδίο ```title``` (τίτλος βιβλίου). Για την υποκλάση ```Email``` ορίστε τα επιπλέον πεδία ```sender``` (αποστολέας), ```subject``` (θέμα), ```recipients``` (λίστα παραληπτών). Η υποκλάση ```Recipient``` να διαθέτει τη μέθοδο ```add_recipient``` για την προσθήκη παραληπτών. Για όλες τις κλάσεις ορίστε κατάλληλους κατασκευαστές και τη συνάρτηση ```__str__```.
Τροποποιήστε το ακόλουθο template κώδικα: 

```{.py title="template4_4.py" linenums="1"}
--8<-- "src/python/lab4/template4_4.py"
```

έτσι ώστε η έξοδος να είναι η ακόλουθη: 

```console
Document created at 2022-03-24 09:30:00 authors=Nikos
Document created at 2022-03-24 10:20:00 authors=Petros, Maria
Document created at 2021-01-01 00:00:00 authors=Socrates, Descartes, Nietschie title=Philosophy 101 type=BOOK
Document created at 2022-03-26 10:30:00 authors=Panayiotis sender=Panayiotis subject=Important notice recipients=Maria type=EMAIL
Document created at 2022-03-21 22:45:00 authors=Marianthi, Vasilis sender=Marianthi subject=SPAM recipients=Maria, Christos, Vasilis, Sofia type=EMAIL
```

* Συμπληρώστε τον κώδικα στη ```main``` έτσι ώστε η λίστα εγγράφων να εμφανίζεται ταξινομημένη σε αύξουσα σειρά ημερομηνίας και ώρας δημιουργίας. 

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

## Επιπλέον εξάσκηση

**Άσκηση E4A5** - Δημιουργήστε μια κλάση με όνομα ```Cylinder``` (κύλινδρος) που: 

1. Nα έχει ως «ιδιωτικά μέλη» δεδομένων τα πεδία ```_height``` (ύψος κυλίνδρου) και ```_radius``` (ακτίνα βάσης κυλίνδρου). 
2. Ορίστε με την ```__init__``` κατασκευαστή που να θέτει τιμές και για τα δύο της μέλη δεδομένων μέσω παραμέτρων που θα δέχεται. 
3. Ορίστε μια συνάρτηση με όνομα ```volume``` που να επιστρέφει τον όγκο του κυλίνδρου με βάση τον τύπο $V=\pi r^2h$, όπου $r$ είναι η ακτίνα της βάσης και $h$ είναι το ύψος του κυλίνδρου (και $\pi = 3.14$). 
4. Συμπληρώστε τη συνάρτηση ```__str__``` έτσι ώστε να εμφανίζει τα στοιχεία ενός κυλίνδρου στη μορφή (ακτίνα, ύψος, όγκος). 
5. Στη ```__main__``` γράψτε κώδικα που να δημιουργεί μια λίστα με αντικείμενα ```Cylinder``` και προσθέστε 5 αντικείμενα ```Cylinder``` με τιμές ύψους κυλίνδρου και ακτίνας βάσης που θα δίνει ο χρήστης. Ταξινομήστε με τη συνάρτηση ```sort```  τα περιεχόμενα της λίστας σε φθίνουσα σειρά βάσει όγκου και εμφανίστε προκαλώντας την κλήση της συνάρτησης ```__str__``` για καθένα από τα στοιχεία της λίστας.

??? note "Λύση άσκησης E4A5"
    ```{.py title="e4a5.py" linenums="1"}
    --8<-- "src/python/lab4/e4a5.py"
    ```

    Παράδειγμα εκτέλεσης:
    ```console
    Δώσε ακτίνα και ύψος για κύλιδρο 1: 2 3.4
    Δώσε ακτίνα και ύψος για κύλιδρο 2: 1.2 4.5
    Δώσε ακτίνα και ύψος για κύλιδρο 3: 12.5 8.9
    Δώσε ακτίνα και ύψος για κύλιδρο 4: 3.3 6.7
    Δώσε ακτίνα και ύψος για κύλιδρο 5: 12.1 90.1
    (ακτίνα=12.1, ύψος=90.1, όγκος=41442.45)
    (ακτίνα=12.5, ύψος=8.9, όγκος=4368.78)
    (ακτίνα=3.3, ύψος=6.7, όγκος=229.22)
    (ακτίνα=2.0, ύψος=3.4, όγκος=42.73)
    (ακτίνα=1.2, ύψος=4.5, όγκος=20.36)
    ```

**Άσκηση E4A6** - Ορίστε μια κλάση με όνομα ```Interval``` (διάστημα) που:

1.	Να έχει ως «ιδιωτικά» μέλη δεδομένων τα πεδία ```_from``` (από) και ```_to``` (έως) που θα αναπαριστούν ένα διάστημα, π.χ. το διάστημα ```[3, 7)``` που έχει μήκος 4. 
2.	Να έχει έναν κατασκευαστή που να θέτει τιμές και για τα δύο ιδιωτικά της μέλη, μέσω παραμέτρων που θα δέχεται. Ωστόσο, αν γίνει απόπειρα να εισαχθεί τιμή στο ```_from``` μεγαλύτερη ή ίση του ```_to```, τότε να προκαλείται μια εξαίρεση (exception) τύπου ```ValueError```.
3.  Να έχει μια μέθοδο με όνομα ```length``` που να επιστρέφει το μήκος του διαστήματος. Ορίστε το ```length``` ως ```property``` έτσι ώστε αν εκχωρηθεί τιμή στο ```length``` τότε να προσαρμόζεται η τιμή του πεδίου ```_to```.
4.  Προσθέστε τις magic μεθόδους ```__str__``` και ```__repr__```.
5.  Να έχει μια μεταβλητή κλάσης με όνομα ```_cnt``` που να μετρά τα αντικείμενα ```Interval``` που έχουν δημιουργηθεί με έγκυρα στοιχεία για τα πεδία ```_from``` και ```_to```. Να επιστρέφεται η τιμή της ```_cnt``` μέσω μιας στατικής μεθόδου της κλάσης με όνομα ```number_of_intervals```.  
5.	Στη ```__main__``` γράψτε κώδικα που να ζητά από τον χρήστη να εισάγει 5 δεδομένα διαστημάτων και αν προκαλείται εξαίρεση, η εξαίρεση να «συλλαμβάνεται» και να εμφανίζεται μήνυμα, αλλιώς να εμφανίζεται το μήκος του διαστήματος (με την  ```__str__```), να αλλάζει σε 10 και να εμφανίζεται εκ νέου το διάστημα με την ```__repr__```. Με την ολοκλήρωση της εισαγωγής των δεδομένων να εμφανίζεται το πλήθος των αντικειμένων ```Interval```.

??? note "Λύση άσκησης E4A6"
    ```{.py title="e4a6.py" linenums="1"}
    --8<-- "src/python/lab4/e4a6.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    Δώσε "από", "μέχρι" όρια διαστήματος: 1 5
    [1,5)
    self._from=1 self._to=11
    Δώσε "από", "μέχρι" όρια διαστήματος: 4 6
    [4,6)
    self._from=4 self._to=14
    Δώσε "από", "μέχρι" όρια διαστήματος: 4 2
    To "από" πρέπει να είναι μικρότερο του "μέχρι"
    Δώσε "από", "μέχρι" όρια διαστήματος: 5 1
    To "από" πρέπει να είναι μικρότερο του "μέχρι"
    Δώσε "από", "μέχρι" όρια διαστήματος: 1 100
    [1,100)
    self._from=1 self._to=11
    Το πλήθος έγκυρων διαστημάτων που εισήχθησαν είναι 3
    ```

**Άσκηση E4A7[^4]** - Ορίστε την κλάση ```Length``` έτσι ώστε να δημιουργούνται αντικείμενα με εντολές της μορφής:

```py
Length(5.5, "cm")
Length(5.5, "in")
```

Ορίστε τις μεθόδους ```__str__``` και ```__repr__``` της ```Length```. Υπερφορτώστε τον τελεστή ```+``` έτσι ώστε να αθροίζονται δύο αντικείμενα ```Length``` και να προκύπτει ένα νέο αντικείμενο. Αν και τα δύο αντικείμενα έχουν την ίδια μονάδα μήκους (είτε cm είτε in) το αποτέλεσμα να είναι σε αυτή τη μονάδα μήκους. Αν η μονάδα μήκους είναι διαφορετική ανάμεσα στα δύο αντικείμενα τότε το αποτέλεσμα να είναι σε εκατοστά. Δίνεται ότι 1 ίντσα ισούται με 2.54 εκατοστά. Ακολουθεί ένα παράδειγμα εκτέλεσης όπου αρχικά δημιουργείται ένα αντικείμενο ```Length``` (με μονάδα μήκους τα εκατοστά) και εκτυπώνεται με την ```__str__```, μετά δημιουργείται ένα άλλο αντικείμενο ```Length``` (με μονάδα μήκους τις ίντσες) και εκτυπώνεται με την ```__repr__``` και μετά με τον τελεστή ```+``` προστίθενται τα δύο αντικείμενα και δημιουργείται ένα νέο αντικείμενο: 

```console
$ python e4a7.py
Εκτύπωση αντικειμένου με τη μέθοδο __str__ (3 τρόποι)
5.50cm
5.50cm
5.50cm
Εκτύπωση αντικειμένου με τη μέθοδο __repr__ (2 τρόποι)
value=3.0 unit=in
value=3.0 unit=in
Υπερφόρτωση τελεστή +
5.50cm + 3.00in = 13.12cm
```

??? note "Λύση άσκησης E4A7"
    ```{.py title="e4a7.py" linenums="1"}
    --8<-- "src/python/lab4/e4a7.py"
    ```

**Άσκηση 8[^4]** - Έστω ο ακόλουθος κώδικας που αφορά μια λίστα δραστηριοτήτων (TO DO LIST). Συμπληρώστε τον έτσι ώστε στις εντολές print να εμφανίζεται αυτό που έχει συμπεριληφθεί ως σχόλιο δεξιά της εντολής. 

```py
tdl = TodoList("groceries")
tdl.add("milk")
tdl.add("bread")
print(tdl.todos) # [description=milk completed=False, description=bread completed=False]
tdl.todos[0].toggle()
tdl.stats() # {'open': 1, 'completed': 1}
```

??? note "Λύση άσκησης E4A8"
    ```{.py title="e4a8.py" linenums="1"}
    --8<-- "src/python/lab4/e4a8.py"
    ```

[^4]: [https://marko-knoebl.github.io/slides/python-intermediate-collection-en.html - Object Oriented Programming and Classes](https://marko-knoebl.github.io/slides/python-intermediate-collection-en.html)

**Άσκηση 9[^5]** - Δημιουργήστε μια κλάση ζαριού (`Dice`). Υλοποίήστε τα ακόλουθα:

* Ο κατασκευαστής να δέχεται ένα όρισμα με όνομα `probs` που να είναι ένα λεξικό όπου κλειδί είναι ο αριθμός της πλευράς του ζαριού και τιμή είναι η πιθανότητα το ζάρι να έχει αυτό το αποτέλεσμα σε μια ρίψη του. Για παράδειγμα το λεξικό `{1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}` αντιστοιχεί σε ένα συνηθισμένο δίκαιο ζάρι.
* Προσθέστε μια μέθοδο `roll` που να  δέχεται ένα όρισμα με όνομα `n` με προκαθορισμένη τιμή 1 που να επιστρέφει τα αποτελέσματα από `n` ρίψεις του ζαριού.
* Προσθέστε μια μέθοδο `expected_value` που να επιστρέφει την αναμενόμενη τιμή και ορίστε τη συνάρτηση ως `@property`.
* Προσθέστε μια μέθοδο κλάσης `from_sides` που να δέχεται ως όρισμα το πλήθος των πλευρών ενός ζαριού και να επιστρέφει ένα αντικείμενο ζαριού με ίση πιθανότητα αποτελέσματος για κάθε πλευρά του (χρησιμοποιήστε τον decorator `@classmethod`).
* Προσθέστε τη μέθοδο `__len__` έτσι ώστε να εμφανίζει για ένα ζάρι το πλήθος των πλευρών του.
* Υπερφορτώστε τον τελεστή `+` έτσι ώστε να δημιουργεί ένα νέο ζάρι με τις πιθανότητες να προκύψει το καθένα από τα αποτελέσματα από το συνδυασμό των αποτελέσματων δύο ζαριών. Για παράδειγμα προσθέτοντας δύο ζάρια με 6 πλευρές το καθένα θα προκύψει ένα νέο "ζάρι" με πιθανά αποτελέσματα από το 2 μέχρι το 12, όπου το 2 προκύπτει μόνο με (1,1) και έχει πιθανότητα `1/6 * 1/6` να συμβεί, το 3 μπορεί να προκύψει με (1,2) και (2,1) και έχει πιθανότητα `1/6 * 1/6 + 1/6 * 1/6` να συμβεί κ.ο.κ.

??? note "Λύση άσκησης E4A9"
    ```{.py title="e4a9.py" linenums="1"}
    --8<-- "src/python/lab4/e4a9.py"
    ```

    Παράδειγμα εκτέλεσης:
    ```console
    $ python e4a9.py
    Dice({1: 0.16666666666666666, 2: 0.16666666666666666, 3: 0.16666666666666666, 4: 0.16666666666666666, 5: 0.16666666666666666, 6: 0.16666666666666666})
    Dice with sides: 1, 2, 3, 4, 5, 6
    Rolls: [2, 4, 1, 5, 6]
    Expected value of d6 = 3.5, sides = 6
    Dice({1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25})
    Dice with sides: 1, 2, 3, 4
    Rolls: [3, 1, 2, 4, 1]
    Expected value of d4 = 2.5, sides = 4
    Dice({2: 0.041666666666666664, 3: 0.08333333333333333, 4: 0.125, 5: 0.16666666666666666, 6: 0.16666666666666666, 7: 0.16666666666666666, 8: 0.125, 9: 0.08333333333333333, 10: 0.041666666666666664})
    Dice with sides: 2, 3, 4, 5, 6, 7, 8, 9, 10
    Rolls: [5, 8, 5, 5, 2]
    Expected value of d6_d4 = 6.0, sides = 9
```

[^5]: Πρόκειται για παράδειγμα από το [https://calmcode.io/course/objects - calmcode.io - objects](https://calmcode.io/course/objects/)

**Άσκηση 10** Γράψτε ένα πρόγραμμα που να δέχεται ορίσματα γραμμής εντολών (τουλάχιστον 2). Αν το πρώτο όρισμα είναι το sum να εμφανίζει το άθροισμα από τις τιμές που ακολουθούν. Αν το πρώτο όρισμα είναι reverse τότε να αντιστρέφει το κείμενο που ακολουθεί.

??? note "Λύση άσκησης E4A10"
    ```{.py title="e4a10.py" linenums="1"}
    --8<-- "src/python/lab4/e4a10.py"
    ```

    Παράδειγμα εκτέλεσης:
    ```console
    $ python e4a10.py sum 5 10 15
    Το άθροισμα είναι: 30.0
    $ python e4a10.py reverse Hello
    olleH
    ```

??? note "Λύση άσκησης E4A10 με το argparse"
    ```{.py title="e4a10b.py" linenums="1"}
    --8<-- "src/python/lab4/e4a10b.py"
    ```
    
    Παράδειγμα εκτέλεσης:
    ```console
    $ python e4a10b.py -h
    usage: e4a10b.py [-h] {sum,reverse} ...

    Process some inputs with different operations.

    positional arguments:
    {sum,reverse}  Available commands
        sum          Sum all the provided numbers
        reverse      Reverse the provided text

    options:
    -h, --help     show this help message and exit
    $ python e4a10b.py sum -h 
    usage: e4a10b.py sum [-h] numbers [numbers ...]

    positional arguments:
    numbers     Numbers to sum

    options:
    -h, --help  show this help message and exit
    $ python e4a10b.py reverse -h
    usage: e4a10b.py reverse [-h] text [text ...]

    positional arguments:
    text        Text to reverse

    options:
    -h, --help  show this help message and exit
    $ python e4a10b.py revers     
    usage: e4a10b.py [-h] {sum,reverse} ...
    e4a10b.py: error: argument command: invalid choice: 'revers' (choose from 'sum', 'reverse')
    $ python e4a10b.py sum 10 20 30 
    The sum is: 60.0
    $ python e4a10b.py reverse Hello
    Reversed text: olleH
    ```

**Άσκηση 11** Γράψτε ένα πρόγραμμα που να ρυθμίζει το logging έτσι ώστε να εμφανίζει μηνύματα INFO στην οθόνη (με format %(levelname)s - %(message)s) και να αποθηκεύει τα μηνύματα (από DEBUG και πάνω) σε αρχείο e4a11.log (με format %(asctime)s - %(levelname)s - %(message)s). Υλοποιήστε μια συνάρτηση calculate_division(x, y) που: (1) καταγράφει DEBUG με τις τιμές εισόδου, (2) επιστρέφει το αποτέλεσμα της διαίρεσης (INFO για επιτυχία), (3) καταγράφει ERROR με stack trace αν y=0. Καλέστε τη συνάρτηση δύο φορές (έγκυρη και μη έγκυρη διαίρεση) και επαληθεύστε τα logs στην οθόνη και στο αρχείο.

??? note "Λύση άσκησης E4A11"
    ```{.py title="e4a11.py" linenums="1"}
    --8<-- "src/python/lab4/e4a11.py"
    ```

    Παράδειγμα εκτέλεσης
    ```console
    $ python e4a11.py
    INFO - Result: 5.0
    ERROR - Division by zero!
    Traceback (most recent call last):
    File "/Users/chgogos/git_repos/dituoi_ARCHES_GLOSSON_PROGRAMMATISMOU/docs/src/python/lab4/e4a11.py", line 20, in calculate_division
        result = x / y
    ZeroDivisionError: division by zero
    ```
