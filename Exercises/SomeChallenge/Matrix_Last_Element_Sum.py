matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input())

print(matrix)

print(matrix[0][2] + matrix[1][2] + matrix[2][2])
