from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b

print("0.1 + 0.2 using Decimal:", c)
print("Is 0.1 + 0.2 exactly 0.3?", c == Decimal('0.3'))
