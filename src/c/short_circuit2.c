#include <stdio.h>
#include <time.h>
#include <unistd.h>

void print(char* msg) {
  time_t now;
  struct tm* local;
  char buffer[80];
  time(&now);
  local = localtime(&now);
  strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", local);
  printf("%s printed at %s\n", msg, buffer);
}

int fun1() {
  print("fun1 started");
  sleep(5);
  print("fun1 finished");
  return 0;
}

int fun2() {
  print("fun2 started");
  sleep(5);
  print("fun2 finished");
  return 0;
}

int main() {
  print("scenario 1");
  int b1 = fun1();
  int b2 = fun2();
  if (b1 && b2) {
    print("hello");
  }

  print("\nscenario 2 (short circuit activated!)");
  if (fun1() && fun2()) {
    print("hello");
  }
}