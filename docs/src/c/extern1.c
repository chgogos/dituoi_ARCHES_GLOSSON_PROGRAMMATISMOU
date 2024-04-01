#include <stdio.h>

int g = 100;

void fun1() {
  extern int e;
  printf("%d e=%d\n", __LINE__, e);
  printf("%d g=%d\n", __LINE__, g);
}

int e = 3;

int main(void) {
  int a = 1;
  printf("%d a=%d\n", __LINE__, a);
  printf("%d e=%d\n", __LINE__, e);
  printf("%d g=%d\n", __LINE__, g);
  fun1();
}
