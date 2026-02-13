philosopher(socrates).
philosopher(plato).
politician(pericles).

human(X):- philosopher(X).
human(X):- politician(X).
mammal(X):- human(X).
mortal(X):- mammal(X).
