def find_max(arr):
    if not arr:
        return -1
    elif len(arr) > 1:
        temp = arr[-1] if arr[-1] > arr[-2] else arr[-2]
        return find_max(arr[:-2] + [temp])
    else:
        return arr[-1]


print(find_max([1, 2, 7, 4, 5]))
