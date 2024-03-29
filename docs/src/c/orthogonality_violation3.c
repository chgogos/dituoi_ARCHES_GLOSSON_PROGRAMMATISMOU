#include <stdio.h>

void fun(int n) {
  for (int i = 0; i < n; i++) {
    printf("fun()\n");
  }
}

int main(void) {
  int a[5];
  double b[5];
  // void c[5]; // error: declaration of 'c' as array of voids
  // void (d[5])(int); // error: declaration of 'd' as array of functions
  void *e[5];
  void (*f[5])(int);

  int x = 42;
  e[0] = &x;
  printf("%d\n", *((int *)e[0]));

  f[0] = &fun;
  f[0](5);
}
