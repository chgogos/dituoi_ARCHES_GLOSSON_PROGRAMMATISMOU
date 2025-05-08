#include <stdio.h>

int counter = 0; // Global variable affecting function behavior

int nonReferentialTransparentFunction(int x) {
    counter++; // Side effect: modifies global state
    return x + counter;
}

int main() {
    int a = 5;
    
    // Calling the function multiple times with the same argument
    printf("First call: %d\n", nonReferentialTransparentFunction(a));
    printf("Second call: %d\n", nonReferentialTransparentFunction(a));
    printf("Third call: %d\n", nonReferentialTransparentFunction(a));
    
    return 0;
}