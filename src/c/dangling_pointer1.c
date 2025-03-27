#include <stdio.h>
#include <stdlib.h>

int main() {
  int *p1 = (int *)malloc(sizeof(int));
  if (p1 == NULL) {
    printf("Memory allocation failed!\n");
    return -1;
  }
  *p1 = 42;
  printf("Value in allocated memory: %d\n", *p1);
  int *p2 = p1;
  free(p1);
  printf("Memory has been freed.\n");

  printf("Value in dangling pointer: %d\n", *p2);  // Undefined behavior!
}
