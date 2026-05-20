#include <stdio.h>

int main() {
  int x = 10, y = 20;

  int max = (x > y) ? x : y;
  printf("The maximum value is: %d\n", max);

  int num = 15;
  printf("%d is %s\n", num, (num % 2 == 0) ? "even" : "odd");

  int a = -5;
  printf("%d is %s\n", a, (a > 0) ? "positive" : (a < 0) ? "negative" : "zero");

  return 0;
}