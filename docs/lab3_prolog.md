# Εργαστήριο 3 στην Prolog

Θέματα που εξετάζονται στο εργαστήριο: Prolog Unit Tests[^1]

## Εξάσκηση (εκφωνήσεις και λύσεις ασκήσεων)

**Άσκηση PRO3E1** Γράψτε μια βάση γνώσης που να περιέχει την πληροφορία ότι ο `john`  και ο `george` είναι άνδρες, οι `mary`, `susan` και `alice` γυναίκες, ο `john` είναι γονέας της `mary`, η `mary` είναι γονέας της `susan` και του `george`, και η `susan` είναι γονέας της `alice`. Επιπλέον ορίστε το κατηγόρημα `ancestor\2` που να ορίζει πότε ένα άτομο είναι πρόγονος ενός άλλου ατόμου. Γράψτε κατάλληλο κώδικα έτσι ώστε τα ακόλουθα tests να περνάνε.

???+ note "pro3e1_tests.pl"
    ```{.prolog title=pro3e1_tests.pl linenums="1"}
    --8<-- "src/prolog/lab3/pro3e1_tests.pl"
    ```

Γράψτε τις εντολές που εκτελούν τα tests.

??? note "Λύση άσκησης PRO3E1"
    ```{.prolog title=pro3e1.pl linenums="1"}
    --8<-- "src/prolog/lab3/pro3e1.pl"
    ```

    Εκκίνηση του swipl.
    ```
    $ swipl
    Welcome to SWI-Prolog (threaded, 64 bits, version 9.2.9)
    SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software.
    Please run ?- license. for legal details.

    For online help and background, visit https://www.swi-prolog.org
    For built-in help, use ?- help(Topic). or ?- apropos(Word).
    ```

    Φόρτωση του αρχείου pro3e1_tests.pl (που περιέχει τα tests).
    ```
    ?- [pro3e1_tests].
    true.
    ```

    Εκτέλεση των tests.
    ```
    ?- run_tests.
    [6/6] dituoi_tests:not_ancestor .................... passed (0.000 sec)
    % All 6 tests passed in 0.003 seconds (0.002 cpu)
    ```
    
    Ή αν γίνει αλλαγή στο κώδικα και θέλουμε να ξαναδοκιμάσουμε τα tests.
    ```
    ?- make.
    true.
    ?- run_tests.
    [6/6] dituoi_tests:not_ancestor .................... passed (0.000 sec)
    % All 6 tests passed in 0.003 seconds (0.002 cpu)
    ```

[^1]: [Unit tests](https://www.swi-prolog.org/pldoc/man?section=plunit-intro)
