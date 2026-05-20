:- module(pro3e1, [male/1, female/1, parent/2, ancestor/2]).

male(john).
male(george).

female(mary).
female(susan).
female(alice).

parent(john, mary).
parent(mary, susan).
parent(susan, alice).
parent(mary, george).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).