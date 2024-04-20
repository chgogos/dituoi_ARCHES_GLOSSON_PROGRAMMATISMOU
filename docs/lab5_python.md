# Εργαστήριο 5 στην Python

Θέματα που εξετάζονται στο εργαστήριο: Γραφικά περιβάλλοντα διεπαφής με το tkinter[^1], APIs, matplotlib, MVC (Model View Controller)

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση E5A1** - Δημιουργήστε ένα πρόγραμμα το οποίο να υλοποιεί μια λίστα εργασιών (todo list) μέσω ενός γραφικού περιβάλλοντος διεπαφής. Ο χρήστης να μπορεί να εισάγει εργασίες στη λίστα και να διαγράφει εργασίες από τη λίστα. Να μην επιτρέπεται η εισαγωγή της ίδιας εργασίας πάνω από μια φορά στη λίστα εργασιών.

??? note "Λύση άσκησης E5A1"
    ```{.py title="5_1_sol.py" linenums="1"}
    --8<-- "src/python/lab5/5_1_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 5_1_sol.py
    ```
    ![TODO List GUI example](images/e5a1_TODO.png)

??? note "Λύση άσκησης E5A1 με OOP"
    ```{.py title="5_1_sol_oop.py" linenums="1"}
    --8<-- "src/python/lab5/5_1_sol_oop.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 5_1_sol_oop.py
    ```
    ![TODO List GUI example OOP](images/e5a1_TODO.png)


**Άσκηση E5A2** - Δημιουργήστε ένα πρόγραμμα που να διαχειρίζεται επαφές (contacts). Για κάθε επαφή να διατηρούνται οι πληροφορίες, επώνυμο, όνομα, τηλέφωνο. Να παρέχεται λειτουργικότητα CRUD (Create, Retrieve, Update, Delete). Τα δεδομένα να αποθηκεύονται σε αρχείο contacts.csv και να ανακαλούνται από αυτό κατά την εκκίνηση του προγράμματος.

??? note "Λύση άσκησης E5A2"
    ```{.py title="5_2_sol.py" linenums="1"}
    --8<-- "src/python/lab5/5_2_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 5_2_sol.py
    ```
    ![CRUD](images/e5a2_CRUD.png)

**Άσκηση E5A3** - Δημιουργήστε ένα πρόγραμμα που να απεικονίζει σε ένα γράφημα τις θερμοκρασίες για τις 5 τελευταίες ημέρες στην Άρτα [39.1606, 20.9853]. Χρησιμοποιήστε το module matplotlib για τη σχεδίαση του γραφήματος και για τη λήψη των θερμοκρασιών το [OpenWeathermap API](https://openweathermap.org/api) (προσοχή πρέπει να λάβετε API key και να το συμπληρώσετε μέσα στον κώδικα).

??? note "Λύση άσκησης E5A3"
    ```{.py title="5_3_sol.py" linenums="1"}
    --8<-- "src/python/lab5/5_3_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 5_3_sol.py
    ```
    ![Weather -5 days](images/e5a3.png)

**Άσκηση E5A4** - Χρησιμοποιήστε το pattern MVC έτσι ώστε να αναπτύξετε μια εφαρμογή που να πραγματοποιεί πράξεις πρόσθεσης, αφαίρεσης, πολλαπλασιασμού και διαίρεσης με μιγαδικούς αριθμούς. Στο ρόλο του view να μπορεί να εναλλάσσεται γραφικό περιβάλλον (GUI=Graphical User Interface) και περιβάλλον κειμένου (TUI=Text User Interface).

??? note "Λύση άσκησης E5A4"
    ```{.py title="5_4_sol.py" linenums="1"}
    --8<-- "src/python/lab5/5_4_sol.py"
    ```
    Παράδειγμα εκτέλεσης για TUI:
    ```
    $ python 5_4_sol.py TUI
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Complex Calculator  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Choose operation::
    1.Addition  2.Substraction  3.Multiplication  4.Division
    5.Quit
    3
    Input of 1st complex number:
    Give real part of 1st complex number:
    2
    Give imaginary part of 1st complex number:
    4
    Input of 2nd complex number:
    Give real part of 2nd complex number:
    3
    Give imaginary part of 2nd complex number:
    5
    Real Result: -14.000, Imaginary Result: 22.000
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Complex Calculator  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Choose operation::
    1.Addition  2.Substraction  3.Multiplication  4.Division
    5.Quit
    5
    Quitting ...
    ```
    
    Παράδειγμα εκτέλεσης για GUI:
    ```
    $ python 5_4_sol.py GUI
    ```
    ![Calculator GUI](images/e5a4.png)


## Επιπλέον εξάσκηση

**Άσκηση E5A5** - Υλοποιήστε με το tkinter την 1η εργασία (Counter) από την ιστοσελίδα [7GUIs](https://eugenkiss.github.io/7guis/tasks). Δηλαδή, δημιουργήστε ένα παράθυρο όπως το ακόλουθο και κάθε φορά που ο χρήστης πατά το πλήκτρο Count η τιμή στο πεδίο κειμένου που κατά την εκκίνηση έχει τιμή 0 να αυξάνεται κατά 1.

![Counter](https://eugenkiss.github.io/7guis/static/counter.9cd92091.png)

??? note "Λύση άσκησης E5A5"
    ```{.py title="e5a5.py" linenums="1"}
    --8<-- "src/python/lab5/e5a5.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python e5a5.py
    ```
    ![7GUIs task 1](images/e5a5.png)

**Άσκηση Ε5Α6** - Υλοποιήστε με το tkinter τη 2η εργασία (Temperature Converter) από την ιστοσελίδα [7GUIs](https://eugenkiss.github.io/7guis/tasks). Δηλαδή, δημιουργήστε ένα παράθυρο όπως το ακόλουθο: 

![Temperature converter](https://eugenkiss.github.io/7guis/static/tempconv.de9aff1f.png)

και κάθε φορά που ο χρήστης εισάγει θερμοκρασία είτε σε βαθμούς Κελσίου είτε σε βαθμούς Φάρεναϊτ να ενημερώνεται και η θερμοκρασία στην άλλη μονάδα μέτρησης. Εντοπίστε πληροφορίες για την ```StringVar```[^4] για την ```trace_add```[^5].

??? note "Λύση άσκησης E5A6"
    ```{.py title="e5a6.py" linenums="1"}
    --8<-- "src/python/lab5/e5a6.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python e5a6.py
    ```
    ![7GUIs task 2](images/e5a6.png)

[^1]: [Tkinter Tutorial](https://www.pythontutorial.net/tkinter/)
[^2]: [Tkinter Matplotlib](https://www.pythontutorial.net/tkinter/tkinter-matplotlib/)
[^3]: [Tkinter MVC](https://www.pythontutorial.net/tkinter/tkinter-mvc/)
[^4]: [StringVar](https://www.askpython.com/python-modules/tkinter/stringvar-with-examples)
[^5]: [trace_add](https://coderslegacy.com/python/tkinter-trace/)