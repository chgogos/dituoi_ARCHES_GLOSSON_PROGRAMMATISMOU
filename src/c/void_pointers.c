#include <stdio.h>

void printValue(void *ptr, char type) {
  switch (type) {
    case 'i':
      printf("Integer: %d\n", *(int *)ptr);
      break;
    case 'f':
      printf("Float: %.2f\n", *(float *)ptr);
      break;
    case 'c':
      printf("Character: %c\n", *(char *)ptr);
      break;
    default:
      printf("Unknown type\n");
  }
}

int main() {
  int a = 10;
  float b = 5.5;
  char c = 'A';

  void *ptr;

  ptr = &a;
  printValue(ptr, 'i');

  ptr = &b;
  printValue(ptr, 'f');

  ptr = &c;
  printValue(ptr, 'c');

  return 0;
}
