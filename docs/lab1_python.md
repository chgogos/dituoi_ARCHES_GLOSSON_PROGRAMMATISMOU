# Εργαστήριο 1 στην Python

Θέματα που εξετάζονται στο εργαστήριο: συγγραφή και εκτέλεση απλών προγραμμάτων σε Python, ranges, δομή επανάληψης[^1], δομή επιλογής[^2], βασικές δομές δεδομένων[^3] (lists, tuples, dictionaries, sets), λεκτικά[^4] (μήκος λεκτικού, αντιστροφή λεκτικού, λήψη τμήματος λεκτικού με slice), αμυντικός προγραμματισμός[^5], import και χρήση βιβλιοθηκών, ChatGPT prompts για παραγωγή κώδικα Python, χρήση του REPL (Read Evaluate Print Loop) της Python.

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση E1A1** - Γράψτε πρόγραμμα που να υπολογίζει τα 10 πρώτα ψηφία του αποτελέσματος της πράξης $\sqrt{\frac{2^{101}}{\pi^{53}+11^7}}$

??? note "Λύση άσκησης Ε1Α1"
    ```{.py title="1_1_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_1_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_1_sol.py
    106.5474731672522
    1065474731
    ```

**Άσκηση E1A2** - Γράψτε πρόγραμμα που να εμφανίζει για τη συμβολοσειρά "How I want a drink alcoholic of course after the heavy lectures involving quantum mechanics"[^1] το πλήθος των χαρακτήρων κάθε λέξης. Παρατήρηση: η μέθοδος split() σε μια συμβολοσειρά επιστρέφει μια λίστα με τις λέξεις της.

[^1]: Το κείμενο αυτό είναι ένας μνημονικός κανόνας για τα 15 πρώτα ψηφία του $\pi$ (3.14159265358979).

??? note "Λύση άσκησης Ε1Α2"
    ```{.py title="1_2_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_2_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_2_sol.py
    314159265358979
    ```

**Άσκηση E1A3** - Γράψτε πρόγραμμα που να υπολογίζει το άθροισμα $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \ldots$ όπου ο χρήστης θα δίνει το πλήθος των όρων του αθροίσματος. Διασφαλίστε με αμυντικό προγραμματισμό ότι η τιμή που δίνει ο χρήστης είναι μια μη αρνητική ακέραια τιμή, αλλιώς να ζητείται επανεισαγωγή της τιμής.

??? note "Λύση άσκησης Ε1Α3"
    ```{.py title="1_3_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_3_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_3_sol.py
    Εισάγετε έναν μη αρνητικό ακέραιο αριθμό: -1
    Λάθος τιμή, προσπαθήστε ξανά!
    Εισάγετε έναν μη αρνητικό ακέραιο αριθμό: α
    Λάθος τιμή, προσπαθήστε ξανά!
    Εισάγετε έναν μη αρνητικό ακέραιο αριθμό: 5
    Οι 5 πρώτοι όροι έχουν άθροισμα 1.9375
    ```

**Άσκηση E1A4** - Δώστε την εντολή ```import this``` στο REPL (Read Evaluate Print Loop) του IDLE (Integrated Decelopmentv and Learning Environment) της Python και αντιγράψτε σε ένα λεκτικό το κείμενο που επιστρέφεται. Γράψτε πρόγραμμα που να εμφανίζει το πλήθος παρατηρήσεων των χαρακτήρων Α έως και Z, χωρίς διάκριση πεζών και κεφαλαίων, στο παραπάνω κείμενο.

??? note "Λύση άσκησης Ε1Α4 (α' τρόπος)"
    ```{.py title="1_4_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_4_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_4_sol.py
    Χαρακτήρας A εμφανίσεις 53
    Χαρακτήρας B εμφανίσεις 21
    Χαρακτήρας C εμφανίσεις 17
    Χαρακτήρας D εμφανίσεις 17
    Χαρακτήρας E εμφανίσεις 92
    Χαρακτήρας F εμφανίσεις 12
    Χαρακτήρας G εμφανίσεις 11
    Χαρακτήρας H εμφανίσεις 31
    Χαρακτήρας I εμφανίσεις 53
    Χαρακτήρας K εμφανίσεις 2
    Χαρακτήρας L εμφανίσεις 33
    Χαρακτήρας M εμφανίσεις 16
    Χαρακτήρας N εμφανίσεις 42
    Χαρακτήρας O εμφανίσεις 43
    Χαρακτήρας P εμφανίσεις 22
    Χαρακτήρας R εμφανίσεις 33
    Χαρακτήρας S εμφανίσεις 46
    Χαρακτήρας T εμφανίσεις 79
    Χαρακτήρας U εμφανίσεις 21
    Χαρακτήρας V εμφανίσεις 5
    Χαρακτήρας W εμφανίσεις 4
    Χαρακτήρας X εμφανίσεις 6
    Χαρακτήρας Y εμφανίσεις 17
    Χαρακτήρας Z εμφανίσεις 1
    ```

??? note "Λύση άσκησης Ε1Α4 (β' τρόπος)"
    ```{.py title="1_4_sol_alt.py" linenums="1"}
    --8<-- "src/python/lab1/1_4_sol_alt.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_4_sol_alt.py
    Χαρακτήρας a εμφανίσεις 53
    Χαρακτήρας b εμφανίσεις 21
    Χαρακτήρας c εμφανίσεις 17
    Χαρακτήρας d εμφανίσεις 17
    Χαρακτήρας e εμφανίσεις 92
    Χαρακτήρας f εμφανίσεις 12
    Χαρακτήρας g εμφανίσεις 11
    Χαρακτήρας h εμφανίσεις 31
    Χαρακτήρας i εμφανίσεις 53
    Χαρακτήρας j εμφανίσεις 0
    Χαρακτήρας k εμφανίσεις 2
    Χαρακτήρας l εμφανίσεις 33
    Χαρακτήρας m εμφανίσεις 16
    Χαρακτήρας n εμφανίσεις 42
    Χαρακτήρας o εμφανίσεις 43
    Χαρακτήρας p εμφανίσεις 22
    Χαρακτήρας q εμφανίσεις 0
    Χαρακτήρας r εμφανίσεις 33
    Χαρακτήρας s εμφανίσεις 46
    Χαρακτήρας t εμφανίσεις 79
    Χαρακτήρας u εμφανίσεις 21
    Χαρακτήρας v εμφανίσεις 5
    Χαρακτήρας w εμφανίσεις 4
    Χαρακτήρας x εμφανίσεις 6
    Χαρακτήρας y εμφανίσεις 17
    Χαρακτήρας z εμφανίσεις 1
    ```

## Επιπλέον εξάσκηση 

**Άσκηση E1A5** - Γράψτε πρόγραμμα που να δέχεται ένα κείμενο από τον χρήστη και να επιστρέφει το ίδιο κείμενο χωρίς κενά και ανεστραμμένο. Αναζητήστε λύση με "prompting", χρησιμοποιώντας το [ChatGPT](https://chat.openai.com/) ή το [Google Gemini](https://gemini.google.com/app) ή το [Microsoft Copilot](https://copilot.microsoft.com/) ή κάποιο άλλο εναλλακτικό μοντέλο γλωσσικής επεξεργασίας φυσικής γλώσσας.

??? note "Λύση άσκησης Ε1Α5"
    ```{.py title="1_5_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_5_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_5_sol.py
    Παρακαλώ εισάγετε ένα κείμενο: Τμήμα Πληροφορικής και Τηλεπικοινωνιών
    Το ανεστραμμένο κείμενο χωρίς κενά είναι: νώινωνιοκιπεληΤιακςήκιροφορηλΠαμήμΤ
    ```

**Άσκηση E1A6** - Αν προστεθεί ο ακέραιος αριθμός 28706162 στο τέλος του κειμένου "ΠΑΝΕΠΙΣΤΗΜΙΟ ΙΩΑΝΝΙΝΩΝ", το νέο κείμενο "ΠΑΝΕΠΙΣΤΗΜΙΟ ΙΩΑΝΝΙΝΩΝ28706162" θα έχει hash τιμή (με τη συνάρτηση κατακερματισμού SHA256) με τα 8 τελευταία ψηφία μηδέν. Αυτό φαίνεται στον ακόλουθο κώδικα: 

```{.py title="1_6.py" linenums="1"}
--8<-- "src/python/lab1/1_6.py"
```
Παράδειγμα εκτέλεσης:
```
$ python 1_6.py
05f4cd1984d18f7200e31891c2b66ba6752568a691ce077da8824c9e0ef05fe3
5c4b9aaed7f48d66a643fc05665f868454c1517e9f5f108b0478305c00000000
```

Ποιος θα είναι ο αριθμός που πρέπει να προστεθεί στο τέλος του κειμένου "ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ" για να έχει το νέο κείμενο hash τιμή με τα 7 τελευταία ψηφία μηδέν;
Ζητήστε από το [ChatGPT](https://chat.openai.com/) ή άλλο να εξηγήσει αναλυτικά τον ρόλο της εντολής: ```hashlib.sha256(text.encode()).hexdigest()```.


??? note "Λύση άσκησης Ε1Α6"
    ```{.py title="1_6_sol.py" linenums="1"}
    --8<-- "src/python/lab1/1_6_sol.py"
    ```
    Παράδειγμα εκτέλεσης:
    ```
    $ python 1_6_sol.py
    Ο επιθυμητός ακέραιος αριθμός είναι: 113357317
    Το νέο κείμενο είναι: ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ113357317
    Η hash τιμή του νέου κειμένου είναι: 392ea340cf29585a1043a190967e19815d39b7ff58486d8ba1ff9d0e00000000
    ```

[^1]: [Notebook με παραδείγματα δομής επανάληψης](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/05-loops.ipynb)
[^2]: [Notebook με παραδείγματα δομής επιλογής](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/04-conditionals.ipynb)
[^3]: [Notebook με παραδείγματα βασικών δομών δεδομένων](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/03-lists-tuples-dictionaries-sets.ipynb)
[^4]: [Notebook με παραδείγματα χειρισμού λεκτικών](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/02-strings.ipynb)
[^5]: [Παραδείγματα αμυντικού προγραμματισμού](./defensive.md)