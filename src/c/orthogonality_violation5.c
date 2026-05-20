#include <stdio.h>

void fun1(void) {
  int a = 0;
  int b = 4;
  a = a + b;
  printf("%d\n", a);
}

void fun2(void) {
  float array[5] = {1.1, 1.2, 1.3, 1.4, 1.5};
  float *a = array;
  printf("%p %f\n", a, *a);

  int b = 4;
  a = a + b;
  printf("%p %f\n", a, *a);
}

int main(void) {
  fun1();
  fun2();
}
