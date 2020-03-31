def sum_(arr):
    if arr:
        return arr.pop() + sum_(arr)
    else:
        return 0


print(sum_([1, 2, 3, 4]))
