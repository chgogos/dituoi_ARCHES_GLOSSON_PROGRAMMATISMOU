# Εργαστήριο 4 στην Python

Θέματα που εξετάζονται στο εργαστήριο: αντικειμενοστραφής προγραμματισμός με την Python, οι μέθοδοι ```__init__```, ```__str__```, ```__repr__```, υπερφόρτωση τελεστών, κληρονομικότητα. 

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


**Άσκηση E4A3** - Δημιουργήστε μια κλάση Stack που να ορίζει μια στοίβα. Η στοίβα να υποστηρίζει τις λειτουργίες ώθηση (push), απώθηση (pop), εκκαθάριση περιεχομένων στοίβας (clear) και εμφάνιση περιεχομένων στοίβας (με τη χρήση του \_\_str\_\_). Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template4_3.py" linenums="1"}
--8<-- "src/python/lab4/template4_3.py"
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