#include <stdio.h>

int main() {
  int sum = 0, num;
  while ((num = 3)) {
    sum += num;
    if (sum > 10) break;
  }
  printf("Sum after loop: %d\n", sum);

  return 0;
}
