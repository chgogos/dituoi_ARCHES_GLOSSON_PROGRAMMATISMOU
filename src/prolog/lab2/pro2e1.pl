% https://www.cpp.edu/~jrfisher/www/prolog_tutorial/pt_framer.html

% η περιοχή Χ είναι γειτονική με τη περιοχή Υ για τον χάρτη Map 
adjacent(X,Y,Map) :- member([X,Y],Map) ; member([Y,X],Map). 

conflict(Map,Coloring) :- 
    member([R1,C],Coloring), 
    member([R2,C],Coloring), 
    adjacent(R1,R2,Map). 
