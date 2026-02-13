import math

a = 0.1 + 0.2
print("0.1 + 0.2 =", a)

print("Is 0.1 + 0.2 exactly 0.3?", a == 0.3)

print("Is 0.1 + 0.2 approximately 0.3?", math.isclose(a, 0.3))
