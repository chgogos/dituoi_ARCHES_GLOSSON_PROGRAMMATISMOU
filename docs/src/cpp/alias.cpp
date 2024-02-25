#include <iostream>

int main() {
  int x = 10;
  int &y = x;
  y = 20; // η τιμή του x αλλάζει
  std::cout << "x=" << x << std::endl;
  std::cout << "y=" << y << std::endl;
}