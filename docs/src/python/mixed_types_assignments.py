# Integer to float (widening)
i = 10
f = float(i)  # Explicit conversion (optional, as Python allows direct assignment)
print(f"Widening: i (int) = {i}, f (float) = {f:.2f}")

# Float to int (narrowing)
pi = 3.14159
x = int(pi)  # Explicit conversion, truncates decimal part
print(f"Narrowing: pi (float) = {pi}, x (int) = {x}")

# String to int (valid case)
s = "42"
num = int(s)  # Converts string to integer
print(f"String to int: s = '{s}', num = {num}")

# Invalid string to int (error)
try:
    invalid_s = "9"
    num = int(invalid_s)  # Will raise ValueError
except ValueError:
    print(f"Cannot convert '{invalid_s}' to int!")

# Integer to string
n = 123
s = str(n)  # Converts int to string
print(f"Int to string: n = {n}, s = '{s}'")

# Float to string
f = 99.99
s = str(f)  # Converts float to string
print(f"Float to string: f = {f}, s = '{s}'")

# Boolean to int
b = True
num = int(b)  # True → 1, False → 0
print(f"Boolean to int: b = {b}, num = {num}")

# Int to boolean
num = 0
b = bool(num)  # 0 → False, nonzero → True
print(f"Int to boolean: num = {num}, b = {b}")

# Implicit conversion (int to float in expression)
result = 5 + 2.5  # Python automatically promotes int to float
print(f"Implicit conversion: 5 + 2.5 = {result} (type: {type(result)})")
