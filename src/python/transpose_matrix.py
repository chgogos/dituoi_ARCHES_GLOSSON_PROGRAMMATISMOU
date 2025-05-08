def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [[1, 2, 3], [4, 5, 6]]

transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)
