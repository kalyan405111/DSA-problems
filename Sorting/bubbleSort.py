def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 2, -1, -1):
        swapped = False
        for j in range(i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr   # early exit once sorted
    return arr

print(bubble_sort([3,6,9,3,5,7,1,8,99,3]))
