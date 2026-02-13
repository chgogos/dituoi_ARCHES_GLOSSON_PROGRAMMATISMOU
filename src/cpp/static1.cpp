#include <iostream>

using namespace std;

void fun() {
  static int x = 0;
  x++;
  cout << x << endl;
}

int main() {
  for (int i = 0; i < 10; i++) {
    fun();
  }
}
