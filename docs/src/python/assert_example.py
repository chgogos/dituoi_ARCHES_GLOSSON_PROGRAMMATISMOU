def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # ZeroDivisionError: division by zero
