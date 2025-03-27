#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    int *ptr1 = &x, *ptr2 = &y;

    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(ptr1, ptr2);
    printf("After swapping: x = %d, y = %d\n", x, y);
    
    return 0;
}