#include <iostream>

int main() {
    bool a = true;
    bool b = false;

    bool c = 1;  // Equivalent to true
    bool d = 0;  // Equivalent to false

    std::cout << "a (true) = " << a << std::endl;
    std::cout << "b (false) = " << b << std::endl;
    std::cout << "c (1) = " << c << std::endl;
    std::cout << "d (0) = " << d << std::endl;

    // implicit conversion
    int x = true + false;  // true (1) + false (0) = 1
    std::cout << "true + false = " << x << std::endl;

    bool result = (5 > 3);  // true
    std::cout << "5 > 3 is " << result << std::endl;

    return 0;
}
