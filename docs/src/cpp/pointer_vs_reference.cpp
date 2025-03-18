#include <iostream>

// Function that uses a reference to modify the original value
void modifyByReference(int &x) {
    x = x * 2; // Modifying the original value by reference
}

// Function that uses a pointer to modify the original value
void modifyByPointer(int *x) {
    if (x != nullptr) { // Check if the pointer is not null
        *x = *x * 2; // Dereferencing the pointer and modifying the value
    }
}

int main() {
    int a = 5;
    int b = 10;

    std::cout << "Original values:\n";
    std::cout << "a = " << a << ", b = " << b << std::endl;

    // Call function with reference
    modifyByReference(a);
    std::cout << "\nAfter modifyByReference:\n";
    std::cout << "a = " << a << ", b = " << b << std::endl;  // a is modified by reference

    // Call function with pointer
    modifyByPointer(&b);
    std::cout << "\nAfter modifyByPointer:\n";
    std::cout << "a = " << a << ", b = " << b << std::endl;  // b is modified by pointer

    return 0;
}
