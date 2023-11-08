def insertonSort(arr):
    tam = len(arr)
    for i in range(tam):
        aux = arr[i]
        while  arr[i - 1] > aux and i > 0 :
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = aux

arr = [1,3,7,15,99,10,23,8,35,5]
print(arr)
insertonSort(arr)
print(arr)
    