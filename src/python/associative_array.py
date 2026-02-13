# Creating an associative array using a dictionary
associative_array = {}

associative_array["apple"] = 3
associative_array["banana"] = 5
associative_array["orange"] = 2

print(f"apple: {associative_array['apple']}")
print(f"banana: {associative_array['banana']}")
print(f"orange: {associative_array['orange']}")

for key, value in associative_array.items():
    print(f"{key}: {value}")
