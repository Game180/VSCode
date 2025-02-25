import array

matrix = [
    array.array('i', [1, 2, 3]), # the i indicates integer
    array.array('i', [4, 5, 6]),
    array.array('i', [7, 8, 9]),
]

print(matrix[1][1])
matrix[1][1] = "Five"
# true arrays can only accept 1 data type

# for loop
for row in matrix:
    for col in row:
        print(col)