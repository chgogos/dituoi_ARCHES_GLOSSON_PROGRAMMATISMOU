# 6. Τύποι δεδομένων (Data Types)

## 6.2 Πρωτογενείς (βασικοί) τύποι δεδομένων

### 6.2.1 Αριθμητικοί τύποι

#### 6.2.1.1 Ακέραιοι (Integer)

```{.c title="ranges_integer_types.c" linenums="1"}
--8<-- "src/c/ranges_integer_types.c"
```

Παράδειγμα εκτέλεσης σε υπολογιστή Apple M2Pro

```console
$ gcc --version
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin24.3.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
$ gcc ranges_integer_types.c && ./a.out
Ranges for integer types in C:
char: -128 to 127
unsigned char: 0 to 255
short: -32768 to 32767
unsigned short: 0 to 65535
int: -2147483648 to 2147483647
unsigned int: 0 to 4294967295
long: -9223372036854775808 to 9223372036854775807
unsigned long: 0 to 18446744073709551615
long long: -9223372036854775808 to 9223372036854775807
unsigned long long: 0 to 18446744073709551615
```

#### 6.2.1.2 Κινητής Υποδιαστολής (Floating Point)

- [IEEE Floating-Point Standard 754](https://ieeexplore.ieee.org/document/8766229)
- <https://0.30000000000000004.com/>

```{.py title="floating_point.py" linenums="1"}
--8<-- "src/python/floating_point.py"
```

```console
$ python floating_point.py
0.1 + 0.2 = 0.30000000000000004
Is 0.1 + 0.2 exactly 0.3? False
Is 0.1 + 0.2 approximately 0.3? True
```

#### 6.2.1.3 Μιγαδικοί αριθμοί (Complex Numbers)

Παραδείγματα με τιμές μιγαδικού τύπου στην Python

```{.py title="complex_type_example.py" linenums="1"}
--8<-- "src/python/complex_type_example.py"
```

```console
$ python complex_type_example.py
z1: (3+4j), z2: (1-2j)
Sum: (4+2j)
Difference: (2+6j)
Product: (11-2j)
Quotient: (-1+2j)
Absolute value of z1: 5.0
Conjugate of z1: (3-4j)
Real part of z1: 3.0, Imaginary part of z1: 4.0
```

#### 6.2.1.4 Δεκαδικοί αριθμοί (Decimal)

BCD (Binary-Coded Decimal): Κάθε ψηφίο αναπαρίσταται από το δικό της σύνολο δυαδικών ψηφίων.

Για παράδειγμα ο δεκαδικός αριθμός 146 αναπαρίσταται στο BCD ως μια ακολουθία από 3 ομάδες 4 ψηφίων, δηλαδή ως 0001 0100 0110

```{.py title=decimal_example.py" linenums="1"}
--8<-- "src/python/decimal_example.py"
```

```console
$ python decimal_example.py
0.1 + 0.2 using Decimal: 0.3
Is 0.1 + 0.2 exactly 0.3? True
```

### 6.2.2 Boolean Τύποι

```{.cpp title="true_false.cpp" linenums="1"}
--8<-- "src/cpp/true_false.cpp"
```

```console
$ g++ true_false.cpp && ./a.out 
a (true) = 1
b (false) = 0
c (1) = 1
d (0) = 0
true + false = 1
5 > 3 is 1
```

### 6.2.3 Τύποι χαρακτήρων

```{.c title="ascii.c" linenums="1"}
--8<-- "src/c/ascii.c"
```

```console
$ gcc ascii.c && ./a.out
Character    ASCII Value
------------------------
    A          65
    B          66
    C          67
    D          68
    E          69
    F          70
    G          71
    H          72
    I          73
    J          74
    K          75
    L          76
    M          77
    N          78
    O          79
    P          80
    Q          81
    R          82
    S          83
    T          84
    U          85
    V          86
    W          87
    X          88
    Y          89
    Z          90

    a          97
    b          98
    c          99
    d          100
    e          101
    f          102
    g          103
    h          104
    i          105
    j          106
    k          107
    l          108
    m          109
    n          110
    o          111
    p          112
    q          113
    r          114
    s          115
    t          116
    u          117
    v          118
    w          119
    x          120
    y          121
    z          122

Additional ASCII characters:
Space: ASCII 32
0: ASCII 48
9: ASCII 57
!: ASCII 33
@: ASCII 64
#: ASCII 35
```

### 6.3 Τύποι συμβολοσειρών χαρακτήρων

```{.c title="string_example.c" linenums="1"}
--8<-- "src/c/string_example.c"
```

```console
$ gcc string_example.c && ./a.out
String: Hello, C!
Length of the string: 9
```

```{.cpp title="string_example.cpp" linenums="1"}
--8<-- "src/cpp/string_example.cpp"
```

```console
$ g++ string_example.cpp && ./a.out
Concatenated string: Hello, World!
Length of result: 13
Substring: Hello
'World' found at position: 7
After replace: Hello, C++!
str1 is 'Hello'
C-style string: Hello, C++!
```

## 6.4 Τύπος Απαρίθμησης (Enumeration Types)

```{.c title="enum_example.c" linenums="1"}
--8<-- "src/c/enum_example.c"
```

```console
$ gcc enum_example.c && ./a.out
Today is WEDNESDAY, which has an integer value of: 3
A regular weekday.
```

## 6.5 Τύποι Διατάξεων (Array Types)

```{.c title="ragged.c" linenums="1"}
--8<-- "src/c/ragged.c"
```

```c
$ gcc ragged.c && ./a.out
Row 1: 1 2 3 
Row 2: 4 5 6 7 8 
Row 3: 9 10 
```

## 6.6 Συσχετιστικοί πίνακες (Associative Arrays)

```{.cpp title="associative_array.cpp" linenums="1"}
--8<-- "src/cpp/associative_array.cpp"
```

```console
$ g++ assiative_array.cpp && ./a.out
apple: 3
banana: 5
orange: 2
apple: 3
banana: 5
orange: 2
```

```{.py title="associative_array.py" linenums="1"}
--8<-- "src/python/associative_array.py"
```

```console
$ python associate_array.py
apple: 3
banana: 5
orange: 2
apple: 3
banana: 5
orange: 2
```

## 6.7 Τύποι εγγραφών (Record Types)

```{.c title="record_example.c" linenums="1"}
--8<-- "src/c/record_example.c"
```

```console
$ gcc record_example.c && ./a.out
Student 1:
ID: 1
Name: John Doe
Grade: 92.50

Student 2:
ID: 2
Name: Jane Smith
Grade: 88.00
```

```{.py title="named_tuple.py" linenums="1"}
--8<-- "src/python/named_tuple.py"
```

```console
$ python named_tuple.py
Student 1:
ID: 1
Name: John Doe
Grade: 92.5

Student 2:
ID: 2
Name: Jane Smith
Grade: 88.0
```

## 6.8 Τύποι Πλειάδας (Tuple Types)

```{.py title="tuple_example.py" linenums="1"}
--8<-- "src/python/tuple_example.py"
```

```console
$ python named_tuple.py
First element of tuple1: 1
Last element of tuple2: cherry
Slicing tuple3 (from index 1 to 3): ('banana', 3.14)

Concatenated tuple6: (1, 2, 3, 4, 'apple', 'banana', 'cherry')

Repeated tuple7: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

Length of tuple1: 4

Is 'apple' in tuple2? True
Is 10 in tuple1? False

Iterating through tuple3:
1
banana
3.14
True

Nested tuple: (1, 2, (3, 4, 5))
Accessing element in nested tuple: 4

Tuple unpacking:
x = 10 y = 20 z = 30

Count of '2' in tuple8: 3
Index of '3' in tuple8: 3
```

## 6.9 Τύποι Λίστας (List Types)

```{.py title="list_example.py" linenums="1"}
--8<-- "src/python/list_example.py"
```

```console
$ python list_example.py
First element of list1: 1
Last element of list2: cherry
Slicing list3 (from index 1 to 3): ['banana', 3.14]

After modifying list1: [100, 2, 3, 4]

After appending 'orange' to list2: ['apple', 'banana', 'cherry', 'orange']
After inserting 'grape' at index 1: ['apple', 'grape', 'banana', 'cherry', 'orange']

After removing 'banana' from list2: ['apple', 'grape', 'cherry', 'orange']
After popping index 1: ['apple', 'cherry', 'orange']
Removed element: grape

Concatenated list6: [100, 2, 3, 4, 'apple', 'cherry', 'orange']

Repeated list7: ['apple', 'cherry', 'orange', 'apple', 'cherry', 'orange']

Length of list1: 4

Is 'apple' in list2? True
Is 10 in list1? False

Iterating through list3:
1
banana
3.14
True

Nested list: [1, 2, [3, 4, 5]]
Accessing element in nested list: 4

List unpacking:
x = 10 y = 20 z = 30

Count of '2' in list8: 3
Index of '3' in list8: 3
```

## 6.10 Τύποι Ενώσεων (Union Types)

```{.c title="union_example.c" linenums="1"}
--8<-- "src/c/union_example.c"
```

```console
$ gcc union_example.c && ./a.out
data.intVal = 10
data.floatVal = 3.14
data.charVal = A
After overwriting, data.intVal = 1078523201
After overwriting, data.floatVal = 3.14
```

## 6.11 Τύποι Δεικτών και Τύποι Αναφοράς (Pointer Types and Reference Types)

```{.cpp title="pointer_vs_reference.cpp" linenums="1"}
--8<-- "src/cpp/pointer_vs_reference.cpp"
```

```console
$ g++ pointer_vs_reference.cpp && ./a.out
Original values:
a = 5, b = 10

After modifyByReference:
a = 10, b = 10

After modifyByPointer:
a = 10, b = 20
```

### Αιωρούμενος Δείκτης (Dangling Pointer)

```{.c title="dangling_pointer.c" linenums="1"}
--8<-- "src/c/dangling_pointer.c"
```

```console
$ gcc dangling_pointer.c && ./a.out
Value in allocated memory: 42
Memory has been freed.
Value in dangling pointer: 0
```

<!-- ## 6.12 Έλεγχος Τύπων

## 6.13 Ισχυροί Τύποι (Strong Typing)

## 6.14 Ισοδυναμία Τύπων (Type Equivalence)

## 6.15 Θεωρία και Τύποι Δεδομένων -->