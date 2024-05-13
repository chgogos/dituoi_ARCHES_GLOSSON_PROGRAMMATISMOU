# Επιρροές συναρτησιακού προγραμματισμού σε κυρίως προστακτικές γλώσσες

* Λάμδα συναρτήσεις (ανώνυμες συναρτήσεις)
* Συναρτήσεις υψηλότερης τάξης (higher order functions)
* Περιφραστικές λίστες (list comprehensions)
* Μερικές συναρτήσεις (partial functions)
* Οκνηρή αποτίμηση (lazy evaluation)
* Κλειστότητες (closures)

## Παραδείγματα απλών λάμδα συναρτήσεων σε C++, Java, Python

```{.cpp title="simple_lambda.cpp" linenums="1"}
--8<-- "src/cpp/simple_lambda.cpp"
```

```
$ g++ simple_lambda.cpp -o simple_lambda
$ ./simple_lambda
42
63
```


```{.java title="SimpleLambda.java" linenums="1"}
--8<-- "src/java/simple_lambda/SimpleLambda.java"
```

```
$ javac SimpleLambda.java 
$ java SimpleLambda
42
```

```{.py title="simple_lambda.py" linenums="1"}
--8<-- "src/python/simple_lambda.py"
```

```
$ python simple_lambda.py
42
63
```

[Notebook με παραδείγματα lambdas σε Python](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/10-lambdas.ipynb)

## Συναρτήσεις υψηλότερης τάξης σε C++, Java, Python

**Ταξινόμηση λεκτικών με βάση το μήκος τους (χρησιμοποιείται ως παράμετρος ανώνυμη συνάρτηση)**

```{.cpp title="sort_with_lambda.cpp" linenums="1"}
--8<-- "src/cpp/sort_with_lambda.cpp"
```

```
$ g++ sort_with_lambda.cpp -o sort_with_lambda
$ ./sort_with_lambda
arta
preveza
ioannina
igoumenitsa
```

```{.java title="SortWithLambda.java" linenums="1"}
--8<-- "src/java/sort_with_java/SortWithLambda.java"
```

```
$ javac SortWithLambda.java
$ java SortWithLambda
arta
preveza
ioannina
igoumenitsa
```

```{.py title="sort_with_lambda.py" linenums="1"}
--8<-- "src/python/sort_with_lambda.py"
```

```
$ python sort_with_lambda.py
arta
preveza
ioannina
igoumenitsa
```

## Περιφραστικές λίστες (list comprehensions) στην Python

Οι περιφραστικές λίστες είναι μια ιδέα που πρωτοεμφανίστηκε στην Haskell αλλά πλέον και άλλες γλώσσες όπως οι Scala, F# και Python έχουν ενσωματώσει τις περιφραστικές λίστες.

[Notebook με παραδείγματα περιφραστικών λιστών στην Python](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/06-comprehensions.ipynb)

## Μερικές συναρτήσεις στην Python

```{.py title="partial_function_example1.py" linenums="1"}
--8<-- "src/python/partial_function_example1.py"
```

```
$ python partial_function_example1
20
```

```{.py title="partial_function_example2.py" linenums="1"}
--8<-- "src/python/partial_function_example2.py"
```

```
$ python partial_function_example2
10
10
10
10
```

## Οκνηρή αποτίμηση (lazy evaluation) στην Python

Στην Python, range είναι μια ακολουθία που δεν μπορεί να τροποποιηθεί (immutable) και η οποία αποτιμάται οκνηρά. Τα στοιχεία της ακολουθίας δεν δημιουργούνται παρά μόνο όταν απαιτούνται.

```{.py title="ranges_are_lazy.py" linenums="1"}
--8<-- "src/python/ranges_are_lazy.py"
```

```
$ python ranges_are_lazy.py
range(0, 1000000, 1000)
5000
```

```{.py title="generators_are_lazy.py" linenums="1"}
--8<-- "src/python/generators_are_lazy.py"
```

```
$ python generators_are_lazy.py
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
```

[Notebook με παραδείγματα generators στην Python](https://github.com/chgogos/dituoi_agp/blob/main/pl/python/notebooks/23-generators.ipynb)

## Κλειστότητες στην Python

```{.py title="closure1.py" linenums="1"}
--8<-- "src/python/closure1.py"
```

```
$ python closure1.py
Hi
```

```{.py title="closure2.py" linenums="1"}
--8<-- "src/python/closure2.py"
```

```
$ python closure2.py
Hi
```

```{.py title="closure3.py" linenums="1"}
--8<-- "src/python/closure3.py"
```

```
$ python closure3.py
Hi
Hello
```

```{.py title="closure4.py" linenums="1"}
--8<-- "src/python/closure4.py"
```

```
$ python closure4.py
INFO:root:Running "add" with arguments (3, 3)
6
INFO:root:Running "sub" with arguments (3, 3)
0
```


