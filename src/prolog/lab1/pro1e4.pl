doublefactorial(0,1).
doublefactorial(1,1).
doublefactorial(N,F) :-
    N>0,
    N1 is N-2,
    doublefactorial(N1,F1),
    F is F1*N.
