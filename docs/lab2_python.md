# Εργαστήριο 2 στην Python

Θέματα που εξετάζονται στο εργαστήριο: συγγραφή συναρτήσεων[^1], unit tests με τη στάνταρντ βιβλιοθήκη unittest[^2], comprehensions[^3][^4], virtual environments (venv), εξωτερικές βιβλιοθήκες και εγκατάσταση με το pip, unit tests με το pytest[^5].


## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση E2A1** - Γράψτε μια συνάρτηση που να δέχεται δύο λεκτικά και να επιστρέφει την απόσταση Hamming (δηλαδή το πλήθος των αντίστοιχων χαρακτήρων που διαφέρουν στα δύο λεκτικά). Αν τα λεκτικά είναι διαφορετικού μήκους η συνάρτηση να επιστρέφει την τιμή -1. Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template2_1.py" linenums="1"}
--8<-- "src/python/lab2/template2_1.py"
```

??? note "Λύση άσκησης 1"
    ```{.py title="template2_1_sol.py" linenums="1"}
    --8<-- "src/python/lab2/template2_1_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python template2_1_sol.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

**Άσκηση E2A2** - Γράψτε μια συνάρτηση που να ελέγχει αν μια φράση είναι παντόγραμμα, δηλαδή περιλαμβάνει και τα 24 γράμματα του Ελληνικού αλφαβήτου. Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template2_2.py" linenums="1"}
--8<-- "src/python/lab2/template2_2.py"
```

??? note "Λύση άσκησης 2"
    ```{.py title="template2_2_sol.py" linenums="1"}
    --8<-- "src/python/lab2/template2_2_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python template2_2_sol.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

**Άσκηση E2A3**  -  Γράψτε μια συνάρτηση που να δέχεται ένα κείμενο, να αφαιρεί τα σύμβολα τελεία και κόμμα, να εντοπίζει το μεγαλύτερο μήκος λέξης που περιέχει και να επιστρέφει μια λίστα με όλες τις λέξεις του κειμένου με μήκος ίσο με το μεγαλύτερο μήκος, ταξινομημένες σε αύξουσα σειρά. Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template2_3.py" linenums="1"}
--8<-- "src/python/lab2/template2_3.py"
```

??? note "Λύση άσκησης 3"
    ```{.py title="template2_3_sol.py" linenums="1"}
    --8<-- "src/python/lab2/template2_3_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python template2_3_sol.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```


**Άσκηση E2A4** - Για την ακόλουθη λίστα τιμών 56, 37, 771, 90, 16, 11 γράψτε comprehensions που να κάνουν τα ακόλουθα:

1. Να δημιουργεί νέα λίστα με το πλήθος των ψηφίων κάθε τιμής.
2. Να δημιουργεί νέα λίστα με τα ψηφία κάθε τιμής σε αντίστροφη σειρά.
3. Να δημιουργεί νέα λίστα μόνο με τις τιμές που είναι μεγαλύτερες από το μέσο όρο των τιμών.
4. Να δημιουργεί νέα λίστα με ζεύγη τιμών που το πρώτο στοιχείο κάθε ζεύγους να είναι η ίδια τιμή και δεύτερο στοιχείο μια λογική τιμή με τιμή True αν η τιμή είναι άρτια αλλιώς η τιμή False.

Τροποποιήστε το ακόλουθο template κώδικα έτσι ώστε η λύση σας να επιτυγχάνει σε όλα τα unit tests.

```{.py title="template2_4.py" linenums="1"}
--8<-- "src/python/lab2/template2_4.py"
```

??? note "Λύση άσκησης 4"
    ```{.py title="template2_4_sol.py" linenums="1"}
    --8<-- "src/python/lab2/template2_4_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python template2_4_sol.py
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    OK
    ```


## Επιπλέον εξάσκηση

**Άσκηση E2A5** Σε έναν φάκελο στην επιφάνεια εργασίας με όνομα ```e2a5```, από τη γραμμή εντολών δημιουργήστε ένα virtual environment με όνομα ```myenv``` και ενεργοποιήστε το με τις ακόλουθες εντολές σε Windows:

```
> python -m venv myenv
> myenv\Scripts\activate.bat
```

ή με τις ακόλουθες εντολές σε Linux ή MacOS:

```
$ python -m venv myenv
$ source myenv/bin/activate
```

Εγκαταστήστε στο ```myenv``` με το ```pip``` τη βιβλιοθήκη [Faker](https://faker.readthedocs.io/en/master/). 

```
(myenv) > pip install faker
```

Δημιουργήστε στοιχεία (όνομα, διεύθυνση, ημερομηνία γέννησης) για 100 υποθετικά άτομα ηλικιών από 18 έως 90 ετών και αποθηκεύστε τα σε ένα αρχείο με όνομα ```fake100.txt``` με ελληνικά ερωτηματικά (;) ως διαχωριστικά των στοιχείων κάθε ατόμου. Συμβουλευτείτε την τεκμηρίωση της βιβλιοθήκης για τις συναρτήσεις που πρέπει να καλέσετε. Φροντίστε έτσι ώστε η εκτέλεση του κώδικα να δίνει κάθε φορά τις ίδιες τιμές. 

Ακολουθεί ένα απόσπασμα τυχαίων τιμών που μπορεί να δημιουργούνται:

```
Allison Hill;819 Johnson Course, East William, AK 74064;1947-09-15
Kimberly Robinson;65423 Garcia Light, West Melanieview, AS 06196;1986-06-17
Valerie Gray;310 Kendra Common Apt. 164, Reidstad, GA 49021;1959-02-15
Mia Sutton;327 Nelson Route, Lake Mark, WI 07832;1949-11-29
```

??? note "Λύση άσκησης 5"
    ```{.py title="e2a5.py" linenums="1"}
    --8<-- "src/python/lab2/e2a5.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python e2a5.py
    Δημιουργία στοιχείων 100 υποθετικών ατόμων και αποθήκευση στο αρχείο fake100.txt.
    ```
    ```{.txt title="fake100.txt"}
    --8<-- "src/python/lab2/fake100.txt"
    ```


**Άσκηση E2A6** Μια άλλη βιβλιοθήκη για unit tests είναι η εξωτερική βιβλιοθήκη [pytest](https://docs.pytest.org/). Επιλύστε ξανά την άσκηση **Ε2Α1** χρησιμοποιώντας αυτή τη φορά την pytest για τους ελέγχους.

??? note "Λύση άσκησης 6"
    Πρώτα θα πρέπει να εγκατασταθεί η βιβλιοθήκη pytest.
    ```
    (myenv) > pip install pytest
    ```
    
    Ο κώδικας που πραγματοποιεί τους ελέγχους με το pytest ακολουθεί:
    ```{.py title="e2a6_test.py" linenums="1"}
    --8<-- "src/python/lab2/e2a6_test.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python e2a6_test.py
    ============================ test session starts =============================
    platform darwin -- Python 3.10.12, pytest-8.1.1, pluggy-1.4.0
    rootdir: XXX/src/python/lab2
    plugins: Faker-24.1.0
    collected 1 item

    e2a6_test.py .                                                         [100%]

    ============================= 1 passed in 0.02s ==============================
    ```
    Στο pytest το όνομα του αρχείου που περιέχει τα tests πρέπει να ξεκινά με ```test_``` ή να τελειώνει με ```_test.py```. Επίσης, τα ονόματα των συναρτήσεων με τους ελέγχους πρέπει να ξεκινούν με ```test_``` ή η κλάση που περιέχει ως μεθόδους τους ελέγχους να έχει όνομα που να ξεκινά με ```Test```. 


[^1]: [Notebook με παραδείγματα συναρτήσεων](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/09-functions.ipynb)
[^2]: [Notebook με παραδείγματα unittest](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/13-testing.ipynb)
[^3]: [Notebook με παραδείγματα comprehensions](https://calmcode.io/course/comprehensions/introduction)
[^4]: [calmcode.io - comprehensions](https://calmcode.io/course/comprehensions/introduction)
[^5]: [calmcode.io - pytest](https://calmcode.io/course/pytest/introduction)
