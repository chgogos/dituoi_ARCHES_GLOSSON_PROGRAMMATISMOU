:- begin_tests(dituoi_tests).
:- use_module(pro3e1).

test(male_john) :- male(john).

test(female_mary) :- female(mary).

test(john_is_parent_of_mary) :- parent(john, mary).


test(direct_ancestor, [nondet]) :-  ancestor(john, mary).
test(indirect_ancestor, [nondet]) :-  ancestor(john, alice).
test(not_ancestor, [fail]) :-  ancestor(alice, john).

:- end_tests(dituoi_tests).
