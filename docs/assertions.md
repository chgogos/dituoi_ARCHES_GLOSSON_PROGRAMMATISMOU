# Assertions

##  Assertions στη C
Δείτε τα παραδείγματα με με εντολές assert, `assert()` και `static_assert()` στην παράγραφο 15.2 του [Τζάλλας, Α., Γκόγκος, Χ., & Τσούλος, Ι. (2024). Μια σύγχρονη προσέγγιση στη γλώσσα C [Προπτυχιακό εγχειρίδιο]. Κάλλιπος, Ανοικτές Ακαδημαϊκές Εκδόσεις.](https://repository.kallipos.gr/handle/11419/11683?&locale=el)


## Assertions στην Python

```{.py title="assert_example.py" linenums="1"}
--8<-- "src/python/assert_example.py"
```

Ενεργοποίηση του ελέγχου που ορίζεται στο assert μέσα στον κώδικα:
```
$ python assert_example.py
5.0
Traceback (most recent call last):
  File ".../assert_example.py", line 6, in <module>
    print(divide(10, 0))  # AssertionError: Denominator cannot be zero!
  File ".../assert_example.py", line 2, in divide
    assert b != 0, "Denominator cannot be zero!"
AssertionError: Denominator cannot be zero!
```


Απενεργοποίηση του ελέγχου που ορίζεται στο assert μέσα στον κώδικα, κατά την μεταγλώττιση/εκτέλεση:
```
$ python -Ο assert_example.py
5.0
Traceback (most recent call last):
  File ".../assert_example.py", line 6, in <module>
    print(divide(10, 0))  # AssertionError: Denominator cannot be zero!
  File ".../assert_example.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero
```
