def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        temp = arr[0]
        larger = [i for i in arr[1:] if i > temp]
        smaller = [i for i in arr[1:] if i < temp]
        return quick_sort(smaller) + [temp] + quick_sort(larger)


print(quick_sort([1, 5, 4, 2, 3, 6]))
