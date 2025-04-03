#include <stdio.h>

enum Day { SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY };

int main() {
  enum Day today;

  today = WEDNESDAY;

  printf("Today is WEDNESDAY, which has an integer value of: %d\n", today);

  switch (today) {
    case MONDAY:
      printf("Start of the workweek!\n");
      break;
    case FRIDAY:
      printf("Weekend is near!\n");
      break;
    case SUNDAY:
    case SATURDAY:
      printf("It's the weekend!\n");
      break;
    default:
      printf("A regular weekday.\n");
      break;
  }

  return 0;
}
