# 7. Εκφράσεις και προτάσεις εκχώρησης

## 7.2 Αριθμητικές εκφράσεις

### 7.2.1.6 Εκφράσεις υπό συνθήκη (conditional expressions)

```{.c title="conditional_expression.c" linenums="1"}
--8<-- "src/c/conditional_expression.c"
```

```console
$ gcc conditional_expression.c && ./a.out
The maximum value is: 20
15 is odd
-5 is negative
```

### 7.2.2.2 Αναφορική διαφάνεια (referential transparency)

Παράδειγμα που δείχνει ότι η C μπορέι να παραβιάσει την αναφορική διαφάνεια

```{.c title="no_referential_transparency.c" linenums="1"}
--8<-- "src/c/no_referential_transparency.c"
```

```console
$ gcc no_referential_transparency.c && ./a.out
First call: 6
Second call: 7
Third call: 8
```

## 7.3 Υπερφορτωμένοι τελεστές

Παράδειγμα σε Python

```{.py title="operator_overload.py" linenums="1"}
--8<-- "src/python/operator_overload.py"
```

```console
$ python operator_overload.py
(4,6)
```

Παράδειγμα σε C++

```{.cpp title="operator_overload.cpp" linenums="1"}
--8<-- "src/cpp/operator_overload.cpp"
```

```console
$ g++ operator_overload.cpp && ./a.out
(4,6)
```


## 7.4 Μετατροπές τύπων

## 7.5 Σχεσιακές και Boolean εκφράσεις

## 7.6 Εσπευσμένη αποτίμηση εκφράσεων

## 7.7 Προτάσεις εκχώρησης

## 7.8 Αναθέσεις μεικτού-τύπου
