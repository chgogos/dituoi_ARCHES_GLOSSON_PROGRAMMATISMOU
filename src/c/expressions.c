#include <limits.h>
#include <stdio.h>

int main() {
  printf("%d\n", 3 / 2);  // 1 (ακέραια διαίρεση)
  printf("%d\n",
         -7 / 2);  // -3 (στρογγυλοποίηση προς το μηδέν, όχι -4 όπως η Python)

  printf("%d\n", 2 < 3 < 4);  // εκτυπώνει 1, διότι (2 < 3) -> 1,  (1 < 4) -> 1
  printf("%d\n",
         2 < (3 < 4));  // εκτυπώνει 0, διότι (3 < 4) -> 1,  (2 < 1) -> 0

  printf("%d\n",
         INT_MAX + 1);  // undefined behavior (μπορεί να είναι οτιδήποτε)

  printf("%d\n", 'a' * 'b');  // 97 * 98 = 9506 (αναβάθμιση σε ακεραίους)

  int i = 10;
  printf("%d\n", i++ + i++);  // undefined behavior (μπορεί να είναι οτιδήποτε)
}