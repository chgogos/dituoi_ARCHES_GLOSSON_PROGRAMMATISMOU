#include <stdio.h>
#include <unistd.h>

int fun1() {
  printf("fun1 started\n");
  sleep(5);
  printf("fun1 finished\n");
  return 0;
}

int fun2() {
  printf("fun2 started\n");
  sleep(5);
  printf("fun2 finished\n");
  return 0;
}

int main() {
  // scenario 1
  int b1 = fun1();
  int b2 = fun1();
  if (b1 && b2) {
    printf("hello\n");
  }

  // scenario2 (short circuit)
  if (fun1() && fun2()) {
    printf("hello\n");
  }
}