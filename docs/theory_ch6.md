# 6. Τύποι δεδομένων (Data Types)

## 6.2 Πρωτογενείς (βασικοί) τύποι δεδομένων

### 6.2.1 Αριθμητικοί τύποι

#### 6.2.1.1 Ακέραιοι (Integer)

```{.c title="ranges_integer_types.c" linenums="1"}
--8<-- "src/c/ranges_integer_types.c"
```

#### 6.2.1.2 Κινητής Υποδιαστολής (Floating Point)

IEEE Floating-Point Standard 754

```{.py title="floating_point.py" linenums="1"}
--8<-- "src/python/floating_point.py"
```

#### 6.2.1.3 Μιγαδικοί αριθμοί (Complex Numbers)

Μια μιγαδική τιμή στην Python

```py
>>> 7 + 3j
(7+3j)
```

#### 6.2.1.4 Δεκαδικοί αριθμοί (Decimal)

BCD (Binary-Coded Decimal): Κάθε ψηφίο αναπαρίσταται από το δικό της σύνολο δυαδικών ψηφίων.

Για παράδειγμα ο δεκαδικός αριθμός 146 αναπαρίσταται στο BCD ως μια ακολουθία από 3 ομάδες 4 ψηφίων, δηλαδή ως 0001 0100 0110

```{.py title=decimal_example.py" linenums="1"}
--8<-- "src/python/decimal_example.py"
```

### 6.2.2 Boolean Τύποι

```{.cpp title="true_false.cpp" linenums="1"}
--8<-- "src/cpp/true_false.cpp"
```

### 6.2.3 Τύποι χαρακτήρων

```{.c title="ascii.c" linenums="1"}
--8<-- "src/c/ascii.c"
```

### 6.3 Τύποι συμβολοσειρών χαρακτήρων

```{.c title="string_example.c" linenums="1"}
--8<-- "src/c/string_example.c"
```

```{.cpp title="string_example.cpp" linenums="1"}
--8<-- "src/cpp/string_example.cpp"
```

## 6.4 Τύπος Απαρίθμησης (Enumeration Types)

```{.c title="enum_example.c" linenums="1"}
--8<-- "src/c/enum_example.c"
```

## 6.5 Τύποι Διατάξεων (Array Types)

```{.c title="ragged.c" linenums="1"}
--8<-- "src/c/ragged.c"
```

## 6.6 Συσχετιστικοί πίνακες (Associative Arrays)

```{.cpp title="associative_array.cpp" linenums="1"}
--8<-- "src/cpp/associative_array.cpp"
```

```{.py title="associative_array.py" linenums="1"}
--8<-- "src/python/associative_array.py"
```


## 6.7 Τύποι εγγραφών (Record Types)

```{.c title="record_example.c" linenums="1"}
--8<-- "src/c/record_example.c"
```

```{.py title="named_tuple.py" linenums="1"}
--8<-- "src/python/named_tuple.py"
```

## 6.8 Τύποι Πλειάδας (Tuple Types)

```{.py title="tuple_example.py" linenums="1"}
--8<-- "src/python/tuple_example.py"
```

## 6.9 Τύποι Λίστας (List Types)

```{.py title="list_example.py" linenums="1"}
--8<-- "src/python/list_example.py"
```

## 6.10 Τύποι Ενώσεων (Union Types)

```{.c title="union_example.c" linenums="1"}
--8<-- "src/c/union_example.c"
```

## 6.11 Τύποι Δεικτών και Τύποι Αναφοράς (Pointer Types and Reference Types)

```{.cpp title="pointer_vs_reference.cpp" linenums="1"}
--8<-- "src/cpp/pointer_vs_reference.cpp"
```

### Dangling pointer

```{.c title="dangling_pointer.c" linenums="1"}
--8<-- "src/c/dangling_pointer.c"
```

<!-- ## 6.12 Έλεγχος Τύπων

## 6.13 Ισχυρή Τυποποίηση

## 6.14 Ισοδυναμία Τύπων

## 6.15 Θεωρία και Τύποι Δεδομένων -->