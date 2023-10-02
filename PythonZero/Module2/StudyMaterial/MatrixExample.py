# Simplified form
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Original matrix:")
print("-"*35)
for row in matrix:
    print(row)

print("Transposed matrix:")
print("-"*35)
for row in transposed_matrix:
    print(row)


# Derived form
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposed_matrix1 = []

for i1 in range(len(matrix1[0])):
    transposed_row1 = []
    for row1 in matrix1:
        transposed_row1.append(row1[i1])
    transposed_matrix1.append(transposed_row1)

print("Original matrix:")
print("-"*35)
for row1 in matrix:
    print(row1)

print("Transposed matrix:")
print("-"*35)
for row1 in transposed_matrix1:
    print(row1)