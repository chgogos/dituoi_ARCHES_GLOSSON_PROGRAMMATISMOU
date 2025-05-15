% Παράδειγμα από το βιβλίο: Αρχές Γλωσσών Προγραμματισμού, Sebesta, έκδοση 11η, εκδόσεις Γκιούρδας 
% Κεφάλαιο 16, σελίδα 706
% Διαφάνεια 31 από το πακέτο διαφανειών του βιβλίου 

speed(ford, 100).
speed(chevy, 105).
speed(dodge, 95).
speed(volvo, 80).
time(ford, 20).
time(chevy, 21).
time(dodge, 24).
time(volvo, 24).
distance(X, Y) :- speed(X, Speed),
    time(X, Time),
    Y is Speed * Time.
