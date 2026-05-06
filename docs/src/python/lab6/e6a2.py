from functools import partial


def calculate_price(price, quantity, discount, tax):
    return price * quantity * (1 - discount) * (1 + tax)


# Σταθερός φόρος 24%
calculate_with_tax = partial(calculate_price, tax=0.24)

# Σταθερή έκπτωση 10%
calculate_with_discount = partial(calculate_price, discount=0.10)

# Σταθερός φόρος 24% και σταθερή έκπτωση 10%
calculate_standard_order = partial(calculate_price, discount=0.10, tax=0.24)


print("Με σταθερό φόρο 24%:")
print(calculate_with_tax(price=100, quantity=2, discount=0.10))

print("\nΜε σταθερή έκπτωση 10%:")
print(calculate_with_discount(price=100, quantity=2, tax=0.24))

print("\nΜε σταθερό φόρο 24% και έκπτωση 10%:")
print(calculate_standard_order(price=100, quantity=2))
print(calculate_standard_order(price=50, quantity=5))
print(calculate_standard_order(price=1200, quantity=1))
