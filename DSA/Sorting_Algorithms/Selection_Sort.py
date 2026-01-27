def selection_sort(arr, size):
    for index in range(size):
        min__index = index
        for j in range(index + 1, size):
            if arr[j]  < arr[min__index]:
                min__index = j
        arr[index], arr[min__index] = arr[min__index], arr[index]
arr = [10, 20, 14, 56, 45, -89, -76, 46, 34]
size = len(arr)
selection_sort(arr, size)
print(arr)