parent(kim, holly).
parent(margaret, kim).
parent(margaret, kent).
parent(esther, margaret).
parent(herbert, margaret).
parent(herbert, jean).

% εναλλακτικός τρόπος ορισμού του greatgrandparent/2
% greatgrandparent(GGP, GGC):-
%     parent(GGP, GP),
%     parent(GP, P),
%     parent(P, GGC).


grandparent(GP, GC) :-
    parent(GP, P), parent(P, GC).
greatgrandparent(GGP, GGC) :-
    grandparent(GGP, P), parent(P, GGC).


ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :-
    parent(Z, Y),
    ancestor(X, Z).

% λανθασμένος ορισμός του sibling/2, επιστρέφει false στο ερώτημα: ?- sibling(X, Y).
sibling(X, Y) :-
    \+ (X = Y),
    parent(P, X),
    parent(P, Y).

% σωστός ορισμός του sibling/2
% sibling(X, Y) :-
%     parent(P, X),
%     parent(P, Y),
%     \+ (X = Y).

% main :-
%     parent(P, jean),
%     write('The parent of jean is '), writeln(P).

% :- initialization(main, main).