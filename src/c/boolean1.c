#include <stdio.h>

int main(void) {
  if (1) {
    printf("1 is considered to be true\n");
  }

  if (-1) {
    printf("-1 is considered to be true\n");
  }

  if (3.14) {
    printf("3.14 is considered to be true\n");
  }

  if (-3.14) {
    printf("-3.14 is considered to be true\n");
  }

  if ('a') {
    printf("a is considered to be true\n");
  }

  if (!0) {
    printf("0 is considered to be false\n");
  }

  if (!0.0) {
    printf("0.0 is considered to be false\n");
  }

  if (!0.0f) {
    printf("0.0f is considered to be false\n");
  }

  if (!NULL) {
    printf("NULL is considered to be false\n");
  }
}
