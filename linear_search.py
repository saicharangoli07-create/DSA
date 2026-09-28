def linear_search(arr,target):
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
target = 3
result = linear_search(arr, target)
if result != -1:    
    print(f"Element found at index: {result}")