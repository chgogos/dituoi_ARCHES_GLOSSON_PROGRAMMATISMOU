#include <stdio.h>

int main() {
  int arr[] = {10, 20, 30, 40, 50};
  int size = sizeof(arr) / sizeof(arr[0]);
  int i = 0;

  // Αναζήτηση ενός στοιχείου με short-circuit σε επανάληψη
  while (i < size && arr[i] != 30) {
    i++;
  }

  if (i < size) {
    printf("Found 30 at index %d\n", i);
  } else {
    printf("30 not found\n");
  }

  return 0;
}
