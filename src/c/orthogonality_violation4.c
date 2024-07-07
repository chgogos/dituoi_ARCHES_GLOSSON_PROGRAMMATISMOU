#include <stdio.h>

void fun(int a, int b[], int n) {
  a = 1;
  b[0] = 1;
}

int main(void) {
  int a = 0;
  int b[3] = {0, 0, 0};
  fun(a, b, 3);

  printf("%d\n", a);
  printf("%d %d %d\n", b[0], b[1], b[2]);
}
