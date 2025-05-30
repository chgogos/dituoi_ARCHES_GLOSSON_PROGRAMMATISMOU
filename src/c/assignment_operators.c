#include <stdio.h>

int main() {
  // Ανάθεση (=)
  int a = 5;
  printf("Assignment: a = %d\n", a);

  // Έλεγχος ισότητας (==)
  int b = 5;
  if (a == b) {
    printf("Equality: a == b is true\n");
  } else {
    printf("Equality: a == b is false\n");
  }

  // Από δεξιά προς τα αριστερά αποτίμηση
  a = b = 7;

  // Ανάθεση με πρόσθεση (+=), ομοίως για -=, *=, /=, %=
  a += 10;  // Ισοδύναμο με: a = a + 10;
  printf("Addition Assignment: a += 10 -> a = %d\n", a);

  // Τελεστής μοναδιαίας αύξησης (++)
  int x = 3;
  printf("Initial x = %d\n", x);

  // Pre-increment (++x)
  printf("Pre-increment: ++x = %d\n", ++x);  // Πώτα αύξηση, μετά εκτύπωση

  // Post-increment (x++)
  printf("Post-increment: x++ = %d\n", x++);  // Εκτύπωση πρώτα, μετά αύξηση
  printf("After post-increment, x = %d\n", x);

  return 0;
}
