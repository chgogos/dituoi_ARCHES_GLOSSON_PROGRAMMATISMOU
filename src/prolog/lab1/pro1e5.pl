my_length([], 0).
my_length([_ | T], L) :-
        my_length(T, TailLength),
        L is TailLength + 1.

my_member(X, [X | _]).
my_member(X, [_ | T]) :- 
        my_member(X, T).

my_sum_list([], 0).
my_sum_list([H | T], Sum) :-
        my_sum_list(T, SumTail),
        Sum is H + SumTail.
