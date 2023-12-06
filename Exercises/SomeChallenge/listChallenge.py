list = [7, 3, 5, 69, 37, 1, 4, 8]

print(list)


def insertSort(list):
    for index in range(1, len(list)):

        currentvalue = list[index]
        position = index

        while position > 0 and list[position - 1] > currentvalue:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = currentvalue
        print(list)
    # print(list)

insertSort(list)