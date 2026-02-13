# 1. Creating Lists
list1 = [1, 2, 3, 4]  # A list of integers
list2 = ["apple", "banana", "cherry"]  # A list of strings
list3 = [1, "banana", 3.14, True]  # A list with mixed data types
list4 = []  # An empty list
list5 = [1]  # A list with a single element

# 2. Accessing List Elements (Indexing and Slicing)
print("First element of list1:", list1[0])  # Indexing
print("Last element of list2:", list2[-1])  # Negative indexing
print("Slicing list3 (from index 1 to 3):", list3[1:3])  # Slicing

# 3. Modifying List Elements
list1[0] = 100  # Modify an element at a specific index
print("\nAfter modifying list1:", list1)

# 4. Adding Elements to a List
list2.append("orange")  # Adding an element to the end of the list
print("\nAfter appending 'orange' to list2:", list2)

list2.insert(1, "grape")  # Inserting an element at a specific position (index 1)
print("After inserting 'grape' at index 1:", list2)

# 5. Removing Elements from a List
list2.remove("banana")  # Removing an element by value
print("\nAfter removing 'banana' from list2:", list2)

removed_element = list2.pop(1)  # Removing and returning an element by index
print("After popping index 1:", list2)
print("Removed element:", removed_element)

# 6. Concatenating Lists
list6 = list1 + list2  # Concatenating two lists
print("\nConcatenated list6:", list6)

# 7. Repeating Lists
list7 = list2 * 2  # Repeating list2 twice
print("\nRepeated list7:", list7)

# 8. Length of a List
print("\nLength of list1:", len(list1))

# 9. Checking Membership
print("\nIs 'apple' in list2?", "apple" in list2)  # Membership test
print("Is 10 in list1?", 10 in list1)

# 10. Iterating through a List
print("\nIterating through list3:")
for item in list3:
    print(item)

# 11. Nested Lists
nested_list = [1, 2, [3, 4, 5]]  # List within a list
print("\nNested list:", nested_list)
print("Accessing element in nested list:", nested_list[2][1])  # Accessing inner list element

# 12. List Unpacking
x, y, z = [10, 20, 30]  # Unpacking a list
print("\nList unpacking:")
print("x =", x, "y =", y, "z =", z)

# 13. Counting Occurrences of an Element
list8 = [1, 2, 2, 3, 4, 2]
print("\nCount of '2' in list8:", list8.count(2))

# 14. Finding the Index of an Element
print("Index of '3' in list8:", list8.index(3))
