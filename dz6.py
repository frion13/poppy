def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  
        elif mid_val < target:
            low = mid + 1 
        else:
            high = mid - 1 

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден по индексу {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")
