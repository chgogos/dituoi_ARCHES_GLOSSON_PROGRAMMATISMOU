#include <stdio.h>

void print_3d_array(int arr[][3][4]) {
  for (int i = 0; i < 2; i++) {
    printf("Block %d:\n", i);
    for (int j = 0; j < 3; j++) {
      for (int k = 0; k < 4; k++) {
        printf("%d ", arr[i][j][k]);
      }
      printf("\n");
    }
    printf("\n");
  }
}

int main() {
  int array[2][3][4] = {{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}},
                        {{13, 14, 15, 16}, {17, 18, 19, 20}, {21, 22, 23, 24}}};

  print_3d_array(array);
  return 0;
}
