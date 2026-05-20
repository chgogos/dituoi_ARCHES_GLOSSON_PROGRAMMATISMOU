from collections import namedtuple

Student = namedtuple("Student", ["id", "name", "grade"])

student1 = Student(1, "John Doe", 92.5)
student2 = Student(2, "Jane Smith", 88.0)

print("Student 1:")
print(f"ID: {student1.id}")
print(f"Name: {student1.name}")
print(f"Grade: {student1.grade}\n")


print("Student 2:")
print(f"ID: {student2.id}")
print(f"Name: {student2.name}")
print(f"Grade: {student2.grade}")
