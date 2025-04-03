#include <stdio.h>

union Data {
  int intVal;
  float floatVal;
  char charVal;
};

int main() {
  union Data data;

  data.intVal = 10;
  printf("data.intVal = %d\n", data.intVal);

  data.floatVal = 3.14;
  printf("data.floatVal = %.2f\n", data.floatVal);

  data.charVal = 'A';
  printf("data.charVal = %c\n", data.charVal);

  printf("After overwriting, data.intVal = %d\n", data.intVal);
  printf("After overwriting, data.floatVal = %.2f\n", data.floatVal);

  return 0;
}
