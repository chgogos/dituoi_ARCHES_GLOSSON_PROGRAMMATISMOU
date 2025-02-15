#include <stdio.h>
#define NDEBUG
#include <assert.h>


void divide(int a, int b) {
    assert(b != 0);  // Ensure the divisor is not zero
    printf("Result: %d\n", a / b);
}

int main() {
    int x = 10, y = 2;
    divide(x, y);  // This works fine

    y = 0;
    divide(x, y);  // This will trigger the assertion failure

    return 0;
}
