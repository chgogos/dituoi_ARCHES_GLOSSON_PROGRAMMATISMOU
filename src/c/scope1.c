#include <stdio.h>

int main(void) {
  int x = 1;
  {
    int x = 2;
    int y = 3;
    printf("x=%d at line %d\n", x, __LINE__);
    printf("y=%d at line %d\n", y, __LINE__);
  }
  printf("x=%d at line %d\n", x, __LINE__);
}
