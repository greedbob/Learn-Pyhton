def num(arr):
    if arr:
        return 1 + num(arr[1:])
    else:
        return 0


print(num([1, 2, 3, 4, 5]))
