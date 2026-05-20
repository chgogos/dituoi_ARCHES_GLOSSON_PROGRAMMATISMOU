#include <stdio.h>


void print_3d_flat(int *arr, int x, int y, int z) {
    for (int i = 0; i < x; i++) {
        printf("Block %d:\n", i);
        for (int j = 0; j < y; j++) {
            for (int k = 0; k < z; k++) {
                int index = (i * y * z) + (j * z) + k;
                printf("%d ", arr[index]);
            }
            printf("\n");
        }
        printf("\n");
    }
}

int main() {
    int x = 2, y = 3, z = 4;
    int array[2][3][4] = {
        {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9,10,11,12}
        },
        {
            {13,14,15,16},
            {17,18,19,20},
            {21,22,23,24}
        }
    };

    // Pass the array as a flat pointer
    print_3d_flat(&array[0][0][0], x, y, z);

    return 0;
}
