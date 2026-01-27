#LINEAR SEARCH 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [2, 3, 4, 7, 10]
target = 4
result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Element is found at index {result}")
else:
    print("Element is not found")

#BINARY SEARCH
def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
arr = [1, 90, 24, 39, 78]
target = 39
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element is found at that index{result}")
else:
    print("Element is not found")
        