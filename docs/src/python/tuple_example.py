# 1. Creating Tuples
tuple1 = (1, 2, 3, 4)  # A tuple of integers
tuple2 = ("apple", "banana", "cherry")  # A tuple of strings
tuple3 = (1, "banana", 3.14, True)  # A tuple with mixed data types
tuple4 = ()  # An empty tuple
tuple5 = (1,)  # A tuple with a single element (note the comma)

# 2. Accessing Tuple Elements (Indexing and Slicing)
print("First element of tuple1:", tuple1[0])  # Indexing
print("Last element of tuple2:", tuple2[-1])  # Negative indexing
print("Slicing tuple3 (from index 1 to 3):", tuple3[1:3])  # Slicing

# 3. Tuple Immutability (Can't modify elements)
# tuple1[0] = 100  # This would raise an error since tuples are immutable

# 4. Concatenating Tuples
tuple6 = tuple1 + tuple2  # Concatenating two tuples
print("\nConcatenated tuple6:", tuple6)

# 5. Repeating Tuples
tuple7 = tuple2 * 2  # Repeating tuple2 twice
print("\nRepeated tuple7:", tuple7)

# 6. Length of a Tuple
print("\nLength of tuple1:", len(tuple1))

# 7. Checking Membership
print("\nIs 'apple' in tuple2?", "apple" in tuple2)  # Membership test
print("Is 10 in tuple1?", 10 in tuple1)

# 8. Iterating through a Tuple
print("\nIterating through tuple3:")
for item in tuple3:
    print(item)

# 9. Nested Tuples
nested_tuple = (1, 2, (3, 4, 5))  # Tuple within a tuple
print("\nNested tuple:", nested_tuple)
print("Accessing element in nested tuple:", nested_tuple[2][1])  # Accessing inner tuple element

# 10. Tuple Unpacking
x, y, z = (10, 20, 30)  # Unpacking a tuple
print("\nTuple unpacking:")
print("x =", x, "y =", y, "z =", z)

# 11. Counting Occurrences of an Element
tuple8 = (1, 2, 2, 3, 4, 2)
print("\nCount of '2' in tuple8:", tuple8.count(2))

# 12. Finding the Index of an Element
print("Index of '3' in tuple8:", tuple8.index(3))
