# Haskell

H Haskell είναι μια αμιγώς συναρτησιακή γλώσσα προγραμματισμού (pure functional programming language) οκνηρής αποτίμησης (lazy evaluation). Η Haskell διαθέτει ισχυρό στατικό σύστημα τύπων (strong static type system) που αντιλαμβάνεται τους τύπους που απαιτούνται για τις συναρτήσεις και τις παραμέτρους τους.

Τα παραδείγματα κώδικα που ακολουθούν είναι από το "[7 Languages in 7 Weeks, by Bruce A. Tate - A Pragmatic Guide to Learning Programming Languages](https://pragprog.com/titles/btlang/seven-languages-in-seven-weeks/)" και από άλλες πηγές.


## Εγκατάσταση της Haskell
H Haskell (η Glasgow Haskell) μπορεί να εγκατασταθεί χρησιμοποιώντας το GHCup, ακολουθώντας τις οδηγίες από το <https://www.haskell.org/downloads/>. 

## Ο διερμηνευτής της Haskell
Ενεργοποίηση και τερματισμός του διερμηνευτή ghci της Haskell.

```
$ ghci
GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
ghci> "Hello World"
"Hello World"
ghci> :quit
Leaving GHCi.
$
```

## Εκφράσεις και βασικοί τύποι

**Αριθμοί**

```hs
ghci> 1 + 2
3
ghci> (+) 1 2
3
ghci> 1 + 2 * 3
7
ghci> 1 + 2 * 3.0
7.0
ghci> 2 ^ 10
1024
ghci> div 10 3
3
ghci> 10 `div` 3 -- div ως infix τελεστής με backticks `
3
ghci> mod 10 3
1
ghci> 10 `mod` 3 -- mod ως infix τελεστής με backticks `
1
ghci> gcd 24 56
8 
```

**Λεκτικά**

```hs
ghci> "hi"
"hi"
ghci> "hello " ++ "world"
"hello world"
-- δεικτοδότηση λεκτικού με το !!
ghci> "hello" !! 1
'e'
```

**Χαρακτήρες**

Ένα λεκτικό είναι μια λίστα χαρακτήρων.

```hs
ghci> 'a'
'a'
ghci> ['a', 'b']
"ab"
```

**Λογικές τιμές**

```hs
ghci> 1 == 2-1
True
ghci> 1 /= 1
False
ghci> "Arta" == ['A','r','t','a']
True
```

## Συναρτήσεις

Οι συναρτήσεις στην Haskell αποτελούνται από δύο τμήματα. Ένα προαιρετικό τμήμα δήλωσης του τύπου της συνάρτησης. Ένα τμήμα με την υλοποίηση της συνάρτησης. Η Haskell έχει ένα ισχυρό σύστημα συμπερασμού για τον εντοπισμό των τύπων που χρησιμοποιούνται στις συναρτήσεις.

Πρόσδεση (binding) της μεταβλητής `x` σε τοπική εμβέλεια.

```hs
> let x = 42
> x
42
```

Πρόσδεση της συνάρτησης `double` σε τοπική εμβέλεια.

```hs
> let double x = 2 * x
> double 21
42
```

Αποθήκευση συνάρτησης σε αρχείο.

```hs
double :: Integer -> Integer
double x = 2 * x
```

??? note "Αρχείο day1.hs με ορισμούς των συναρτήσεων: double, fact, factpm, factg, fibpm, fibt, fibc, size, prod, allEven"
    ```{.hs title="day1.hs" linenums="1"}
    --8<-- "src/haskell/7L7W/day1.hs"
    ```
Φόρτωση κώδικα, κλήση συνάρτησης.

```
$ ghci
GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
ghci> :load day1.hs
ghci> double 10
20
Main> :quit
Leaving GHCi
```

ή 

```
$ ghci day1.hs
GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
ghci> double 10
20
ghci> :quit
```


## Αναδρομή (recursion)

Ορισμός της συνάρτησης fact απευθείας στο ghci

```
ghci> let fact x = if x == 0 then 1 else fact (x - 1) * x
ghci> fact 3
6
```

**Αντιστοίχιση μοτίβων (pattern matching)**

Ορισμός της multiline συνάρτησης factpm απευθείας στο ghci, προσοχή στη χρήση των συμβόλων `:{` και `:}`.

```
ghci> :{
ghci| factpm :: Integer -> Integer
ghci| factpm 0 = 1
ghci| factpm x = x * factpm (x - 1)
ghci| :}
ghci> factpm 10
3628800
```

**Φρουροί (guards)**

Οι φρουροί είναι συνθήκες που περιορίζουν τις τιμές των ορισμάτων όπως στη συνέχεια. Όταν η συνθήκη ενός φρουρού ικανοποιείται η Haskell καλεί την κατάλληλη συνάρτηση.

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
factg :: Integer -> Integer
factg x
    | x > 1 = x * factg (x-1)
    | otherwise 1
```

```
$ ghci day1.hs 
ghci> factg 5
120
```

## Πλειάδες και λίστες

Στις πλειάδες τα στοιχεία μπορούν να είναι διαφορετικού τύπου ενώ στις λίστες όλα τα στοιχεία είναι του ίδιου τύπου. 

Μια λίστα και μια πλειάδα. Με το ```:type``` μπορούμε να δούμε τον τύπο μιας έκφρασης.

```
ghci>:type [1,2,3]
[1,2,3] :: Num a => [a]
ghci> :type ('1', "2", 3, 4)
('1', "2", 3, 4) :: (Num c, Num d) => (Char, String, c, d)
```

**Πρώτο (fst) και δεύτερο (snd) στοιχείο σε μια πλειάδα**

```
ghci> fst (1,2)
1
ghci> snd (1,2)
2
```

Συνάρτηση εύρεσης όρων της ακολουθίας fibonacci.

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
fib :: Integer -> Integer
fib 0 = 1
fib 1 = 1
fib x = fib (x - 1) + fib (x - 2)
```

```
ghci> fib 10
10946
```

Υλοποίηση ταχύτερης έκδοσης της συνάρτησης fib (με χρήση πλειάδων).

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
fibTuple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
fibTuple (x, y, 0) = (x, y, 0)
fibTuple (x, y, index) = fibTuple (y, x + y, index - 1)

fibResult :: (Integer, Integer, Integer) -> Integer
fibResult (x, y, z) = x

fib :: Integer -> Integer
fib x = fibResult (fibTuple (0, 1, x))
```

```hs
ghci> fib 100
354224848179261915075
```

**head, tail, init, last σε λίστες**

```
ghci> head [1,2,3,4]
1
ghci> tail [1,2,3,4]
[2,3,4]
ghci> let (h:t) = [1,2,3,4]
ghci> h
1
ghci> t
[2,3,4]
ghci> init [1,2,3,4]
[1,2,3]
ghci> last [1,2,3,4]
4
```

**Σύνθεση (composition)**

```
ghci> let second = head . tail
ghci> second [1,2,3]
second = 2
```

## Διάσχιση λιστών

**Μέγεθος λίστας**

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
size [] = 0
size (h:t) = 1 + size t
```

```
ghci> size [1,2,3,4]
4
```

**Γινόμενο τιμών λίστας**

```hs
ghci> product [1,2,3,4]
24
```

**Συνδυασμός λιστών με το zip**

```hs
ghci> zip [1,2,3,4] [5,6,7,8]
[(1,5),(2,6),(3,7),(4,8)]
```

**Συνδυασμός λιστών με συνάρτηση με το zipWith**

```
ghci> zipWith (*) [1,2,3,4] [5,6,7,8]
[5,12,21,32]
```


## Δημιουργία λιστών

Το σύμβολο ```:``` λέγεται cons και διαχωρίζει την κεφαλή από την ουρά της λίστας. 

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
ghci> 1:[2,3]
[1,2,3]
```

**Συνάρτηση που επιστρέφει μια λίστα με τους άρτιους αριθμούς μιας λίστας**

```hs
-- ο κώδικας βρίσκεται στο αρχείο day1.hs
allEven :: [Integer] -> [Integer]
allEven [] = []
allEven (h:t) = if even h then h:allEven t else allEven t
```


```hs
ghci> allEven [1,2,3,4,5,6]
[2,4,6]
```

**Περιοχές τιμών (ranges)** 

```
ghci> [1..10]
[1,2,3,4,5,6,7,8,10]
ghci> [0,5..10]
[0,5,10]
ghci> [2, 1.5, 0]
[2.0,1.5,1.0,0.5,0.0]
```

**Μη φραγμένες περιοχές τιμών** 

```
ghci> take 5 [1..]
[1,2,3,4,5]
```

**Περιφραστικές λίστες (list comprehensions)**

```
ghci> [x * 2 | x <- [1, 2, 3]]
[2,4,6]
ghci> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
ghci> [ (y, x) | (x, y) <- [(1, 2), (2, 3), (3, 1)]]
[(2,1),(3,2),(1,3)]
ghci> let a = [1..10]
ghci> let b = [0,5,20]
ghci> [(x,y) | x <- a, y<-b]
[(1,0),(1,5),(1,20),(2,0),(2,5),(2,20),(3,0),(3,5),(3,20),(4,0),(4,5),(4,20),(5,0),(5,5),(5,20),(6,0),(6,5),(6,20),(7,0),(7,5),(7,20),(8,0),(8,5),(8,20),(9,0),(9,5),(9,20),(10,0),(10,5),(10,20)]
ghci> [(x,y) | x <- a, y<-b, x < y]
[(1,5),(1,20),(2,5),(2,20),(3,5),(3,20),(4,5),(4,20),(5,20),(6,20),(7,20),(8,20),(9,20),(10,20)]
```

## Συναρτήσεις υψηλότερης τάξης

??? note "Αρχείο day2.hs με ορισμούς των συναρτήσεων: squareAll, myRange"
    ```{.hs title="day2.hs" linenums="1"}
    --8<-- "src/haskell/7L7W/day2.hs"
    ```

**Ανώνυμες συναρτήσεις**

Η σύνταξη των ανώνυμων συναρτήσεων (λάμδα συναρτήσεων) στη Haskell είναι η ακόλουθη:

```
(\param1 .. paramn -> function_body)
```

Μια ανώνυμη συνάρτηση επιστροφής του τετραγώνου της παραμέτρου της και η κλήση της με παράμετρο την τιμή 5.

```
ghci> (\ x -> x * x) 5
25
```

Μια ανώνυμη συνάρτηση με δύο παραμέτρους:

```
ghci> (\ x y-> x * y) 5 7
35
```

**map**

```
ghci> map (\x -> x * x) [1, 2, 3]
[1, 4, 9]
```

```hs
-- ο κώδικας βρίσκεται στο αρχείο day2.hs
squareAll :: Num b => [b] -> [b]
squareAll list = map square list
    where square x = x *x
```

```
ghci> squareAll [1, 2, 3]
[1,4,9]
```

H `(+1)` είναι μια μερικά εφαρμοσμένη συνάρτηση. Πρόκειται για τη συνάρτηση `+` στην οποία έχει προσδεθεί η μια από τις δύο παραμέτρους με τιμή 1. Η δεύτερη παράμετρος σε κάθε κλήση της συνάρτησης θα είναι μια τιμή της λίστας.

```
ghci> map (+1) [1,2,3]
[2,3,4]
```

**filter**

```
ghci> filter odd [1, 2, 3, 4, 5]
[1, 3, 5]
```

**foldl**

```
ghci> foldl (\x sum -> sum + x) 0 [1, 2, 3, 4]
10
```

```
ghci> foldl (+) 0 [1,2,3,4]
10
```

```
ghci> foldl1 (+) [1,2,3,4]
10
```

## Μερικά εφαρμοσμένες συναρτήσεις και currying

Στη Haskell κάθε συνάρτηση ουσιαστικά έχει μια μόνο παράμετρο.

```
ghci> let prod x y = x * y
ghci> prod 3 4
12
ghci> (prod 3) 4
12
ghci> tripple = prod 3
ghci> tripple 40
12
```

## Οκνηρή αποτίμηση

H Haskell επιτρέπει άπειρες λίστες να επιστρέφονται από συναρτήσεις.

Ορισμός μιας άπειρης λίστας.

```hs
-- ο κώδικας βρίσκεται στο αρχείο day2.hs
myRange :: Num t => t -> t -> [t]
myRange start step = start:(myRange (start + step) step)
```

```
ghci> take 5 (myRange 10 2)
[10,12,14,16,18]
```

Σύνταξη της Haskell για μη φραγμένες περιοχές τιμών.

```
ghci> take 10 [1..]
[1,2,3,4,5,6,7,8,9,10]
ghci> take 10 [1,3..]
[1,3,5,7,9,11,13,15,17,19]
```

## Τύποι

**Πρωτογενείς τύποι**

```
ghci> :type 'a'
'a' :: Char
ghci> :type True
True :: Bool
```

??? note "Αρχείο day3.hs με ορισμούς τύπων δεδομένων: Suit, Rank, Card, Hand, Tree"
    ```{.hs title="day3.hs" linenums="1"}
    --8<-- "src/haskell/7L7W/day3.hs"
    ```

**Τύποι ορισμένοι από τον χρήστη**

```hs
-- ο κώδικας βρίσκεται στο αρχείο day3.hs
data Suit = Spades | Hearts deriving (Show)
data Rank = Ten | Jack | Queen | King | Ace deriving (Show)
type Card = (Rank, Suit)
type Hand = [Card]
```

**Αναδρομικοί τύποι**

```hs
-- ο κώδικας βρίσκεται στο αρχείο day3.hs
data Tree a = Children [Tree a] | Leaf a deriving (Show)
```

```
ghci> let tree = Children[Leaf 1, Children [Leaf 2, Leaf 3]]
ghci> tree
Children[Leaf 1, Children [Leaf 2, Leaf 3]]
```

<!-- **Κλάσεις**

Στην Haskell μια κλάση ορίζει ένα πρωτόκολλο λειτουργιών (σύνολο από συναρτήσεις) που πρέπει να υποστηρίζει ένας τύπος έτσι ώστε ο τύπος να θεωρείται στιγμιότυπο της κλάσης. -->


## Μεταγλώττιση και εκτέλεση κώδικα

```{.hs title="example1.hs" linenums="1"}
--8<-- "src/haskell/example1.hs"
```

**Εκτέλεση από τον διερμηνευτή ghci**
```
$ ghci example1.hs
GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
[1 of 2] Compiling Main             ( example1.hs, interpreted )
Ok, one module loaded.
ghci> main
1405006117752879898543142606244511569936384000000000
```

**Μεταγλώττιση από το ghc, εκτέλεση**
```
$ ghc example1.hs
[1 of 2] Compiling Main             ( example1.hs, example1.o )
[2 of 2] Linking example1
$ ./example1
1405006117752879898543142606244511569936384000000000
```

## Ανάγνωση και εγγραφή σε αρχεία

Ανάγνωση από το αρχείο κειμένου [input_for_haskell.txt](src/haskell/input_for_haskell.txt)

```{.hs title="fileReadFrom.hs" linenums="1"}
--8<-- "src/haskell/fileReadFrom.hs"
```

Μεταγγλώττιση και εκτέλεση:
```
$ ghc fileReadFrom.hs
[1 of 2] Compiling Main             ( fileReadFrom.hs, fileReadFrom.o )
[2 of 2] Linking fileReadFrom
$ ./fileReadFrom
[["maria","8"],["petros","9"],["kostas","5"]]
```

Εγγραφή περιεχομένων λίστας στο αρχείο κειμένου "output_from_haskell.txt"
```{.hs title="fileWriteTo.hs" linenums="1"}
--8<-- "src/haskell/fileWriteTo.hs"
```

Μεταγγλώττιση και εκτέλεση:
```
$ ghc fileWriteTo.hs
[1 of 2] Compiling Main             ( fileWriteTo.hs, fileWriteTo.o )
[2 of 2] Linking fileWriteTo
$ ./fileWriteTo
"Write successed!"
```

## Βιβλία - σημειώσεις
* [Σταματόπουλος, Π. (2015). Λογικός και συναρτησιακός προγραμματισμός [Προπτυχιακό εγχειρίδιο]. Κάλλιπος, Ανοικτές Ακαδημαϊκές Εκδόσεις. https://hdl.handle.net/11419/3587](https://repository.kallipos.gr/handle/11419/3587)
* [Learn You a Haskell for Great Good](http://learnyouahaskell.com/chapters)

## Videos
* [Graham Hutton - Functional Programming](https://www.youtube.com/channel/UCBDp7ydYTHi1dh4Gnf3VTPA)
* [Philipp Hagenlocher - Haskell for Imperative Programmers](https://www.youtube.com/watch?v=Vgu82wiiZ90&list=PLe7Ei6viL6jGp1Rfu0dil1JH1SHk9bgDV)
* [Curtis D'Alves - Learning Haskell](https://www.youtube.com/playlist?list=PLHRF-X-NtQR4MZBvm05NshPIEI8ELID5m)

## Haskell documentation
* [Hoogle](https://hoogle.haskell.org/)
* [Search Haskell packages](https://flora.pm/)

## Πηγές
* [Learning Haskell](https://wiki.haskell.org/Learning_Haskell)
* [Learn X in Y minutes](https://learnxinyminutes.com/docs/haskell/)
