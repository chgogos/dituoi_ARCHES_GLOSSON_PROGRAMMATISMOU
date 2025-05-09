#include <iostream>

using namespace std;

int adder(int list[], int listlen) {
  static int sum = 0; // στατική τοπική μεταβλητή
  int count; // τοπική μεταβλητή δυναμική-στοίβας
  for (count = 0; count < listlen; count++) {
    sum += list[count];
  }
  return sum;
}

int main() {
  int a[] = {1, 2, 3};    // το άθροισμα των τιμών είναι 6
  int b[] = {4, 5, 6, 7}; // -> το άθροισμα των τιμών είναι 22
  cout << adder(a, 3) << endl; // εμφανίζει 6
  cout << adder(b, 4) << endl; // εμφανίζει 28
}
