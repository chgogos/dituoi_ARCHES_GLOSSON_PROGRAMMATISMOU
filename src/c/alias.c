#include <stdio.h>

int main(void) {
  int x = 10;
  int *p = &x; // το *p είναι ένα ψευδώνυμο για το x
  *p = 20;     // η τιμή του x αλλάζει
  printf("x = %d\n", x);
  printf("*p = %d\n", *p);
}
