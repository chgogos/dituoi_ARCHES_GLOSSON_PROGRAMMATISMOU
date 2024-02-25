#include <stdio.h>

#define max(A, B) ((A) > (B) ? (A) : (B)) // εντολή προεπεξεργασίας

int main(void) {
  double x, y = 2.7, z = 13.1;
  x = max(2 * y, z / 1.7);
  printf("%.f\n", x);
}
