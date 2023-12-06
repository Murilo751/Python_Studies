matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
i = 0
j = 0
sum = 0
sumd = 0
sumsd = 0
average = 0
largest = 0
smallest = 0

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input())

        sum += matrix[i][j]

        if smallest == 0:
            smallest = matrix[i][j]

        elif matrix[i][j] < smallest:
            smallest = matrix[i][j]

        if matrix[i][j] > largest: largest = matrix[i][j]

for i in range(len(matrix)):
    sumsd += matrix[i][len(matrix[i] -1 -i)]

average = sum / 9

sumd = matrix[0][0] + matrix[1][1] + matrix[2][2]

print("The sum of all elements is: ", sum)
print("The largest element in the matrix is: ", largest)
print("The smallest element in the matrix is: ", smallest)
print("The average of the elements in the matrix is: ", average)
print("The sum of the elements in the main diagonal is: ", sumd)
print("The sum of the elements in the second diagonal is: ", sumsd)
