#include <iostream>
#include <string>  

int main() {
    std::string str1 = "Hello";
    std::string str2 = "World";

    // Concatenation
    std::string result = str1 + ", " + str2 + "!";  // No need for strcat
    std::cout << "Concatenated string: " << result << std::endl;

    // Getting string length
    std::cout << "Length of result: " << result.length() << std::endl;

    // Substring extraction
    std::string sub = result.substr(0, 5);  // Extract "Hello"
    std::cout << "Substring: " << sub << std::endl;

    // Finding a substring
    size_t pos = result.find("World");
    if (pos != std::string::npos) {
        std::cout << "'World' found at position: " << pos << std::endl;
    }

    // Replacing a substring
    result.replace(pos, 5, "C++");
    std::cout << "After replace: " << result << std::endl;

    // Comparing strings
    if (str1 == "Hello") {
        std::cout << "str1 is 'Hello'" << std::endl;
    }

    // Converting a string to C-style string
    const char* cstr = result.c_str();
    std::cout << "C-style string: " << cstr << std::endl;

    return 0;
}
