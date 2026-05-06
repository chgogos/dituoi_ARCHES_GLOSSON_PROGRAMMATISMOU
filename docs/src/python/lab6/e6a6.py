#fmt:off
students = [
    ("Anna", True),
    ("Nikos", True),
    ("Maria", False),
    ("Giorgos", True)
]
#fmt:on

all_passed = True
someone_failed = False

for name, passed in students:
    if not passed:
        all_passed = False
        someone_failed = True

print("All students passed:", all_passed)
print("At least one student failed:", someone_failed)
