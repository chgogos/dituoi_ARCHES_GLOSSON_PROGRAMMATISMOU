# Εργαστήριο 1 στη Ηaskell

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση H1E1** Γράψτε μια συνάρτηση με όνομα `volumeBox` που να υπολογίζει τον όγκο ενός κουτιού δεχόμενη ως είσοδο το πλάτος, το μήκος και το ύψος του, και μια συνάρτηση με όνομα `volumeSquarePyramid` που να υπολογίζει τον όγκο μιας πυραμίδας με τετραγωνική βάση δεχόμενη το μήκος της πλευράς της βάσης της πυραμίδας και το ύψος της πυραμίδας. Γράψτε ένα πρόγραμμα σε Haskell που να ζητά από το χρήστη τις διαστάσεις μιας πυραμίδας με τετραγωνική βάση (μήκος πλευράς βάσης και ύψος σε μέτρα) και να υπολογίζει πόσα πέτρινα τούβλα χρειάζονται κατά προσέγγιση για να καλυφθεί ο όγκος της πυραμίδας αν κάθε τούβλο έχει μήκος 19 εκατοστά, πλάτος 9 εκατοστά και ύψος 6 εκατοστά. Δίνεται ότι ο όγκος μιας πυραμίδας είναι ίσος με το ένα τρίτο του γινομένου του εμβαδού της βάσης της πυραμίδας επί το ύψος της.

??? note "Λύση άσκησης H1E1"
    ```{.hs title=h1e1.hs linenums="1"}
    --8<-- "src/haskell/lab1/h1e1.hs"
    ```
    Μεταγλώττιση και εκτέλεση:
    ```
    $ ghc h1e1.hs
    [1 of 2] Compiling Main             ( h1e1.hs, h1e1.o )
    [2 of 2] Linking h1e1
    $ ./h1e1
    Μήκος πλευράς βάσης σε μέτρα: 10
    Ύψος πυραμίδας σε μέτρα: 5
    Αριθμός πέτρινων τούβλων = 162443.14489928525
    ```

**Άσκηση H1E2** Οι αντιστάσεις έχουν έναν χρωματικό κώδικα που υποδεικνύει πόσα Ohms είναι η κάθε μια. Ο κώδικας αποτελείται από τρεις γραμμές και κάθε μία γραμμή υποδηλώνει ένα ψηφίο (black=0, brown=1, red=2, orange=3, yellow=4, green=5, blue=6 violet=7, grey=8, white=9). Η χωρητικότητα σε Ohms υπολογίζεται ως εξής. Η πρώτη γραμμή αντιστοιχεί στο πλέον αριστερό ψηφίο, η δεύτερη γραμμή στο αμέσως επόμενο και η τρίτη γραμμή σε ποσα μηδενικά ακολουθούν. Έτσι, για παράδειγμα ο συνδυασμός violet, grey, red υποδηλώνει 7800 Ohms. Γράψτε ένα πρόγραμμα σε Haskell που για μια αντίσταση ο χρήστης να δίνει τρία χρώματα στη σειρά και το πρόγραμμα να εμφανίζει τα Ohms της αντίστασης.

<!-- ![Resistors](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Resistor_color_code.png/754px-Resistor_color_code.png) -->


??? note "Λύση άσκησης H1E2"
    ```{.hs title=h1e2.hs linenums="1"}
    --8<-- "src/haskell/lab1/h1e2.hs"
    ```
    Μεταγλώττιση και εκτέλεση:
    ```
    $ ghc h1e2.hs
    [1 of 2] Compiling Main             ( h1e2.hs, h1e2.o )
    [2 of 2] Linking h1e2
    $ ./h1e2
    Enter resistor's color code :
    violet
    grey
    red
    Ohms = 7800
    ```

**Άσκηση H1E3** Κατασκευάστε μια συνάρτηση με όνομα `inRange` που να δέχεται τρία ορίσματα `min`, `max` και `x` (ακέραιες τιμές) και να επιστρέφει True ή False ανάλογα με το αν το `x` βρίσκεται στο διάστημα `[min,max]` ή όχι. Καλέστε τη συνάρτηση από κύριο πρόγραμμα για 3 τιμές που θα δίνει ο χρήστης και εμφανίστε κατάλληλα μηνύματα. Γράψτε 3 επιπλέον εναλλακτικές υλοποιήσεις της `inRange` χρησιμοποιώντας let bindings, where και guards.


??? note "Λύση άσκησης H1E3"
    ```{.hs title=h1e3.hs linenums="1"}
    --8<-- "src/haskell/lab1/h1e3.hs"
    ```
    Μεταγλώττιση και εκτέλεση:
    ```
    $ ghc h1e3.hs
    [1 of 2] Compiling Main             ( h1e3.hs, h1e3.o )
    [2 of 2] Linking h1e3
    $ ghc h1e3
    Enter min : 10
    Enter max : 30
    Enter value : 20
    Α' Τρόπος
    YES
    Β' Τρόπος
    YES
    Γ' Τρόπος
    YES
    Δ' Τρόπος
    YES
    ```

**Άσκηση H1E4** Συμπληρώστε σε ένα αρχείο με όνομα `h1e4i.hs` τον ακόλουθο κώδικα που ταξινομεί μια λίστα τιμών υλοποιώντας τον αλγόριθμο quicksort.

```hs
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let smallerSorted = quicksort [a | a <- xs, a <= x]
      biggerSorted = quicksort [a | a <- xs, a > x]
  in  smallerSorted ++ [x] ++ biggerSorted
```

α) Φορτώστε το αρχείο `h1e4i.hs` στο ghci και ταξινομήστε τις ακόλουθες λίστες τιμών:

```
[9, 7, 3, 2, 1, 5, 6, 0, 4, 8]
[3.142, 2.718, 1.414, 1.618]
["Ioannina", "Preveza", "Igoumenitsa", "Arta"]
[False, True, False, True]
```

??? note "Λύση άσκησης H1E4 (α' ερώτημα)"
    ```
    $ ghci h1e4i.hs
    GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
    [1 of 2] Compiling Main             ( h1e4i.hs, interpreted )
    Ok, one module loaded.
    ghci> quicksort [9, 7, 3, 2, 1, 5, 6, 0, 4, 8]
    [0,1,2,3,4,5,6,7,8,9]
    ghci> quicksort [3.142, 2.718, 1.414, 1.618]
    [1.414,1.618,2.718,3.142]
    ghci> quicksort ["Ioannina", "Preveza", "Igoumenitsa", "Arta"]
    ["Arta","Igoumenitsa","Ioannina","Preveza"]
    ghci> quicksort [False, True, False, True]
    [False,False,True,True]
    ghci> :module Data.List
    ghci> sort [9, 7, 3, 2, 1, 5, 6, 0, 4, 8]
    [0,1,2,3,4,5,6,7,8,9]
    ghci> :q
    Leaving GHCi.
    ```

β) Δημιουργήστε ένα αρχείο `h1e4.hs` που όταν μεταγλωττιστεί με το ghc να προκύπτει εκτελέσιμο που κατά την εκτέλεσή του να ταξινομεί και να εμφανίζει ταξινομημένες τις παραπάνω λίστες.

??? note "Λύση άσκησης H1E4 (β' ερώτημα με την υλοποίηση της quicksort)"
    ```{.hs title=h1e4.hs linenums="1"}
    --8<-- "src/haskell/lab1/h1e4.hs"
    ```
    Μεταγλώττιση και εκτέλεση:
    ```
    $ ghc h1e4.hs
    [1 of 2] Compiling Main             ( h1e4.hs, h1e4.o )
    [2 of 2] Linking h1e4
    $ ./h1e4
    [0,1,2,3,4,5,6,7,8,9]
    [1.414,1.618,2.718,3.142]
    ["Arta","Igoumenitsa","Ioannina","Preveza"]
    [False,False,True,True]
    ```

??? note "Λύση άσκησης H1E4 (β' ερώτημα με τη συνάρτηση βιβλιοθήκης sort)"
    ```{.hs title=h1e4sort.hs linenums="1"}
    --8<-- "src/haskell/lab1/h1e4sort.hs"
    ```
    Μεταγλώττιση και εκτέλεση:
    ```
    $ ghc h1e4sort.hs
    [1 of 2] Compiling Main             ( h1e4sort.hs, h1e4sort.o )
    [2 of 2] Linking h1e4sort
    $ ./h1e4sort
    [0,1,2,3,4,5,6,7,8,9]
    [1.414,1.618,2.718,3.142]
    ["Arta","Igoumenitsa","Ioannina","Preveza"]
    [False,False,True,True]
    ```

