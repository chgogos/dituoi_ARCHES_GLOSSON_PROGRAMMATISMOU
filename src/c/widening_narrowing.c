#include <stdio.h>

int main() {
  // Widening Conversions (ασφαλής)
  int smallInt = 100;
  float wideFloat = smallInt;     // int -> float
  double wideDouble = wideFloat;  // float -> double

  printf("Widening Conversions:\n");
  printf("int to float: %d → %f\n", smallInt, wideFloat);
  printf("float to double: %f → %lf\n\n", wideFloat, wideDouble);

  // Narrowing Conversions (επικίνδυνο)
  double largeDouble = 123456.789;
  float narrowFloat =
      largeDouble;              // double -> float (πιθναή απώλεια ακρίβειας)
  int narrowInt = narrowFloat;  // float → int (αποκοπή δεκαδικών ψηφίων)

  printf("Narrowing Conversions:\n");
  printf("double to float: %lf → %f\n", largeDouble, narrowFloat);
  printf("float to int: %f → %d\n\n", narrowFloat, narrowInt);

  // Overflow in Narrowing
  unsigned char narrowChar = 300;  // char (0-255), 300 wraps around
  printf("Overflow in Narrowing:\n");
  printf("300 stored in unsigned char: %d\n",
         narrowChar);  // Output: 44 (300 % 256)

  return 0;
}
