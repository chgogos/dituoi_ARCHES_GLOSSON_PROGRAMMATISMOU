from functools import reduce

orders = [
    ("A101", "laptop", 1200, 1),
    ("A102", "mouse", 25, 2),
    ("A103", "keyboard", 75, 1),
    ("A104", "monitor", 300, 2),
    ("A105", "laptop", 1100, 1),
    ("A106", "mouse", 20, 3),
    ("A107", "monitor", 280, 1)
]

# 1. Συνολική αξία κάθε παραγγελίας
order_totals = list(map(
    lambda o: (o[0], o[1], o[2] * o[3]),
    orders
))

print("Συνολική αξία κάθε παραγγελίας:")
print(order_totals)


# 2. Παραγγελίες με συνολική αξία πάνω από 100 ευρώ
orders_over_100 = list(filter(
    lambda o: o[2] > 100,
    order_totals
))

print("\nΠαραγγελίες άνω των 100 ευρώ:")
print(orders_over_100)


# 3. Ομαδοποίηση order_id ανά προϊόν
orders_by_product = reduce(
    lambda acc, o: {
        **acc,
        o[1]: acc.get(o[1], []) + [o[0]]
    },
    orders,
    {}
)

print("\nOrder IDs ανά προϊόν:")
print(orders_by_product)


# 4. Συνολικά έσοδα ανά προϊόν
revenue_by_product = reduce(
    lambda acc, o: {
        **acc,
        o[1]: acc.get(o[1], 0) + o[2] * o[3]
    },
    orders,
    {}
)

sorted_products = sorted(
    revenue_by_product.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nΠροϊόντα κατά συνολική αξία φθίνουσα:")
print(sorted_products)


# 5. Προϊόν με τα μεγαλύτερα συνολικά έσοδα
top_product = reduce(
    lambda a, b: a if a[1] > b[1] else b,
    sorted_products
)

print("\nΠροϊόν με τα μεγαλύτερα συνολικά έσοδα:")
print(top_product)