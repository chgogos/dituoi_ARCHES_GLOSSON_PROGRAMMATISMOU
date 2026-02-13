binary_to_decimal(ListOfBits, Decimal) :-
    reverse(ListOfBits, ListOfBitsR),
    binary_reversed_to_decimal(ListOfBitsR, Decimal).

binary_reversed_to_decimal([], 0).
binary_reversed_to_decimal([0 | T], Decimal):-
    binary_reversed_to_decimal(T, Decimal2),
    Decimal is 2 * Decimal2.

binary_reversed_to_decimal([1 | T], Decimal):-
    binary_reversed_to_decimal(T, Decimal2),
    Decimal is 2 * Decimal2 + 1.
