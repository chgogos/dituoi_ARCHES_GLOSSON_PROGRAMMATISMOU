#include <stdio.h>
#include <stdlib.h>

void createMemoryLeak(int iteration) {
    int *ptr = (int *)malloc(5 * sizeof(int)); // Allocating memory for 5 integers
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return;
    }
    
    // Assigning values
    for (int i = 0; i < 5; i++) {
        ptr[i] = i * 10;
    }
    
    // Printing values
    printf("Allocated memory region %d: ", iteration);
    for (int i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");
    
    // Memory leak occurs because we forget to free(ptr)
    printf("Memory at address %p is not freed.\n", (void*)ptr);
}

void memoryLeak() {
    for (int i = 0; i < 3; i++) {
        createMemoryLeak(i + 1);
    }
}

int main() {
    memoryLeak();
    return 0;
}
