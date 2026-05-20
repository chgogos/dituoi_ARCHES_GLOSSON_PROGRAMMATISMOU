#include <stdio.h>
#include <string.h>

int main() {
  char str[] = "Hello, C!";

  int length = strlen(str);

  printf("String: %s\n", str);
  printf("Length of the string: %d\n", length);

  return 0;
}
