change(e, w).
change(w, e).

move([X, X, Goat, Cabbage], wolf, [Y, Y, Goat, Cabbage]) :-
    change(X, Y).

move([X, Wolf, X, Cabbage], goat, [Y, Wolf, Y, Cabbage]) :-
    change(X, Y).

move([X, Wolf, Goat, X], cabbage, [Y, Wolf, Goat, Y]) :-
    change(X, Y).

move([X, Wolf, Goat, Cabbage], nothing, [Y, Wolf, Goat, Cabbage]) :-
    change(X, Y).

guarded_or_separated(Man, Goat, Other) :-
    Man = Goat ;
    Goat \= Other.

safe([Man, Wolf, Goat, Cabbage]) :-
    guarded_or_separated(Man, Goat, Wolf),
    guarded_or_separated(Man, Goat, Cabbage).

solution(Start, Moves) :-
    solution(Start, [Start], Moves).

solution([w, w, w, w], _, []).

solution(Config, Visited, [Move | Moves]) :-
    move(Config, Move, NextConfig),
    safe(NextConfig),
    \+ member(NextConfig, Visited),
    solution(NextConfig, [NextConfig | Visited], Moves).

print_moves([]).

print_moves([Move | Moves]) :-
    writeln(Move),
    print_moves(Moves).

main :-
    solution([e, e, e, e], Moves),
    writeln('Solution:'),
    print_moves(Moves).

:- initialization(main, main).