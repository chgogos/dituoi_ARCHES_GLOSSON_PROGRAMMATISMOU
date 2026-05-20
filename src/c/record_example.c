#include <stdio.h>
#include <string.h>

struct Student {
  int id;
  char name[50];
  float grade;
};

int main() {
  struct Student student1;
  student1.id = 1;
  strcpy(student1.name, "John Doe");
  student1.grade = 92.5;

  struct Student student2 = {2, "Jane Smith", 88.0};

  printf("Student 1:\n");
  printf("ID: %d\n", student1.id);
  printf("Name: %s\n", student1.name);
  printf("Grade: %.2f\n\n", student1.grade);

  printf("Student 2:\n");
  printf("ID: %d\n", student2.id);
  printf("Name: %s\n", student2.name);
  printf("Grade: %.2f\n", student2.grade);

  return 0;
}
