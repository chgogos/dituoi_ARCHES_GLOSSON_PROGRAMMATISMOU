:- use_module(library(clpfd)).

solve(X,Y,Z) :- 
    X in 1..20,
    Y in 1..20,
    Z in 1..20,
    X + Y + Z #= 15,
    X #> Y,
    Z #>= 2 * Y,
    label([X,Y,Z]).

% εναλλακτική λύση
solve2(X,Y,Z) :- 
    Vs = [X,Y,Z], 
    Vs ins 1..20,
    X + Y + Z #= 15,
    X #> Y,
    Z #>= 2 * Y,
    label(Vs), 
    write(Vs),
    nl,
    fail.

