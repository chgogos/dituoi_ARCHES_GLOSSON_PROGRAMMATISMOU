#  Μεταγλώττιση 

Μεταγλώττιση του αρχείου πηγαίου κώδικα hello.c
```
$ gcc hello.c
$ ./a.out
Hello World!
```

Σταδιακή δημιουργία ενδιάμεσων αρχείων κατά την μεταγλώττιση του αρχείου πηγαίου κώδικα hello.c
```
1. Προεπεξεργαστής
$ gcc -o hello.i hello.c -E

2. Μεταγλώττιση
$ gcc -o hello.s hello.i -S

3. Συμβολομετάφραση
$ as -o hello.o hello.s

4. Σύνδεση
$ gcc -o hello hello.o
```

Μεταγλώττιση του αρχείου πηγαίου κώδικα hello.c με δημιουργία των ενδιάμσεων αρχείων 
```
$ gcc -o hello hello.c -save-temps
$ ./hello
Hello World!
```

## Η περίπτωση του clang

Μεταγλώττιση του αρχείου πηγαίου κώδικα hello.c
```
Δημιουργία llvm bytecode
$ clang -o hello.bc hello.c -emit-llvm 


```
