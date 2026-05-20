#fmt:off
students = [
    ("Anna", True),
    ("Nikos", True),
    ("Maria", False),
    ("Giorgos", True)
]
#fmt:on

all_passed = all(passed for name, passed in students)
someone_failed = any(not passed for name, passed in students)

print("All students passed:", all_passed)
print("At least one student failed:", someone_failed)
