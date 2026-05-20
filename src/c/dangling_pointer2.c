#include <stdio.h>
#include <stdlib.h>

void createDanglingPointer() {
  int *ptr = (int *)malloc(sizeof(int));
  if (ptr == NULL) {
    printf("Memory allocation failed!\n");
    return;
  }

  *ptr = 42;
  printf("Value in allocated memory: %d\n", *ptr);

  free(ptr);
  printf("Memory has been freed.\n");

  // At this point, 'ptr' is a dangling pointer because the memory has been
  // freed Dereferencing a dangling pointer is unsafe and leads to undefined
  // behavior.
  printf("Value in dangling pointer: %d\n", *ptr);  // Undefined behavior!
}

int main() {
  createDanglingPointer();
  return 0;
}
