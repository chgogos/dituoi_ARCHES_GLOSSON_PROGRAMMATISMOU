# 7. Εκφράσεις και προτάσεις εκχώρησης

## 7.2 Αριθμητικές εκφράσεις

Παράδειγμα με μεγάλους αριθμούς στη Python

```{.py title="large_numbers.py" linenums="1"}
--8<-- "src/python/large_numbers.py"
```

```console
$ python large_numbers.py 
The factorial of 100 is: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
```

Παράδειγμα με μεγάλους αριθμούς στη C

```{.c title="large_numbers.c" linenums="1"}
--8<-- "src/c/large_numbers.c"
```

Εγκατάσταση της βιβλιοθήκης GMP σε Linux
```console
$ sudo apt update
$ sudo apt install libgmp-dev
```

```
$ gcc -o factorial factorial.c -lgmp & ./a.out
The factorial of 100 is: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

```



### 7.2.1 Σειρά αποτίμησης τελεστών

```{.py title="expressions.py" linenums="1"}
--8<-- "src/python/expressions.py"
```

```{.c title="expressions.c" linenums="1"}
--8<-- "src/c/expressions.c"
```

#### 7.2.1.6 Εκφράσεις υπό συνθήκη (conditional expressions)

```{.c title="conditional_expression.c" linenums="1"}
--8<-- "src/c/conditional_expression.c"
```

```console
$ gcc conditional_expression.c && ./a.out
The maximum value is: 20
15 is odd
-5 is negative
```

### 7.2.2 Σειρά αποτίμησης τελεστέων

#### 7.2.2.1 Παρενέργειες (side-effects)

```{.c title="side_effects.c" linenums="1"}
--8<-- "src/c/side_effects.c"
```

#### 7.2.2.2 Αναφορική διαφάνεια (referential transparency)

Παράδειγμα παραβίασης της αναφορικής διαφάνειας στη C

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

```{.c title="widening_narrowing.c" linenums="1"}
--8<-- "src/c/widening_narrowing.c"
```

```console
$ gcc widening_narrowing.c && ./a.out
widening_narrowing.c:24:30: warning: implicit conversion from 'int' to 'unsigned char' changes value from 300 to 44 [-Wconstant-conversion]
   24 |   unsigned char narrowChar = 300;  // char (0-255), 300 wraps around
      |                 ~~~~~~~~~~   ^~~
1 warning generated.
Widening Conversions:
int to float: 100 → 100.000000
float to double: 100.000000 → 100.000000

Narrowing Conversions:
double to float: 123456.789000 → 123456.789062
float to int: 123456.789062 → 123456

Overflow in Narrowing:
300 stored in unsigned char: 44
```

## 7.5 Σχεσιακές και Boolean εκφράσεις

```{.py title="equality_vs_identity.py" linenums="1"}
--8<-- "src/python/equality_vs_identity.py"
```

## 7.6 Εσπευσμένη αποτίμηση εκφράσεων

```{.c title="short_circuit.c" linenums="1"}
--8<-- "src/c/short_circuit.c"
```

```console
$ gcc short_circuit.c && ./a.out
Found 30 at index 2
```

## 7.7 Προτάσεις εκχώρησης

```{.c title="assignment_operators.c" linenums="1"}
--8<-- "src/c/assignment_operators.c"
```

```console
$ gcc assignment_operators.c && ./a.out
Assignment: a = 5
Equality: a == b is true
Addition Assignment: a += 10 -> a = 17
Initial x = 3
Pre-increment: ++x = 4
Post-increment: x++ = 4
After post-increment, x = 5
```

### 7.7.5 Η εκχώρηση ως έκφραση

```{.c title="assignment_as_expression.c" linenums="1"}
--8<-- "src/c/assignment_as_expression.c"
```

```console
$ gcc assignment_as_expression.c && ./a.out
Sum after loop: 12
```

## 7.8 Αναθέσεις μεικτού-τύπου

```{.py title="mixed_types_assignments.py" linenums="1"}
--8<-- "src/python/mixed_types_assignments.py"
```

```console
$ python mixed_types_assignments.py
Widening: i (int) = 10, f (float) = 10.00
Narrowing: pi (float) = 3.14159, x (int) = 3
String to int: s = '42', num = 42
Int to string: n = 123, s = '123'
Float to string: f = 99.99, s = '99.99'
Boolean to int: b = True, num = 1
Int to boolean: num = 0, b = False
Implicit conversion: 5 + 2.5 = 7.5 (type: <class 'float'>)
```
