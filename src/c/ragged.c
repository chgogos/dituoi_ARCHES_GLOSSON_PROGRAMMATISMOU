#include <stdio.h>
#include <stdlib.h>

int main() {
  int rows = 3;
  int* arr[rows];

  // Allocate different lengths for each row
  arr[0] = (int*)malloc(3 * sizeof(int));
  arr[1] = (int*)malloc(5 * sizeof(int));
  arr[2] = (int*)malloc(2 * sizeof(int));

  arr[0][0] = 1;
  arr[0][1] = 2;
  arr[0][2] = 3;
  arr[1][0] = 4;
  arr[1][1] = 5;
  arr[1][2] = 6;
  arr[1][3] = 7;
  arr[1][4] = 8;
  arr[2][0] = 9;
  arr[2][1] = 10;

  for (int i = 0; i < rows; i++) {
    printf("Row %d: ", i + 1);
    for (int j = 0; j < (i == 0 ? 3 : (i == 1 ? 5 : 2)); j++) {
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }

  for (int i = 0; i < rows; i++) {
    free(arr[i]);
  }

  return 0;
}
